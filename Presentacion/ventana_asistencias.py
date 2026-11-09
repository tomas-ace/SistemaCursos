from tkinter import *
from tkinter import messagebox
from Servicios.asistencia_service import *
from Presentacion.elementos import *
from Servicios.clase_service import *
from datetime import *
class Ventana_Asistencia():
    def __init__(self,contenido):
        self._contenido=contenido
    
    def lista_presencias(self,id_clase,ventana_anterior=None):
        if ventana_anterior is not None:
            ventana_anterior.destroy()
        ventana_asistencias = Toplevel(self._contenido)
        ventana_asistencias.title(f"Asistencias - Clase {id_clase}")
        ventana_asistencias.geometry("550x400")
        ventana_asistencias.maxsize(550,400)
        
        
        ventana_asistencias.configure(bg="white") 
        
        Label(
            ventana_asistencias, 
            text="Registro de Asistencias", 
            font=("Arial", 16, "bold"), 
            bg="white"
        ).pack(pady=15)
        
        servicio_asistencia = Asistencia_Service()
        
        
        datos_asistencias = servicio_asistencia.asistencia_por_clase(id_clase) 
        
        
        encabezados = ["IdInsc","Nombre","Apellido", "Fecha", "Estado"]
        
        
        frame_tabla = Frame(ventana_asistencias)
        frame_tabla.pack(fill="both", expand=True, padx=20, pady=10)
        
        
        tree=treeview(frame_tabla, encabezados, datos_asistencias)
        tree["displaycolumns"] = ("Nombre", "Apellido", "Fecha", "Estado")
        frame_boton=Frame(ventana_asistencias)
        frame_boton.pack(padx=20, pady=10)
        Button(
                frame_boton, text="Tomar Lista", bg=azul, fg=blanco, font=("Arial", 12, "bold"),
                command=lambda: self.ventana_tomar_lista(id_clase,ventana_asistencias)
            ).grid(pady=10,column=0,row=0,padx=5)
        Button(
                frame_boton, text="Editar Estado", bg=azul, fg=blanco, font=("Arial", 12, "bold"),
                command=lambda: self.editar_asistencia(tree,ventana_asistencias,id_clase)
            ).grid(pady=10,column=1,row=0,padx=5)
                
    def editar_asistencia(self,tree,ventana,id_clase):
        servicio_classe=Clase_Service()
        if servicio_classe.esta_inactiva(id_clase):
            messagebox.showerror("Error","No puedes modificar asistencia en una clase inactiva")
            return
        seleccion = tree.selection()
        if not seleccion:
            messagebox.showerror("Error","Seleccione una asistencia")
            return
        
        item_id = seleccion[0]
        datos_clase = tree.item(item_id)['values']
        ventana.destroy()
        id_insc=datos_clase[0]
        fecha=datos_clase[3]
        estado=datos_clase[4]
        service=Asistencia_Service()
        service.editar_estado(id_insc,fecha,estado)
        self.lista_presencias(id_clase)
                    
                    
    def ventana_tomar_lista(self, id_clase,ventana_anterior):
        servicio_classe=Clase_Service()
        servicio_classe=Clase_Service()
        if servicio_classe.esta_inactiva(id_clase):
            messagebox.showerror("Error","No puedes tomar lista en una clase inactiva")
            return
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        servicio_asistencia = Asistencia_Service()
        if servicio_asistencia.existe_asistencia(fecha_actual, id_clase):
            messagebox.showinfo("Información", "La asistencia para esta clase ya ha sido registrada hoy.")
            return
        alumnos=servicio_classe.lista_de_alumnos_por_clase(id_clase)
        ventana = Toplevel(self._contenido)
        ventana.title("Tomar Lista")
        ventana.geometry("700x600")
        ventana.configure(bg=blanco)

        

        lista_asistencia = [] 

        frame_alumnos = Frame(ventana, bg=blanco)
        frame_alumnos.pack(pady=10)

        fila = 0
        for alumno in alumnos:
            nombre = f"{alumno[1]} {alumno[2]}"
            id_inscripcion=alumno[3]
            presencia = StringVar(value="Ausente") 
            
            lista_asistencia.append([id_inscripcion, presencia])

            Label(
                frame_alumnos, text=nombre, bg=blanco, bd=1, width=25, anchor="w", padx=10, pady=5
            ).grid(row=fila, column=0, pady=5, padx=20)

            Radiobutton(frame_alumnos, text="Presente", variable=presencia, value="Presente", bg=blanco).grid(row=fila, column=1)
            Radiobutton(frame_alumnos, text="Ausente", variable=presencia, value="Ausente", bg=blanco).grid(row=fila, column=2)
            
            fila += 1 

        Button(
            ventana, text="Guardar Asistencia", bg=azul, fg=blanco, font=("Arial", 12, "bold"),
            command=lambda: self.guardar_asistencia(fecha_actual, ventana,lista_asistencia,id_clase,ventana_anterior)
        ).pack(pady=20)
    
    
    def guardar_asistencia(self, fecha, ventana,lista,id_clase,ventana_anterior):
        asistencia_service= Asistencia_Service()
        quedo_alguno_libre=False
        for alumno in lista:
            
            id_inscripcion=alumno[0]
            estado = alumno[1].get() 
            asistencia=Asistencia(fecha,estado,id_inscripcion)
            
            resultado=asistencia_service.registrar_asistencia(asistencia)
            if resultado==True:
                quedo_alguno_libre=True
        if quedo_alguno_libre:
            messagebox.showwarning("Atención", "Uno o mas alumnos han superado el límite de inasistencias y su estado cambió automáticamente a 'Libre'.")
        asistencia_service.registrar_libres_y_bajas(fecha,id_clase)
        servicio_clase = Clase_Service()
        
        if servicio_clase.curso_finalizado(id_clase):
            respuesta = messagebox.askyesno(
                "Fin de Cursada Detectado", 
                "Se ha alcanzado el límite de clases previstas para este curso. ¿Desea cerrar la clase ahora y calcular los promedios finales de los alumnos?"
            )
            
            if respuesta:
                servicio_clase.cerrar_clase_y_evaluar(id_clase)
                messagebox.showinfo("Éxito", "La clase ha sido cerrada y los alumnos regulares fueron evaluados.")
        self.lista_presencias(id_clase,ventana_anterior)
        ventana.destroy()
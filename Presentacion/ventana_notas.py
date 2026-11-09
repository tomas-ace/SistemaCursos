from Servicios.notas_service import *
from tkinter import *
from tkinter import messagebox
from Presentacion.elementos import *
from Servicios.clase_service import *
from Dominio.nota import *

class Ventana_Notas():
    def __init__(self,contenido):
          self._contenido=contenido
    def lista_notas(self,id_clase,contenedor=None):
                if contenedor is None:
                    ventana_notas = Toplevel(self._contenido)
                    ventana_notas.title(f"Notas - Clase {id_clase}")
                    ventana_notas.geometry("680x450")
                    ventana_notas.configure(bg="white")
                else:
                    ventana_notas = contenedor
                    for elemento in ventana_notas.winfo_children():
                        elemento.destroy()
                Label(
                    ventana_notas, 
                    text="Registro de Notas", 
                    font=("Arial", 16, "bold"), 
                    bg="white"
                ).pack(pady=15)
            
                servicio_notas = Nota_Service()
                datos_notas = servicio_notas.notas_por_alumno(id_clase)
                encabezados = ["Id","Nombre","Apellido","Descripción", "Nota", "Fecha"]
                frame_tabla = Frame(ventana_notas)
                frame_tabla.pack(fill="both", expand=True, padx=20, pady=10)
                
         
                tree = treeview(frame_tabla, encabezados, datos_notas)
                tree["displaycolumns"] = ("Nombre", "Apellido", "Descripción", "Nota", "Fecha")
                Button(
                                frame_tabla, 
                                text="Agregar Notas", 
                                font=("Arial", 10, "bold"), 
                                bg=azul, 
                                fg="white", 
                                bd=0, 
                                padx=15, 
                                pady=5,
                                command=lambda: self.ventana_agregar_notas(id_clase,ventana_notas)
                            ).grid(row=1, column=0, padx=10)
                frame_edicion = Frame(ventana_notas, bg="white")
                frame_edicion.pack(pady=10,anchor="w")
                Label(frame_edicion, text="Editar nota (seleccione nota para editar):", font=("Arial", 11, "bold"), bg="white").grid(row=0, column=0, padx=5,pady=10)
                Label(frame_edicion, text="Nueva Nota:", font=("Arial", 11, "bold"), bg="white").grid(row=1, column=0, padx=5)
    
                entry_nota = Entry(frame_edicion, font=("Arial", 11), width=8)
                entry_nota.grid(row=1, column=1, padx=5)
    
                Button(
                    frame_edicion, 
                    text="Guardar Cambio", 
                    font=("Arial", 10, "bold"), 
                    bg=azul, 
                    fg="white", 
                    bd=0, 
                    padx=15, 
                    pady=5,
                    command=lambda: self.guardar_edicion_nota(tree, entry_nota, id_clase, ventana_notas)
                ).grid(row=1, column=2, padx=10)
                
    def guardar_edicion_nota(self, tree, entry, id_clase, ventana):
                servicio_classe=Clase_Service()
                if servicio_classe.esta_inactiva(id_clase):
                    messagebox.showerror("Error","No puedes modificar notas en una clase inactiva")
                    return
                seleccion = tree.selection()
                
                if not seleccion:
                    messagebox.showwarning("Atención", "Seleccione una nota de la tabla para editar.", parent=ventana)
                    return
                    
                nueva_nota_texto = entry.get()
                item_id = seleccion[0]
                datos_fila = tree.item(item_id)['values']
                id_nota = datos_fila[0] 
                servicio_notas = Nota_Service()
                resultado=servicio_notas.editar_nota(id_nota, nueva_nota_texto) 
                
                if resultado==True:
                    messagebox.showinfo("Exito", "Nota modificada correctamente",parent=ventana)
                else:
                    messagebox.showerror("Error", resultado,parent=ventana)
            
                self.lista_notas(id_clase, contenedor=ventana) 
                    
    def ventana_agregar_notas(self, id_clase,ventana_notas):
                
            servicio_classe=Clase_Service()
            if servicio_classe.esta_inactiva(id_clase):
                messagebox.showerror("Error","No puedes agregar notas en una clase inactiva")
                return
                
            alumnos=servicio_classe.lista_de_alumnos_por_clase(id_clase)
            ventana = Toplevel(self._contenido)
            ventana.title("Agregar Notas")
            ventana.geometry("700x600")
            ventana.configure(bg=blanco)

            frame_fecha = Frame(ventana, bg=blanco)
            frame_fecha.pack(pady=20)
            
            Label(frame_fecha, text="Día:", bg=blanco).grid(row=0, column=0)
            entry_dia = Entry(frame_fecha, width=5)
            entry_dia.grid(row=0, column=1, padx=10)

            Label(frame_fecha, text="Mes:", bg=blanco).grid(row=0, column=2)
            entry_mes = Entry(frame_fecha, width=10)
            entry_mes.grid(row=0, column=3, padx=10)
            
            Label(frame_fecha, text="Año:", bg=blanco).grid(row=0, column=4)
            entry_anio = Entry(frame_fecha, width=8)
            entry_anio.grid(row=0, column=5, padx=10)
            
            Label(frame_fecha, text="Descripcion:", bg=blanco).grid(row=1, column=0)
            entry_descripcion = Entry(frame_fecha, width=12)
            entry_descripcion.grid(row=1, column=1, padx=10, columnspan=4)

            lista_notas = [] 

            frame_alumnos = Frame(ventana, bg=blanco)
            frame_alumnos.pack(pady=10)

            fila = 0
            for alumno in alumnos:
                nombre = f"{alumno[1]} {alumno[2]}"
                id_inscripcion=alumno[3]
                nota = StringVar(value="1") 
                
                lista_notas.append([id_inscripcion, nota])

                Label(
                    frame_alumnos, text=nombre,bd=1, width=25,padx=10, pady=5
                ).grid(row=fila, column=0, pady=5, padx=20)

                Entry(frame_alumnos, textvariable=nota).grid(row=fila, column=1)
                
                fila += 1 

            Button(
                ventana, text="Guardar Nota", bg=azul, fg=blanco, font=("Arial", 12, "bold"),
                command=lambda: self.guardar_notas(id_clase,entry_descripcion.get(),entry_dia.get(), entry_mes.get(), entry_anio.get(), ventana,lista_notas,ventana_notas)
            ).pack(pady=20)
            
            
            
    def guardar_notas(self,id_clase,descripcion, dia, mes, anio, ventana,lista,ventana_notas):                
        fecha_completa = f"{anio}-{mes}-{dia}"
        nota_detalle_service= Nota_Service()
        todas_validas=True
        for alumno in lista:
            
            id_inscripcion=alumno[0]
            nota = alumno[1].get() 
            nota_detalle=Nota(None,fecha_completa,nota,descripcion,id_inscripcion)
            validacion=nota_detalle_service.datos_validos(nota_detalle)
            if validacion != True:
                messagebox.showerror("Error", validacion,parent=ventana)
                todas_validas=False
                break
        if todas_validas:
            for alumno in lista:
                id_inscripcion=alumno[0]
                nota = alumno[1].get() 
                nota_detalle=Nota(None,fecha_completa,nota,descripcion,id_inscripcion)
                nota_detalle_service.registrar_nota(nota_detalle)
            messagebox.showinfo("Exito", "Notas registradas correctamente.",parent=ventana)
            ventana.destroy()
            self.lista_notas(id_clase,contenedor=ventana_notas)
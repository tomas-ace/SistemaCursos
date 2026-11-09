from datetime import datetime
from tkinter import *
from Presentacion.elementos import *
from Dominio.inscripcion import *
from Servicios.inscripcion_service import *
from Presentacion.ventana_clases import *
from Servicios.alumno_service import *
from tkinter import messagebox

class Ventana_Inscripciones():
        def __init__(self,contenido):
                    self._contenido = contenido
                    self._botones = Frame(contenido, bg=blanco)

        def ventana_registro_inscripcion(self,ventana_none):
            if ventana_none == None:
                pass
            else:
                ventana_none.destroy()
            ventana = Toplevel(self._contenido)
    
            ventana.title("Registrar nueva inscripcion")
            ventana.geometry("400x400")
            ventana.configure(bg=blanco)
            Label(
                ventana,
                text="Registrar nueva inscripcion",
                font=("Arial", 20, "bold"),
                bg=blanco,
                fg=texto
            ).grid(pady=(10, 25), column=0, row=0)

            #datoss

            frame_contenido=Frame(ventana, bg=blanco)
            frame_contenido.grid(column=0, row=1, padx=20, pady=10,rowspan=4,columnspan=4)
            self.mostrar_listas(frame_contenido,ventana)
    
        def mostrar_listas(self,contenedor,ventana):
            for elemento in contenedor.winfo_children():
                elemento.destroy()
            service_alumnos=Alumno_Service()
            lista_de_alumnos=service_alumnos.lista_por_nombre_apellido()
            print("lsita de alumnos",lista_de_alumnos)
            encabezados_alumnos = ["ID","Nombre", "Apellido"]
            tree_alumnos=treeview(contenedor, encabezados_alumnos, lista_de_alumnos)
            
            tree_alumnos["displaycolumns"] = ("Nombre", "Apellido")
            
            frame_botones=Frame(contenedor,bg=blanco)
            frame_botones.grid(column=0,row=16,columnspan=2)
            Button(
                    frame_botones,
                    text="Siguiente",
                    font=("Arial", 12),
                    bg=azul,
                    fg=blanco,
                    bd=0,
                    padx=30,
                    pady=12,
                    command=lambda: self.guardar_y_avanzar(tree_alumnos,contenedor,ventana)
                ).grid(padx=(0, 10), column=0, row=0)
            Button(
                    frame_botones,
                    text="Cancelar",
                    font=("Arial", 12),
                    bg=azul,
                    fg=blanco,
                    bd=0,
                    padx=30,
                    pady=12,
                    command=lambda: ventana.destroy()
                ).grid(padx=(0, 10), column=1, row=0)

        def guardar_y_avanzar(self,tree_alumnos,contenedor,ventana):
            seleccion = tree_alumnos.selection()
            if not seleccion:
                messagebox.showwarning("Atencion", "Por favor, seleccione un alumno de la lista.", parent=contenedor)
                return
            item_id = seleccion[0]
            alumno_seleccionado_para_inscribir = tree_alumnos.item(item_id)['values']
           
            self.mostrar_cursos(contenedor, alumno_seleccionado_para_inscribir[0], ventana)
        def mostrar_cursos(self,contenedor,alumno,ventana):
            for elemento in contenedor.winfo_children():
                elemento.destroy()
            service_cursos=Clase_Service()
            lista_de_cursos=service_cursos.listar_por_descripcion()
            encabezados_cursos = ["ID","Descripcion", "Turno"]
            tree_cursos=treeview(contenedor, encabezados_cursos, lista_de_cursos)
            tree_cursos["displaycolumns"] = ("Descripcion", "Turno")
            frame_botones=Frame(contenedor,bg=blanco)
            frame_botones.grid(column=0,row=16,columnspan=2)
            Button(
                    frame_botones,
                    text="Finalizar Inscripcion",
                    font=("Arial", 12),
                    bg=azul,
                    fg=blanco,
                    bd=0,
                    padx=30,
                    pady=12,
                    command=lambda: self.guardar_inscripcion(tree_cursos,alumno,contenedor,ventana)
                ).grid(padx=(0, 10), column=0, row=0)
            Button(
                    frame_botones,
                    text="Cancelar",
                    font=("Arial", 12),
                    bg=azul,
                    fg=blanco,
                    bd=0,
                    padx=30,
                    pady=12,
                    command=lambda: ventana.destroy()
                ).grid(padx=(0, 10), column=1, row=0)
        
        def guardar_inscripcion(self,tree_cursos,alumno,contenedor,ventana):
            seleccion = tree_cursos.selection()
            if not seleccion:
                messagebox.showwarning("Atencion", "Por favor, seleccione un curso de la lista.",parent=contenedor)
                return
            item_id = seleccion[0]
            curso_seleccionado_para_inscribir = tree_cursos.item(item_id)['values']
            fecha_actual = datetime.now().strftime("%Y-%m-%d")
            
          
            nueva_inscripcion=Inscripcion(None, fecha_actual, "En Curso", alumno, curso_seleccionado_para_inscribir[0])
            servicio_inscripcion=Inscripcion_Service()
            resultado=servicio_inscripcion.nueva_inscripcion(nueva_inscripcion)
            if resultado != True:
                messagebox.showerror("Error", resultado,parent=contenedor)
            else:
                messagebox.showinfo("Exito", "Inscripción realizada con éxito.",parent=contenedor)
                ventana.destroy()
                     
        
from tkinter import *
from Presentacion.elementos import *
from Dominio.inscripcion import *
from Servicios.inscripcion_service import *
from Presentacion.ventana_clases import *
from Servicios.alumno_service import *

class Ventana_Inscripciones():
        def __init__(self,contenido):
                    self._contenido = contenido
                    self._botones = Frame(contenido, bg=blanco)
        def mostrar_opcion_elegida(self,opcion):
            if opcion == "Inscribir alumno":
                self.ventana_registro_inscripcion(None)
            else:
                self.lista_inscripciones()

                    
                    
        def lista_inscripciones(self):
            ventana_lista = Toplevel(self._contenido)
            ventana_lista.title("Lista de inscripciones")
            ventana_lista.geometry("1200x600")
            ventana_lista.configure(bg=blanco)
            Label(
                ventana_lista,
                text="Lista de inscripciones",
                font=("Arial", 20, "bold"),
                bg=blanco,
                fg=texto
            ).grid(pady=(10, 25), column=0, row=0)
            columnas = ["IdInscripcion", "Fecha", "Estado", "Nombre", "Apellido", "Curso", "Anio", "Turno"]
            datos_inscripcion = Inscripcion_Service().listar_inscripciones()
            tree=treeview(ventana_lista, columnas, datos_inscripcion)
            frame_acciones = Frame(ventana_lista, bg=blanco)
            frame_acciones.grid(column=0, row=2, padx=20, pady=10)
    
            Button(
                frame_acciones,
                text="Agregar Nuevo",
                font=("Arial", 11, "bold"),
                bg=azul,
                fg=blanco,
                bd=0,
                padx=20,
                pady=10,
                command=lambda: self.ventana_registro_inscripcion(ventana_lista)
            ).pack(side="left", padx=10)
    
            Button(
                frame_acciones,
                text="Modificar Seleccionado",
                font=("Arial", 11, "bold"),
                bg=gris,
                fg=blanco,
                bd=0,
                padx=20,
                pady=10,
                command=lambda: self.preparar_modificacion(tree,ventana_lista)
            ).pack(side="left", padx=10)
        def preparar_modificacion(self,tree,ventana_lista):
            seleccion = tree.selection()
            if not seleccion:
                return
    
            item_id = seleccion[0]
            datos_inscripcion = tree.item(item_id)['values']
            ventana_lista.destroy()  
            self.ventana_modificar_inscripcion(datos_inscripcion)
                    
        def ventana_modificar_inscripcion(self,datos_inscripcion):
                ventana = Toplevel(self._contenido)
                ventana.title("Modificar Estado")
                ventana.geometry("600x600")
                ventana.configure(bg=blanco)
                id_inscripcion = datos_inscripcion[0]
                print(datos_inscripcion)
                estado_actual = datos_inscripcion[2]
                Label(
                    ventana,
                    text="Modificar Estado",
                    font=("Arial", 20, "bold"),
                    bg=blanco,
                    fg=texto
                ).grid(pady=(10, 25), column=0, row=0)
        
        
                #campos 
                Label(ventana, text="Estado", font=("Arial", 12, "bold"), bg=blanco, fg=texto).grid(column=0, row=1)
                
                estado=StringVar(value=estado_actual)
                estado.set(estado_actual)
                Radiobutton(ventana, text="Aprobado", variable=estado, value="Aprobado", font=("Arial", 12), bg=blanco, fg=texto).grid(column=0, row=2)
                Radiobutton(ventana, text="Desaprobado", variable=estado, value="Desaprobado", font=("Arial", 12), bg=blanco, fg=texto).grid(column=0, row=3)
                Radiobutton(ventana, text="Libre", variable=estado, value="Libre", font=("Arial", 12), bg=blanco, fg=texto).grid(column=0, row=4)
                Radiobutton(ventana, text="En Curso", variable=estado, value="En Curso", font=("Arial", 12), bg=blanco, fg=texto).grid(column=0, row=5)
                Radiobutton(ventana, text="Baja", variable=estado, value="Baja", font=("Arial", 12), bg=blanco, fg=texto).grid(column=0, row=6)
                
                
                Button(
                    ventana,
                    text="Guardar Cambios",
                    font=("Arial", 12),
                    bg=azul,
                    fg=blanco,
                    bd=0,
                    padx=20,
                    pady=12,
                    command=lambda: self.guardar_modificacion(id_inscripcion,estado.get(),ventana)
                ).grid(padx=(0, 10), column=0, row=7)
        
                Button(
                    ventana,
                    text="Cancelar",
                    font=("Arial", 12),
                    bg=gris,
                    fg=blanco,
                    bd=0,
                    padx=20,
                    pady=12,
                    command=ventana.destroy
                ).grid(padx=(0, 10), column=1, row=7)
        def guardar_modificacion(self, id_inscripcion, estado, ventana):
            servicio_inscripcion = Inscripcion_Service()
            servicio_inscripcion.modificar_estado_de_inscripcion(id_inscripcion, estado)
            ventana.destroy()  
        
        def ventana_registro_inscripcion(self,ventana_none):
            from Presentacion.ventana_clases import Ventana_Clases
            if ventana_none == None:
                pass
            else:
                ventana_none.destroy()
            ventana = Toplevel(self._contenido)
    
            ventana.title("Registrar nueva inscripcion")
            ventana.geometry("600x600")
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

            alumno=self.seleccion_alumno(frame_contenido)

            curso=self.seleccion_curso(frame_contenido)
        
    #botones
    
            # Button(
            #     ventana,
            #     text="Registrar",
            #     font=("Arial", 12),
            #     bg=azul,
            #     fg=blanco,
            #     bd=0,
            #     padx=30,
            #     pady=12,
            #     command=lambda: self.registrar(f"{anio.get()}-{mes.get()}-{dia.get()}", tree_clases, tree_alumnos, ventana)
            # ).grid(padx=(0, 10), column=0, row=16)
                
    
            # Button(
            #     ventana,
            #     text="Cancelar",
            #     font=("Arial", 12),
            #     bg=gris,
            #     fg=blanco,
            #     bd=0,
            #     padx=30,
            #     pady=12,
            #     command=lambda: self.cancelar(ventana)
            # ).grid(padx=(0, 10), column=1, row=16)
        def seleccion_alumno(self,contenedor):
            service_alumnos=Alumno_Service()
            lista_de_alumnos=service_alumnos.lista_por_nombre_apellido()
            encabezados_alumnos = ["Nombre", "Apellido"]
            tree_alumnos=treeview(contenedor, encabezados_alumnos, lista_de_alumnos)
            Button(
                    contenedor,
                    text="Seleccionar Alumno",
                    font=("Arial", 12),
                    bg=azul,
                    fg=blanco,
                    bd=0,
                    padx=30,
                    pady=12,
                    command=lambda: self.alumno_seleccionado(tree_alumnos)
                ).grid(padx=(0, 10), column=0, row=16)
            return self.alumno_seleccionado(tree_alumnos)

        def alumno_seleccionado(self,tree_alumnos):
            seleccion = tree_alumnos.selection()
            if not seleccion:
                return

            item_id = seleccion[0]
            datos_alumno = tree_alumnos.item(item_id)['values']
            return datos_alumno
        def seleccion_curso(self,contenedor):
            service_cursos=Clase_Service()
            lista_de_cursos=service_cursos.lista_por_nombre_apellido()
            encabezados_cursos = ["Descripcion", "Turno"]
            tree_cursos=treeview(contenedor, encabezados_cursos, lista_de_cursos)
        def registrar(self, fecha, clase, alumno, ventana):
            clase_seleccion = clase.selection()
            if not clase_seleccion:
                return

            clase_item_id = clase_seleccion[0]
            datos_clase = clase.item(clase_item_id)['values']
            id_clase = datos_clase[0]
            print(id_clase)
            
            alumno_seleccion = alumno.selection()
            if not alumno_seleccion:
                return

            alumno_item_id = alumno_seleccion[0]
            datos_alumno = alumno.item(alumno_item_id)['values']
            id_alumno = datos_alumno[0]
            print(id_alumno)

            nueva_inscripcion=Inscripcion(None, fecha, "En Curso", id_alumno, id_clase)
            servicio_inscripcion=Inscripcion_Service()
            servicio_inscripcion.nueva_inscripcion(nueva_inscripcion)
            ventana.destroy()         
        def mostrar(self):
            print("hola")
            Label(
                self._contenido,
                text="Inscripcion",
                font=("Arial", 16, "bold"),
                bg=blanco,
                fg=texto
            ).grid(column=0, row=0, padx=20, pady=10)
    
            Label(
                self._contenido,
                text="Seleccione la opcion que desee.",
                font=("Arial", 11),
                bg=blanco,
                fg=gris
            ).grid(column=0, row=1, padx=20, pady=10)
    
            
            self._botones.grid(column=0, row=2, padx=20, pady=10)#coloca el contenedor y le dice que se ezpanda
            opciones = [
                "Inscribir alumno",
                "Consultar inscripciones"
            ]
            fila = 0
            for opcion in opciones:
                    crear_boton(opcion,fila,self._botones,lambda opcion_actual=opcion: self.mostrar_opcion_elegida(opcion_actual))
                    fila += 1

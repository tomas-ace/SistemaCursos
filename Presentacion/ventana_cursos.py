from tkinter import *
from Presentacion.elementos import *
from Servicios.curso_service import *
from Dominio.curso import *
# Colores
azul = "#2864e8"
azul_oscuro = "#093068"
blanco = "#ffffff"
gris = "#6b7280"
texto = "#111827"
borde = "#d1d5db"

class Ventana_Cursos():
        def __init__(self,contenido):
                    self._contenido = contenido
                    self._botones = Frame(contenido, bg=blanco)
        def mostrar_opcion_elegida(self,opcion):
            from Presentacion.ventana_clases import Ventana_Clases
            if opcion == "Registrar nuevo curso":
                self.ventana_registro_curso(None)
            elif opcion == "Clases":
                for elemento in self._contenido.winfo_children():
                        elemento.destroy()
                print("clases")
                clase_ventana=Ventana_Clases(self._contenido)
                clase_ventana.mostrar()
            else:
                self.lista_de_cursos()
        def ventana_registro_curso(self,ventana_none):
                if ventana_none == None:
                    pass
                else:
                    ventana_none.destroy()
                ventana = Toplevel(self._contenido)
        
                ventana.title("Registrar curso")
                ventana.geometry("600x600")
                ventana.configure(bg=blanco)
                Label(
                    ventana,
                    text="Registrar nuevo curso",
                    font=("Arial", 20, "bold"),
                    bg=blanco,
                    fg=texto
                ).grid(pady=(10, 25), column=0, row=0)
        
        
                #datoss
                
                descripcion = StringVar()
                duracion = IntVar()
                
                
                Label(
                        ventana,
                        text="Nombre",
                        font=("Arial", 12, "bold"),
                        bg=blanco,
                        fg=texto
                    ).grid(column=0, row=1)
                self._descripcion = Entry(
                    ventana,
                    font=("Arial", 12),
                    textvariable=descripcion
                )
                self._descripcion.grid(pady=(5, 15), column=1, row=1,columnspan=2)
        
                Label(
                    ventana,
                    text="Duración (Clases)",
                    font=("Arial", 12, "bold"),
                    bg=blanco,
                    fg=texto
                ).grid(column=0, row=2)
        
                self._duracion = Entry(
                    ventana,
                    font=("Arial", 12),
                    textvariable=duracion
                )
                self._duracion.grid(pady=(5, 15), column=1, row=2,columnspan=2)
                            
                #botones
        
                Button(
                    ventana,
                    text="Registrar",
                    font=("Arial", 12),
                    bg=azul,
                    fg=blanco,
                    bd=0,
                    padx=30,
                    pady=12,
                    command=lambda: self.registrar(descripcion.get(), duracion.get(), ventana)
                ).grid(padx=(0, 10), column=0, row=9)
                   
        
                Button(
                    ventana,
                    text="Cancelar",
                    font=("Arial", 12),
                    bg=gris,
                    fg=blanco,
                    bd=0,
                    padx=30,
                    pady=12,
                    command=lambda: self.cancelar(ventana)
                ).grid(padx=(0, 10), column=1, row=9)
        
        def registrar(self,descripcion,duracion,ventana):
                nuevo_curso=Curso(None,descripcion,duracion)
                servicio_curso=Curso_Service()
                servicio_curso.nuevo_curso(nuevo_curso)
                ventana.destroy()
        def cancelar(self,ventana):
            ventana.destroy()
        
                    
        def mostrar(self):
            print("hola")
            Label(
                self._contenido,
                text="Cursos",
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
    
            
            self._botones.grid(column=0, row=2, padx=20, pady=10)
            opciones = [
                "Registrar nuevo curso",
                "Consultar cursos",
                "Clases" 
            ]
            fila = 0
            for opcion in opciones:
                crear_boton(opcion,fila,self._botones,lambda: self.mostrar_opcion_elegida(opcion))
                fila += 1

        def lista_de_cursos(self,contenedor=None):
                if contenedor == None:
                    ventana_lista = Toplevel(self._contenido)
                    ventana_lista.title("Lista de cursos")
                    ventana_lista.geometry("600x600")
                    ventana_lista.configure(bg=blanco)
                    Label(
                        ventana_lista,
                        text="Lista de cursos",
                        font=("Arial", 20, "bold"),
                        bg=blanco,
                        fg=texto
                    ).grid(pady=(10, 25), column=0, row=0)
                else:
                    ventana_lista = contenedor
                columnas = ["IDCurso", "Descripcion", "Duracion"]
                datos_cursos = Curso_Service().listar_cursos()
                tree=treeview(ventana_lista, columnas, datos_cursos)
                frame_acciones = Frame(ventana_lista, bg=blanco)
                frame_acciones.grid(column=0, row=2, padx=20, pady=10)

                if contenedor == None:
                    Button(
                            frame_acciones,
                            text="Agregar Nuevo",
                            font=("Arial", 11, "bold"),
                            bg=azul,
                            fg=blanco,
                            bd=0,
                            padx=20,
                            pady=10,
                            command=lambda: self.ventana_registro_curso(ventana_lista)
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
                
                return tree
        def preparar_modificacion(self,tree,ventana):
                seleccion = tree.selection()
                if not seleccion:
                    return
        
                item_id = seleccion[0]
                datos_curso = tree.item(item_id)['values']
                ventana.destroy()  
                self.ventana_modificar_curso(datos_curso)
                
        def ventana_modificar_curso(self,datos_curso):
                ventana = Toplevel(self._contenido)
                ventana.title("Modificar curso")
                ventana.geometry("600x600")
                ventana.configure(bg=blanco)
        
                Label(
                    ventana,
                    text="Modificar curso",
                    font=("Arial", 20, "bold"),
                    bg=blanco,
                    fg=texto
                ).grid(pady=(10, 25), column=0, row=0)
        
                #cargo las variabkes con los datos
                id_curso = datos_curso[0]
                descripcion = StringVar(value=datos_curso[1])
                duracion = IntVar(value=datos_curso[2])
                
        
                #campos 
                Label(ventana, text="Descripcion", font=("Arial", 12, "bold"), bg=blanco, fg=texto).grid(column=0, row=1)
                Entry(ventana, font=("Arial", 12), textvariable=descripcion).grid(pady=(5, 15), column=1, row=1, columnspan=2)
        
                Label(ventana, text="Duracion (Clases)", font=("Arial", 12, "bold"), bg=blanco, fg=texto).grid(column=0, row=2)
                Entry(ventana, font=("Arial", 12), textvariable=duracion).grid(pady=(5, 15), column=1, row=2, columnspan=2)
        
        
        
                # Botón para guardar cambios
                Button(
                    ventana,
                    text="Guardar Cambios",
                    font=("Arial", 12),
                    bg=azul,
                    fg=blanco,
                    bd=0,
                    padx=20,
                    pady=12,
                    command=lambda: self.guardar_modificacion(id_curso, descripcion.get(), duracion.get(),ventana)
                ).grid(padx=(0, 10), column=0, row=9)
        
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
                ).grid(padx=(0, 10), column=1, row=9)
        def guardar_modificacion(self, id_curso, descripcion, duracion, ventana):
                curso_actualizado = Curso(id_curso, descripcion, duracion)
                servicio_curso = Curso_Service()
                servicio_curso.modificar_curso(curso_actualizado)
                print(f"Curso {id_curso} modificado con éxito")
                ventana.destroy()
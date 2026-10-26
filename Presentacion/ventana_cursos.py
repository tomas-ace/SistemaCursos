from tkinter import *
from Presentacion.treeview import treeview
from Presentacion.ventana_clases import *
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
            if opcion == "Registrar nuevo curso":
                self.ventana_registro_curso()
            elif opcion == "Clases":
                print("clases")
                clase_ventana=Ventana_Clases(self._contenido)
                clase_ventana.mostrar()
            else:
                self.lista_de_cursos()
        def ventana_registro_curso(self):
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
                    command=lambda: self.registrar(descripcion.get(), duracion.get())
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
                    command=self.cancelar
                ).grid(padx=(0, 10), column=1, row=9)
        
        def registrar(self,descripcion,duracion):
                nuevo_curso=Curso(None,descripcion,duracion)
                servicio_curso=Curso_Service()
                servicio_curso.nuevo_curso(nuevo_curso)
        def cancelar(self):
            pass
        def crear_boton(self,nombre,fila):
                Button(
                        self._botones,
                        text=nombre,
                        command=lambda: self.mostrar_opcion_elegida(nombre),
                        font=("Arial", 20),
                        bg=azul,
                        fg=blanco,
                        bd=0,
                        padx=40,
                        pady=15,
                    ).grid(column=2, row=fila, padx=10, pady=10)
                    
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
                self.crear_boton(opcion,fila)
                fila += 1

        def lista_de_cursos(self):
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
                columnas = ["IDCurso", "Descripcion", "Duracion"]
                datos_cursos = Curso_Service().listar_cursos()
                tree=treeview(ventana_lista, columnas, datos_cursos)
                a=input("pausa para que me deje seleccionar")
                seleccion = tree.selection()#agarra el identificadopr
                item_id = seleccion[0]  #lo guarda en una variable
                datos_fila = tree.item(item_id)['values'] #extrae los valores de la fila
            
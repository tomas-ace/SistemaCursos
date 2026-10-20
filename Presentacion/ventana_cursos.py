from tkinter import *
from Presentacion.ventana_clases import *
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
                print("registrar")
            elif opcion == "Clases":
                print("clases")
                clase_ventana=Ventana_Clases(self._contenido)
                clase_ventana.mostrar()
            else:
                print("consultar")
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

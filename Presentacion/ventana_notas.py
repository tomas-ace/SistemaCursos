# from tkinter import *

# # Colores
# azul = "#2864e8"
# azul_oscuro = "#093068"
# blanco = "#ffffff"
# gris = "#6b7280"
# texto = "#111827"
# borde = "#d1d5db"

# class Ventana_Notas():
#     def __init__(self,contenido):
#                 self._contenido = contenido
#                 self._botones = Frame(contenido, bg=blanco)
#     def mostrar_opcion_elegida(self,opcion):
#         if opcion == "Registrar nuevo alumno":
#             print("registrar")
#         else:
#             print("consultar")
#     def crear_boton(self,nombre):
#             Button(
#                     self._botones,
#                     text=nombre,
#                     command=lambda: self.mostrar_opcion_elegida(nombre),
#                     font=("Arial", 20),
#                     bg=azul,
#                     fg=blanco,
#                     bd=0,
#                     padx=40,
#                     pady=15,
#                 ).pack(pady=5)
                
#     def mostrar(self):
#         print("hola")
#         Label(
#             self._contenido,
#             text="Alumnos",
#             font=("Arial", 16, "bold"),
#             bg=blanco,
#             fg=texto
#         ).pack(anchor="w", pady=(8, 4))

#         Label(
#             self._contenido,
#             text="Seleccione la opcion que desee.",
#             font=("Arial", 11),
#             bg=blanco,
#             fg=gris
#         ).pack(anchor="w", pady=(0, 18))

        
#         self._botones.pack(fill="both", expand=True)#coloca el contenedor y le dice que se ezpanda
#         opciones = [
#             "Registrar nuevo alumno",
#             "Consultar alumnos"
#         ]
#         for opcion in opciones:
#             self.crear_boton(opcion)

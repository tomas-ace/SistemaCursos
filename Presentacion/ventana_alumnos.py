from tkinter import *

# Colores
azul = "#2864e8"
azul_oscuro = "#093068"
blanco = "#ffffff"
gris = "#6b7280"
texto = "#111827"
borde = "#d1d5db"

class Ventana_Alumnos():
    def __init__(self):
        pass
        
    def mostrar(self,contenido):
        """Dibuja la pantalla de inicio dentro del contenedor recibido."""

        Label(
            contenido,
            text="¡Estamos en estudiantes!",
            font=("Arial", 16, "bold"),
            bg=blanco,
            fg=texto
        ).pack(anchor="w", pady=(8, 4))

        Label(
            contenido,
            text="Seleccioná una opción del menú para comenzar.",
            font=("Arial", 11),
            bg=blanco,
            fg=gris
        ).pack(anchor="w", pady=(0, 18))

        Label(
            contenido,
            text="Resumen del sistema",
            font=("Arial", 13, "bold"),
            bg=blanco,
            fg=texto
        ).pack(anchor="w", pady=(0, 10))

        tarjetas = Frame(contenido, bg=blanco)
        tarjetas.pack(fill="both", expand=True)

        def crear_tarjeta(columna, fila, nombre, numero):
            tarjeta = Frame(
                tarjetas,
                bg=blanco,
                highlightbackground=borde,
                highlightthickness=1
            )
            tarjeta.grid(
                row=fila,
                column=columna,
                sticky="nsew",
                padx=5,
                pady=5
            )

            Label(
                tarjeta,
                text=nombre,
                font=("Arial", 11),
                bg=blanco,
                fg=texto
            ).pack(anchor="w", padx=14, pady=(14, 5))

            Label(
                tarjeta,
                text=numero,
                font=("Arial", 21, "bold"),
                bg=blanco,
                fg=azul
            ).pack(anchor="w", padx=14, pady=(0, 12))

        tarjetas.grid_columnconfigure(0, weight=1)
        tarjetas.grid_columnconfigure(1, weight=1)
        tarjetas.grid_rowconfigure(0, weight=1)
        tarjetas.grid_rowconfigure(1, weight=1)

        crear_tarjeta(0, 0, "Estudiantes", "0")
        crear_tarjeta(1, 0, "Cursos", "0")
        crear_tarjeta(0, 1, "Inscripciones", "0")
        crear_tarjeta(1, 1, "Calificaciones", "0")

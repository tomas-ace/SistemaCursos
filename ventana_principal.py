from tkinter import *

from Presentacion.ventana_bienvenida import *
from Presentacion.ventana_alumnos import *
from Presentacion.ventana_cursos import *
from Presentacion.ventana_inscripciones import *



#colores
azul = "#2864e8"
azul_oscuro = "#093068"
blanco = "#ffffff"
gris = "#6b7280"
texto = "#111827"

#ventana
raiz = Tk()
raiz.title("Sistema de Gestión Educativa")
raiz.geometry("900x520")
raiz.minsize(760, 460)
raiz.config(bg=blanco)

#encabezado
encabezado = Frame(raiz, bg=blanco)
encabezado.pack(fill="x", padx=22, pady=(18, 8))

Label(
    encabezado,
    text="Sistema de Gestión de Cursos",
    font=("Arial", 18, "bold"),
    bg=blanco,
    fg=azul_oscuro
).pack(anchor="w")

#contenedor de botones
menu = Frame(raiz, bg=blanco)
menu.pack(fill="x", padx=22, pady=(0, 18))

#contenedor que contiene lo que va a mostrar cada ventana
contenido = Frame(raiz, bg=blanco)
contenido.pack(fill="both", expand=True, padx=28, pady=(0, 22))


def limpiar_contenido():
    for elemento in contenido.winfo_children():
        elemento.destroy()


def mostrar_seccion(seccion):
    limpiar_contenido()
    if seccion == "Inicio":
        bienvenida=Bienvenida(contenido)
        bienvenida.mostrar()
    elif seccion == "Alumnos":
        alumnos=Ventana_Alumnos(contenido)
        alumnos.mostrar()
    elif seccion == "Cursos":
        cursos=Ventana_Cursos(contenido)
        cursos.mostrar()
    elif seccion == "Inscripciones":
        inscripciones=Ventana_Inscripciones(contenido)
        inscripciones.mostrar()
    


def crear_boton(nombre):
    Button(
        menu,
        text=nombre,
        command=lambda: mostrar_seccion(nombre),
        font=("Arial", 10),
        bg=azul,
        fg=blanco,
        bd=0,
        padx=20,
        pady=10,
    ).pack(side="left", padx=(0, 5))


opciones = [
    "Inicio",
    "Alumnos",
    "Cursos",
    "Inscripciones"
]

for opcion in opciones:
    crear_boton(opcion)

mostrar_seccion("Inicio")
raiz.mainloop()

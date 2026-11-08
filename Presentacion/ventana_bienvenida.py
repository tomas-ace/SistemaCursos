from tkinter import *
from Servicios.alumno_service import *
from Servicios.inscripcion_service import *
from Servicios.curso_service import *
from Servicios.clase_service import *
from Presentacion.elementos import *

class Bienvenida():
    def __init__(self,contenido):
        self._contenido = contenido
        self._tarjetas = Frame(contenido, bg=blanco)
    def crear_tarjeta(self,columna, fila, nombre, numero):
            tarjeta = Frame(
                    self._tarjetas,
                    bg="white",
                    highlightbackground=azul, #color borde de la tarjeta
                    highlightthickness=2, #grosor borde de tarjetas
                    padx=15, 
                    pady=20
                )
            tarjeta.grid(
                    row=fila,
                    column=columna,
                    sticky="nsew", #se expande en todas las direcciones
                    padx=10,
                    pady=10
                )
            self._tarjetas.grid_columnconfigure(columna, weight=1, uniform="grupo_tarjetas")
            self._tarjetas.grid_rowconfigure(fila, weight=1, uniform="grupo_filas")
            Label(
                    tarjeta,
                    text=nombre,
                    font=("Arial", 11,"bold"),
                    bg="white",
                ).pack(anchor="center", pady=(0, 10))
    
            Label(
                    tarjeta,
                    text=numero,
                    font=("Arial", 26, "bold"),
                    bg="white",
                    fg=azul
                ).pack(anchor="center")
                
    def mostrar(self):

        Label(
            self._contenido,
            text="¡Bienvenido al sistema!",
            font=("Arial", 16, "bold"),
            bg=blanco
        ).grid(column=0,row=0, pady=(8, 4))

        Label(
            self._contenido,
            text="Seleccioná una opción del menú para comenzar.",
            font=("Arial", 11),
            bg=blanco,
            fg=gris
        ).grid(column=0,row=1, pady=(0, 18)) #(arriba,abajo)

        Label(
            self._contenido,
            text="Resumen del sistema",
            font=("Arial", 13, "bold"),
            bg=blanco
        ).grid(column=0,row=2,pady=(0, 10))

        
        self._tarjetas.grid(column=0,row=3,columnspan=3)#coloca el contenedor y le dice cuantas columnas se expande

        
        
        service_alumno=Alumno_Service()
        service_curso=Curso_Service()
        service_clase=Clase_Service()
        service_inscripcion=Inscripcion_Service()
        
        self.crear_tarjeta(0, 0, "Estudiantes", service_alumno.cantidad_de_alumnos())
        self.crear_tarjeta(1, 0, "Cursos", service_curso.cantidad_de_cursos())
        self.crear_tarjeta(0, 1, "Inscripciones Activas", service_inscripcion.cantidad_de_inscripciones_activas())
        self.crear_tarjeta(1, 1, "Clases Activas", service_clase.cantidad_de_clases_activas())

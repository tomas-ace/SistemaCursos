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
                    bg=blanco,
                    highlightbackground=borde, #color borde de la tarjeta
                    highlightthickness=2 #grosor borde de tarjetas
                )
            tarjeta.grid(
                    row=fila,
                    column=columna,
                    sticky="nsew", #se expande en todas las direcciones
                    padx=5,
                    pady=5
                )
    
            Label(
                    tarjeta,
                    text=nombre,
                    font=("Arial", 11),
                    bg=blanco
                ).grid(padx=14, pady=(14, 5), column=0, row=0)
    
            Label(
                    tarjeta,
                    text=numero,
                    font=("Arial", 21, "bold"),
                    bg=blanco,
                    fg=azul
                ).grid(padx=14, pady=(0, 12), column=0, row=1)
                
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

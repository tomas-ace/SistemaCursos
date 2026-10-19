from tkinter import *
from Servicios.alumno_service import *
from Servicios.inscripcion_service import *
from Servicios.curso_service import *
from Servicios.clase_service import *

# Colores
azul = "#2864e8"
azul_oscuro = "#093068"
blanco = "#ffffff"
gris = "#6b7280"
texto = "#111827"
borde = "#d1d5db"

class Ventana_Alumnos():
    def __init__(self,contenido):
            self._contenido = contenido
            self._botones = Frame(contenido, bg=blanco)
    def ventana_registro_alumno(self):
        for elemento in self._contenido.winfo_children():
            elemento.destroy()
        Label(
            self._contenido,
            text="Registrar nuevo alumno",
            font=("Arial", 20, "bold"),
            bg=blanco,
            fg=texto
        ).pack(anchor="w", pady=(10, 25))

        Label(
            self._contenido,
            text="Nombre",
            font=("Arial", 12, "bold"),
            bg=blanco,
            fg=texto
        ).pack(anchor="w")

        self._nombre = Entry(
            self._contenido,
            font=("Arial", 12),
            width=40
        )

        self._nombre.pack(
            anchor="w",
            pady=(5, 15)
        )

        # APELLIDO

        Label(
            self._contenido,
            text="Apellido",
            font=("Arial", 12, "bold"),
            bg=blanco,
            fg=texto
        ).pack(anchor="w")

        self._apellido = Entry(
            self._contenido,
            font=("Arial", 12),
            width=40
        )

        self._apellido.pack(
            anchor="w",
            pady=(5, 15)
        )

        # DNI

        Label(
            self._contenido,
            text="DNI",
            font=("Arial", 12, "bold"),
            bg=blanco,
            fg=texto
        ).pack(anchor="w")

        self._dni = Entry(
            self._contenido,
            font=("Arial", 12),
            width=40
        )

        self._dni.pack(
            anchor="w",
            pady=(5, 15)
        )

        # EMAIL

        Label(
            self._contenido,
            text="Email",
            font=("Arial", 12, "bold"),
            bg=blanco,
            fg=texto
        ).pack(anchor="w")

        self._email = Entry(
            self._contenido,
            font=("Arial", 12),
            width=40
        )

        self._email.pack(
            anchor="w",
            pady=(5, 25)
        )
        Label(
                    self._contenido,
                    text="Telefono",
                    font=("Arial", 12, "bold"),
                    bg=blanco,
                    fg=texto
                ).pack(anchor="w")
        telefono = Entry(
                    self._contenido,
                    font=("Arial", 12),
                    width=40
                )
        
        telefono.pack(
                    anchor="w",
                    pady=(5, 25)
                )
        Label(
                    self._contenido,
                    text="Fecha de nacimiento",
                    font=("Arial", 12, "bold"),
                    bg=blanco,
                    fg=texto
                ).pack(anchor="w")
        
        fecha_nacimiento = Entry(
                            self._contenido,
                            font=("Arial", 12),
                            width=40
                        )
                
        fecha_nacimiento.pack(
                            anchor="w",
                            pady=(5, 25)
                        )
        # BOTONES

        FrameBotones = Frame(
            self._contenido,
            bg=blanco
        )

        FrameBotones.pack(anchor="w")

        Button(
            FrameBotones,
            text="Registrar",
            font=("Arial", 12),
            bg=azul,
            fg=blanco,
            bd=0,
            padx=30,
            pady=12,
            command=self.registrar
        ).pack(
            side="left",
            padx=(0, 10)
        )

        Button(
            FrameBotones,
            text="Cancelar",
            font=("Arial", 12),
            bg=gris,
            fg=blanco,
            bd=0,
            padx=30,
            pady=12,
            command=self.cancelar
        ).pack(
            side="left"
        )
    def registrar(self):
        pass
    def cancelar(self):
        pass
    def mostrar_opcion_elegida(self,opcion):
        if opcion == "Registrar nuevo alumno":
            self.ventana_registro_alumno()
        else:
            print("consultar")
    def crear_boton(self,nombre):
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
                ).pack(pady=5)
                
    def mostrar(self):
        print("hola")
        Label(
            self._contenido,
            text="Alumnos",
            font=("Arial", 16, "bold"),
            bg=blanco,
            fg=texto
        ).pack(anchor="w", pady=(8, 4))

        Label(
            self._contenido,
            text="Seleccione la opcion que desee.",
            font=("Arial", 11),
            bg=blanco,
            fg=gris
        ).pack(anchor="w", pady=(0, 18))

        
        self._botones.pack(fill="both", expand=True)#coloca el contenedor y le dice que se ezpanda
        opciones = [
            "Registrar nuevo alumno",
            "Consultar alumnos"
        ]
        for opcion in opciones:
            self.crear_boton(opcion)
    
        


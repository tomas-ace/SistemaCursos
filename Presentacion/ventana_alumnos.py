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
        ).grid(pady=(10, 25), column=0, row=0)


        #datoss
        Label(
            self._contenido,
            text="Nombre",
            font=("Arial", 12, "bold"),
            bg=blanco,
            fg=texto
        ).grid(column=0, row=1)

        self._nombre = Entry(
            self._contenido,
            font=("Arial", 12),
            width=40
        )
        self._nombre.grid(pady=(5, 15), column=1, row=1)

        Label(
            self._contenido,
            text="Apellido",
            font=("Arial", 12, "bold"),
            bg=blanco,
            fg=texto
        ).grid(column=0, row=2)

        self._apellido = Entry(
            self._contenido,
            font=("Arial", 12),
            width=40
        )
        self._apellido.grid(pady=(5, 15), column=1, row=2)
        Label(
            self._contenido,
            text="DNI",
            font=("Arial", 12, "bold"),
            bg=blanco,
            fg=texto
        ).grid(column=0, row=3)

        self._dni = Entry(
            self._contenido,
            font=("Arial", 12),
            width=40
        )

        self._dni.grid(pady=(5, 15), column=1, row=3)
        Label(
            self._contenido,
            text="Email",
            font=("Arial", 12, "bold"),
            bg=blanco,
            fg=texto
        ).grid(column=0, row=4)

        self._email = Entry(
            self._contenido,
            font=("Arial", 12),
            width=40
        )

        self._email.grid(pady=(5, 25), column=1, row=4)
            
        Label(
                    self._contenido,
                    text="Telefono",
                    font=("Arial", 12, "bold"),
                    bg=blanco,
                    fg=texto
                ).grid(column=0, row=5)
        telefono = Entry(
                    self._contenido,
                    font=("Arial", 12),
                    width=40
                )
        
        telefono.grid(pady=(5, 25), column=1, row=5)
        Label(
                    self._contenido,
                    text="Fecha de nacimiento",
                    font=("Arial", 12, "bold"),
                    bg=blanco,
                    fg=texto
                ).grid(column=0, row=6)
        
        fecha_nacimiento = Entry(
                            self._contenido,
                            font=("Arial", 12),
                            width=40
                        )
                
        fecha_nacimiento.grid(pady=(5, 25), column=1, row=6)
                    
        #botones

        Button(
            self._contenido,
            text="Registrar",
            font=("Arial", 12),
            bg=azul,
            fg=blanco,
            bd=0,
            padx=30,
            pady=12,
            command=self.registrar
        ).grid(padx=(0, 10), column=0, row=7)
           

        Button(
            self._contenido,
            text="Cancelar",
            font=("Arial", 12),
            bg=gris,
            fg=blanco,
            bd=0,
            padx=30,
            pady=12,
            command=self.cancelar
        ).grid(padx=(0, 10), column=1, row=7)
    def registrar(self):
        pass
    def cancelar(self):
        pass
    def mostrar_opcion_elegida(self,opcion):
        if opcion == "Registrar nuevo alumno":
            self.ventana_registro_alumno()
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
                ).grid(pady=5,column=0,row=fila)
                
    def mostrar(self):
        print("hola")
        Label(
            self._contenido,
            text="Alumnos",
            font=("Arial", 16, "bold"),
            bg=blanco,
            fg=texto
        ).grid(pady=(8, 4), column=0, row=0)

        Label(
            self._contenido,
            text="Seleccione la opcion que desee.",
            font=("Arial", 11),
            bg=blanco,
            fg=gris
        ).grid(pady=(8, 4), column=0, row=1)

        
        self._botones.grid(column=1,row=2,columnspan=2)#coloca el contenedor y le dice que se ezpanda
        opciones = [
            "Registrar nuevo alumno",
            "Consultar alumnos"
        ]
        fila=0
        for opcion in opciones:
            self.crear_boton(opcion,fila)
            fila+=1
    
        


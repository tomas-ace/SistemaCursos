from tkinter import *
from Servicios.alumno_service import *
from Servicios.inscripcion_service import *
from Servicios.curso_service import *
from Servicios.clase_service import *
from Dominio.alumno import *

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
        ventana = Toplevel(self._contenido)

        ventana.title("Registrar alumno")
        ventana.geometry("600x600")
        ventana.configure(bg=blanco)
        Label(
            ventana,
            text="Registrar nuevo alumno",
            font=("Arial", 20, "bold"),
            bg=blanco,
            fg=texto
        ).grid(pady=(10, 25), column=0, row=0)


        #datoss
        Label(
            ventana,
            text="Nombre",
            font=("Arial", 12, "bold"),
            bg=blanco,
            fg=texto
        ).grid(column=0, row=1)
        nombre = StringVar()
        apellido = StringVar()
        dni = IntVar()
        email = StringVar()
        telefono = IntVar()
        fecha_nacimiento = StringVar()
        self._nombre = Entry(
            ventana,
            font=("Arial", 12),
            width=40,
            textvariable=nombre
        )
        self._nombre.grid(pady=(5, 15), column=1, row=1)

        Label(
            ventana,
            text="Apellido",
            font=("Arial", 12, "bold"),
            bg=blanco,
            fg=texto
        ).grid(column=0, row=2)

        self._apellido = Entry(
            ventana,
            font=("Arial", 12),
            width=40,
            textvariable=apellido
        )
        self._apellido.grid(pady=(5, 15), column=1, row=2)
        Label(
            ventana,
            text="DNI",
            font=("Arial", 12, "bold"),
            bg=blanco,
            fg=texto
        ).grid(column=0, row=3)

        self._dni = Entry(
            ventana,
            font=("Arial", 12),
            width=40,
            textvariable=dni
        )

        self._dni.grid(pady=(5, 15), column=1, row=3)
        Label(
            ventana,
            text="Email",
            font=("Arial", 12, "bold"),
            bg=blanco,
            fg=texto
        ).grid(column=0, row=4)

        self._email = Entry(
            ventana,
            font=("Arial", 12),
            width=40,
            textvariable=email
        )

        self._email.grid(pady=(5, 25), column=1, row=4)
            
        Label(
                    ventana,
                    text="Telefono",
                    font=("Arial", 12, "bold"),
                    bg=blanco,
                    fg=texto
                ).grid(column=0, row=5)
        self._telefono = Entry(
                    ventana,
                    font=("Arial", 12),
                    width=40,
                    textvariable=telefono
                )
        
        self._telefono.grid(pady=(5, 25), column=1, row=5)
        Label(
                    ventana,
                    text="Fecha de nacimiento",
                    font=("Arial", 12, "bold"),
                    bg=blanco,
                    fg=texto
                ).grid(column=0, row=6)
        
        self._fecha_nacimiento = Entry(
                            ventana,
                            font=("Arial", 12),
                            width=40,
                            textvariable=fecha_nacimiento
                        )
                
        self._fecha_nacimiento.grid(pady=(5, 25), column=1, row=6)
                    
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
            command=lambda: self.registrar(nombre.get(),apellido.get(),dni.get(),email.get(),telefono.get(),fecha_nacimiento.get())
        ).grid(padx=(0, 10), column=0, row=7)
           

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
        ).grid(padx=(0, 10), column=1, row=7)
    def registrar(self,nombre,apelleido,dni,email,telefono,fecha_nacimiento):
        print(nombre)
        print(apelleido)
        print(dni)
        print(email)
        print(telefono) 
        print(fecha_nacimiento)
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

        
        self._botones.grid(column=0,row=2,columnspan=1)#coloca el contenedor y le dice que se ezpanda
        opciones = [
            "Registrar nuevo alumno",
            "Consultar alumnos"
        ]
        fila=0
        for opcion in opciones:
            self.crear_boton(opcion,fila)
            fila+=1
    
        


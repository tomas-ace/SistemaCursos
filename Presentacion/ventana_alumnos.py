from tkinter import *
from Servicios.alumno_service import *
from Servicios.inscripcion_service import *
from Servicios.curso_service import *
from Servicios.clase_service import *
from Dominio.alumno import *
from Presentacion.treeview import treeview

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
    def ventana_registro_alumno(self,ventana_none):
        if ventana_none == None:
            pass
        else:
            ventana_none.destroy()
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
        dia= StringVar()
        mes= StringVar()
        anio= StringVar()
        self._nombre = Entry(
            ventana,
            font=("Arial", 12),
            textvariable=nombre
        )
        self._nombre.grid(pady=(5, 15), column=1, row=1,columnspan=2)

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
            textvariable=apellido
        )
        self._apellido.grid(pady=(5, 15), column=1, row=2,columnspan=2)
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
            textvariable=dni
        )

        self._dni.grid(pady=(5, 15), column=1, row=3,columnspan=2)
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
            textvariable=email
        )

        self._email.grid(pady=(5, 25), column=1, row=4,columnspan=2)
            
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
                    textvariable=telefono
                )
        
        self._telefono.grid(pady=(5, 25), column=1, row=5,columnspan=2)
        Label(
                    ventana,
                    text="Fecha de nacimiento",
                    font=("Arial", 12, "bold"),
                    bg=blanco,
                    fg=texto
                ).grid(column=0, row=6)
        Label(
                    ventana,
                    text="Dia",
                    font=("Arial", 12, "bold"),
                    bg=blanco,
                    fg=texto
                ).grid(column=1, row=6)
        self._dia = Entry(
                            ventana,
                            font=("Arial", 12),
                            width=7,
                            textvariable=dia
                        )
                
        self._dia.grid(pady=(5, 25), column=2, row=6)

        Label(
                            ventana,
                            text="Mes",
                            font=("Arial", 12, "bold"),
                            bg=blanco,
                            fg=texto
                        ).grid(column=1, row=7)

        self._mes = Entry(
                                    ventana,
                                    font=("Arial", 12),
                                    textvariable=mes,
                                    width=7
                                )
                        
        self._mes.grid(pady=(5, 25), column=2, row=7)

        Label(
                            ventana,
                            text="Año",
                            font=("Arial", 12, "bold"),
                            bg=blanco,
                            fg=texto
                        ).grid(column=1, row=8)
        self._anio = Entry(
                                    ventana,
                                    font=("Arial", 12),
                                    textvariable=anio,
                                    width=7
                                )
                        
        self._anio.grid(pady=(5, 25), column=2, row=8)
        #sfecha=f"{dia.get()}-{mes.get()}-{anio.get()}"
                    
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
            command=lambda: self.registrar(nombre.get(),apellido.get(),dni.get(),email.get(),telefono.get(),f"{anio.get()}-{mes.get()}-{dia.get()}",ventana)
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
            command=lambda: self.cancelar(ventana)
        ).grid(padx=(0, 10), column=1, row=9)

    def registrar(self,nombre,apelleido,dni,email,telefono,fecha_nacimiento,ventana):
        nuevo_alumno=Alumno(None,nombre,apelleido,fecha_nacimiento,dni,telefono,email)
        servicio_alumno=Alumno_Service()
        servicio_alumno.nuevo_alumno(nuevo_alumno)
        ventana.destroy()
       
    def cancelar(self,ventana):
        ventana.destroy()
    def mostrar_opcion_elegida(self,opcion):
        if opcion == "Registrar nuevo alumno":
            self.ventana_registro_alumno(None)
        else:
            self.lista_de_alumnos()
    def lista_de_alumnos(self):
        ventana_lista = Toplevel(self._contenido)
        ventana_lista.title("Lista de alumnos")
        ventana_lista.geometry("1500x600")
        ventana_lista.configure(bg=blanco)
        Label(
            ventana_lista,
            text="Lista de alumnos",
            font=("Arial", 20, "bold"),
            bg=blanco,
            fg=texto
        ).grid(pady=(10, 25), column=0, row=0)
        columnas = ["ID", "Nombre", "Apellido", "DNI", "Telefono", "Email", "Fecha de nacimiento"]
        datos_alumnos = Alumno_Service().listar_alumnos()
        tree=treeview(ventana_lista, columnas, datos_alumnos)
        frame_acciones = Frame(ventana_lista, bg=blanco)
        frame_acciones.grid(column=0, row=2, padx=20, pady=10)

        Button(
            frame_acciones,
            text="Agregar Nuevo",
            font=("Arial", 11, "bold"),
            bg=azul,
            fg=blanco,
            bd=0,
            padx=20,
            pady=10,
            command=lambda: self.ventana_registro_alumno(ventana_lista)
        ).pack(side="left", padx=10)

        Button(
            frame_acciones,
            text="Modificar Seleccionado",
            font=("Arial", 11, "bold"),
            bg=gris,
            fg=blanco,
            bd=0,
            padx=20,
            pady=10,
            command=lambda: self.preparar_modificacion(tree,ventana_lista)
        ).pack(side="left", padx=10)
        
        Button(
                    frame_acciones,
                    text="Ver Detalle",
                    font=("Arial", 11, "bold"),
                    bg=gris,
                    fg=blanco,
                    bd=0,
                    padx=20,
                    pady=10,
                    command=lambda: self.detalle_alumno(tree,ventana_lista)
                ).pack(side="left", padx=10)
        
    def detalle_alumno(self,tree,ventana):
        if not seleccion:
            print("Por favor, seleccione un alumno de la tabla.")
            return
        ventana.destroy() 
        ventana_detalle = Toplevel(self._contenido)
        ventana_detalle.title("Detalle del alumno")
        ventana_detalle.geometry("600x600")
        ventana_detalle.configure(bg=blanco)
        seleccion = tree.selection()
    

        item_id = seleccion[0]
        datos_alumno = tree.item(item_id)['values']
        
    def preparar_modificacion(self,tree,ventana): 
        seleccion = tree.selection()
        if not seleccion:
            print("Por favor, seleccione un alumno de la tabla.")
            return

        item_id = seleccion[0]
        print("item_id:", item_id)
        datos_alumno = tree.item(item_id)['values']
        print("datos_alumno:", datos_alumno[0])
        ventana.destroy() 
        self.ventana_modificar_alumno(datos_alumno)
        
    def ventana_modificar_alumno(self,datos_alumno):
        ventana = Toplevel(self._contenido)
        ventana.title("Modificar alumno")
        ventana.geometry("600x600")
        ventana.configure(bg=blanco)

        Label(
            ventana,
            text="Modificar alumno",
            font=("Arial", 20, "bold"),
            bg=blanco,
            fg=texto
        ).grid(pady=(10, 25), column=0, row=0)

        #cargo las variabkes con los datos
        id_alumno = datos_alumno[0]
        nombre = StringVar(value=datos_alumno[1])
        apellido = StringVar(value=datos_alumno[2])
        dni = IntVar(value=datos_alumno[3])
        telefono = IntVar(value=datos_alumno[4])
        email = StringVar(value=datos_alumno[5])
        nacimiento = datos_alumno[6]

        #campos 
        Label(ventana, text="Nombre", font=("Arial", 12, "bold"), bg=blanco, fg=texto).grid(column=0, row=1)
        Entry(ventana, font=("Arial", 12), textvariable=nombre).grid(pady=(5, 15), column=1, row=1, columnspan=2)

        Label(ventana, text="Apellido", font=("Arial", 12, "bold"), bg=blanco, fg=texto).grid(column=0, row=2)
        Entry(ventana, font=("Arial", 12), textvariable=apellido).grid(pady=(5, 15), column=1, row=2, columnspan=2)

        Label(ventana, text="DNI", font=("Arial", 12, "bold"), bg=blanco, fg=texto).grid(column=0, row=3)
        Entry(ventana, font=("Arial", 12), textvariable=dni).grid(pady=(5, 15), column=1, row=3, columnspan=2)

        Label(ventana, text="Email", font=("Arial", 12, "bold"), bg=blanco, fg=texto).grid(column=0, row=4)
        Entry(ventana, font=("Arial", 12), textvariable=email).grid(pady=(5, 25), column=1, row=4, columnspan=2)

        Label(ventana, text="Telefono", font=("Arial", 12, "bold"), bg=blanco, fg=texto).grid(column=0, row=5)
        Entry(ventana, font=("Arial", 12), textvariable=telefono).grid(pady=(5, 25), column=1, row=5, columnspan=2)


        # Botón para guardar cambios
        Button(
            ventana,
            text="Guardar Cambios",
            font=("Arial", 12),
            bg=azul,
            fg=blanco,
            bd=0,
            padx=20,
            pady=12,
            command=lambda: self.guardar_modificacion(id_alumno, nombre.get(), apellido.get(), dni.get(), email.get(), telefono.get(), nacimiento,ventana)
        ).grid(padx=(0, 10), column=0, row=9)

        Button(
            ventana,
            text="Cancelar",
            font=("Arial", 12),
            bg=gris,
            fg=blanco,
            bd=0,
            padx=20,
            pady=12,
            command=ventana.destroy
        ).grid(padx=(0, 10), column=1, row=9)

    def guardar_modificacion(self, id_alumno, nombre, apellido, dni, email, telefono, fecha_nacimiento, ventana):
        alumno_actualizado = Alumno(id_alumno, nombre, apellido, fecha_nacimiento, dni, telefono, email)
        servicio_alumno = Alumno_Service()
        servicio_alumno.modificar_alumno(alumno_actualizado)
        print(f"Alumno {id_alumno} modificado con éxito")
        ventana.destroy()
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
    
        


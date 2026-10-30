from tkinter import *
from Servicios.alumno_service import *
from Servicios.inscripcion_service import *
from Servicios.curso_service import *
from Servicios.clase_service import *
from Dominio.alumno import *
from Presentacion.elementos import *



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
            bg=blanco
            
        ).grid(pady=(10, 25), column=0, row=0)


        #datoss
        Label(
            ventana,
            text="Nombre",
            font=("Arial", 12, "bold"),
            bg=blanco
            
        ).grid(column=0, row=1)
        nombre = StringVar()
        apellido = StringVar()
        dni = IntVar()
        email = StringVar()
        telefono = IntVar()
        dia= StringVar()
        mes= StringVar()
        anio= StringVar()
        entry_nombre = Entry(
            ventana,
            font=("Arial", 12),
            textvariable=nombre
        )
        entry_nombre.grid(pady=(5, 15), column=1, row=1,columnspan=2)

        Label(
            ventana,
            text="Apellido",
            font=("Arial", 12, "bold"),
            bg=blanco
            
        ).grid(column=0, row=2)

        entry_apellido = Entry(
            ventana,
            font=("Arial", 12),
            textvariable=apellido
        )
        entry_apellido.grid(pady=(5, 15), column=1, row=2,columnspan=2)
        Label(
            ventana,
            text="DNI",
            font=("Arial", 12, "bold"),
            bg=blanco
            
        ).grid(column=0, row=3)

        entry_dni = Entry(
            ventana,
            font=("Arial", 12),
            textvariable=dni
        )

        entry_dni.grid(pady=(5, 15), column=1, row=3,columnspan=2)
        Label(
            ventana,
            text="Email",
            font=("Arial", 12, "bold"),
            bg=blanco
            
        ).grid(column=0, row=4)

        entry_email = Entry(
            ventana,
            font=("Arial", 12),
            textvariable=email
        )

        entry_email.grid(pady=(5, 25), column=1, row=4,columnspan=2)
            
        Label(
                    ventana,
                    text="Telefono",
                    font=("Arial", 12, "bold"),
                    bg=blanco
                    
                ).grid(column=0, row=5)
        entry_telefono = Entry(
                    ventana,
                    font=("Arial", 12),
                    textvariable=telefono
                )
        
        entry_telefono.grid(pady=(5, 25), column=1, row=5,columnspan=2)
        Label(
                    ventana,
                    text="Fecha de nacimiento",
                    font=("Arial", 12, "bold"),
                    bg=blanco
                    
                ).grid(column=0, row=6)
        Label(
                    ventana,
                    text="Dia",
                    font=("Arial", 12, "bold"),
                    bg=blanco
                    
                ).grid(column=1, row=6)
        entry_dia = Entry(
                            ventana,
                            font=("Arial", 12),
                            width=7,
                            textvariable=dia
                        )
                
        entry_dia.grid(pady=(5, 25), column=2, row=6)

        Label(
                            ventana,
                            text="Mes",
                            font=("Arial", 12, "bold"),
                            bg=blanco
                            
                        ).grid(column=1, row=7)

        entry_mes = Entry(
                                    ventana,
                                    font=("Arial", 12),
                                    textvariable=mes,
                                    width=7
                                )
                        
        entry_mes.grid(pady=(5, 25), column=2, row=7)

        Label(
                            ventana,
                            text="Año",
                            font=("Arial", 12, "bold"),
                            bg=blanco
                            
                        ).grid(column=1, row=8)
        entry_anio = Entry(
                                    ventana,
                                    font=("Arial", 12),
                                    textvariable=anio,
                                    width=7
                                )
                        
        entry_anio.grid(pady=(5, 25), column=2, row=8)
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
        print (opcion)
        if opcion == "Registrar nuevo alumno":
            self.ventana_registro_alumno(None)
        else:
            self.lista_de_alumnos()
            
    def lista_de_alumnos(self,contenedor=None):
        if contenedor == None:
            ventana_lista = Toplevel(self._contenido)
            ventana_lista.title("Lista de alumnos")
            ventana_lista.geometry("1500x600")
            ventana_lista.configure(bg=blanco)
            Label(
                ventana_lista,
                text="Lista de alumnos",
                font=("Arial", 20, "bold"),
                bg=blanco
                
            ).grid(pady=(10, 25), column=0, row=0)
        else:
            ventana_lista = contenedor
        
        columnas = ["ID", "Nombre", "Apellido", "DNI", "Telefono", "Email", "Fecha de nacimiento"]
        datos_alumnos = Alumno_Service().listar_alumnos()
        tree=treeview(ventana_lista, columnas, datos_alumnos)
        frame_acciones = Frame(ventana_lista, bg=blanco)
        frame_acciones.grid(column=0, row=2, padx=20, pady=10)

        if contenedor == None:
            Button(
                        frame_acciones,
                        text="Agregar Nuevo",
                        font=("Arial", 11, "bold"),
                        bg=azul,
                        fg=blanco,
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
        return tree
        
        
    def detalle_alumno(self,tree,ventana):
        seleccion = tree.selection()
        if not seleccion:
            print("Por favor, seleccione un alumno de la tabla.")
            return
         
        item_id = seleccion[0]
        datos_alumno = tree.item(item_id)['values']
        ventana.destroy()
        ventana_detalle = Toplevel(self._contenido)
        ventana_detalle.title("Detalle del alumno")
        ventana_detalle.geometry("600x600")
        ventana_detalle.configure(bg=blanco)


        Label(
            ventana_detalle,
            text="Detalle del alumno",
            font=("Arial", 20, "bold"),
            bg=blanco
            
        ).pack(pady=(20, 20))

       
        frame_datos = Frame(ventana_detalle, bg=blanco)
        frame_datos.pack(pady=10)
        titulos_columnas = ["ID:", "Nombre:", "Apellido:", "DNI:", "Teléfono:", "Email:", "Fecha de nacimiento:"]
        for i in range(len(titulos_columnas)):
            if i==0:
                continue

            titulo = titulos_columnas[i]
            
            
            Label(
                frame_datos,
                text=titulo,
                font=("Arial", 12, "bold"),
                bg=blanco,
                width=18
            ).grid(row=i, column=0, pady=8, padx=10)

           
            Label(
                frame_datos,
                text=str(datos_alumno[i]),
                font=("Arial", 12),
                bg=blanco,
                fg=gris
            ).grid(row=i, column=1, pady=8, padx=10)

        frame_datos_cursada = Frame(ventana_detalle, bg=blanco)
        frame_datos_cursada.pack(pady=40)

        Button(
            frame_datos_cursada,
            text="Cursos",
            font=("Arial", 11, "bold"),
            bg=azul,
            fg=blanco,
            padx=20,
            pady=10,
            command=lambda: self.cursos_alumno(datos_alumno[0])
        ).grid(column=0,row=0, padx=10)

        Button(
            frame_datos_cursada,
            text="Notas",
            font=("Arial", 11, "bold"),
            bg=azul,
            fg=blanco,
            padx=20,
            pady=10,
            command=lambda: self.notas_alumno(datos_alumno[0])
        ).grid(column=1,row=0, padx=10)

        Button(
            frame_datos_cursada,
            text="Inasistencias",
            font=("Arial", 11, "bold"),
            bg=azul,
            fg=blanco,
            padx=20,
            pady=10,
            command=lambda: self.inasistencias_alumno(datos_alumno[0])
        ).grid(column=2,row=0, padx=10)
    def cursos_alumno(self, alumno_id):
        cursos=Alumno_Service().cursos_por_alumno(alumno_id)
        ventana_cursos = Toplevel(self._contenido)
        ventana_cursos.title("Cursos del alumno")
        ventana_cursos.geometry("1200x400")
        ventana_cursos.configure(bg=blanco)

        Label(
            ventana_cursos,
            text="Historial de Cursos",
            font=("Arial", 18, "bold"),
            bg=blanco
            
        ).grid(pady=(15, 10),column=0, row=0)

    
        if not cursos:
            Label(
                ventana_cursos,
                text="Este alumno no está inscripto en ningún curso actualmente.",
                font=("Arial", 12),
                bg=blanco,
                fg=gris
            ).grid(pady=30, column=0, row=1)
            return 

        columnas = ["Descripción", "Duración", "Turno", "Año", "Fecha de Inscripción", "Estado"]

        tabla_cursos = treeview(ventana_cursos, columnas, cursos)
        
        
        Button(
            ventana_cursos,
            text="Cerrar",
            font=("Arial", 11, "bold"),
            bg=gris,
            fg=blanco,
            bd=0,
            padx=20,
            pady=10,
            command=ventana_cursos.destroy
        ).grid(pady=15, column=0, row=2)
    def notas_alumno(self, alumno_id):
        notas=Alumno_Service().notas_por_alumno(alumno_id)
        ventana_notas = Toplevel(self._contenido)
        ventana_notas.title("Notas del alumno")
        ventana_notas.geometry("1200x400")
        ventana_notas.configure(bg=blanco)

        Label(
            ventana_notas,
            text="Historial de Notas",
            font=("Arial", 18, "bold"),
            bg=blanco
            
        ).grid(pady=(15, 10),column=0, row=0)

    
        if not notas:
            Label(
                ventana_notas,
                text="Este alumno no tiene notas registradas.",
                font=("Arial", 12),
                bg=blanco,
                fg=gris
            ).grid(pady=30, column=0, row=1)
            return 

        columnas = ["Fecha", "Descripcion", "Curso", "Año", "Nota"]

        tabla_notas = treeview(ventana_notas, columnas, notas)
        
        
        Button(
            ventana_notas,
            text="Cerrar",
            font=("Arial", 11, "bold"),
            bg=gris,
            fg=blanco,
            bd=0,
            padx=20,
            pady=10,
            command=ventana_notas.destroy
        ).grid(pady=15, column=0, row=2)     
    
    def inasistencias_alumno(self, alumno_id):
        inasistencias=Alumno_Service().inasistencias_por_alumno(alumno_id)
        ventana_inasistencias = Toplevel(self._contenido)
        ventana_inasistencias.title("Inasistencias del alumno")
        ventana_inasistencias.geometry("900x400")
        ventana_inasistencias.configure(bg=blanco)

        Label(
            ventana_inasistencias,
            text="Historial de Inasistencias",
            font=("Arial", 18, "bold"),
            bg=blanco
            
        ).grid(pady=(15, 10),column=0, row=0)

    
        if not inasistencias:
            Label(
                ventana_inasistencias,
                text="Este alumno no tiene inasistencias registradas.",
                font=("Arial", 12),
                bg=blanco,
                fg=gris
            ).grid(pady=30, column=0, row=1)
            return 

        columnas = ["Curso", "Año", "Fecha"]

        tabla_inasistencias = treeview(ventana_inasistencias, columnas, inasistencias)
        
        
        Button(
            ventana_inasistencias,
            text="Cerrar",
            font=("Arial", 11, "bold"),
            bg=gris,
            fg=blanco,
            padx=20,
            pady=10,
            command=ventana_inasistencias.destroy
        ).grid(pady=15, column=0, row=2)
    def preparar_modificacion(self,tree,ventana): 
        seleccion = tree.selection()
        if not seleccion:
            print("seleccione un alumno de la tabla.")
            return

        item_id = seleccion[0]#guarda el id interno del treeviewe que le asigna tkinter
        print("item_id:", item_id)
        datos_alumno = tree.item(item_id)['values']#guarda los valores de la fila en una lista
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
            bg=blanco
            
        ).grid(pady=(10, 25), column=0, row=0)

        #cargo las variabkes con los datos
        id_alumno = datos_alumno[0] #sin el intvar porque no lo modifico
        nombre = StringVar(value=datos_alumno[1])
        apellido = StringVar(value=datos_alumno[2])
        dni = IntVar(value=datos_alumno[3])
        telefono = IntVar(value=datos_alumno[4])
        email = StringVar(value=datos_alumno[5])
        nacimiento = datos_alumno[6]

        #campos 
        Label(ventana, text="Nombre", font=("Arial", 12, "bold"), bg=blanco).grid(column=0, row=1)
        Entry(ventana, font=("Arial", 12), textvariable=nombre).grid(pady=(5, 15), column=1, row=1, columnspan=2)

        Label(ventana, text="Apellido", font=("Arial", 12, "bold"), bg=blanco).grid(column=0, row=2)
        Entry(ventana, font=("Arial", 12), textvariable=apellido).grid(pady=(5, 15), column=1, row=2, columnspan=2)

        Label(ventana, text="DNI", font=("Arial", 12, "bold"), bg=blanco).grid(column=0, row=3)
        Entry(ventana, font=("Arial", 12), textvariable=dni).grid(pady=(5, 15), column=1, row=3, columnspan=2)

        Label(ventana, text="Email", font=("Arial", 12, "bold"), bg=blanco).grid(column=0, row=4)
        Entry(ventana, font=("Arial", 12), textvariable=email).grid(pady=(5, 25), column=1, row=4, columnspan=2)

        Label(ventana, text="Telefono", font=("Arial", 12, "bold"), bg=blanco).grid(column=0, row=5)
        Entry(ventana, font=("Arial", 12), textvariable=telefono).grid(pady=(5, 25), column=1, row=5, columnspan=2)

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
        ventana.destroy()
    
                
    def mostrar(self):
        print("hola")
        Label(
            self._contenido,
            text="Alumnos",
            font=("Arial", 16, "bold"),
            bg=blanco
        ).grid(pady=(8, 4), column=0, row=0)

        Label(
            self._contenido,
            text="Seleccione la opcion que desee.",
            font=("Arial", 11),
            bg=blanco,
            fg=gris
        ).grid(pady=(8, 4), column=0, row=1)

        
        self._botones.grid(column=0,row=2,columnspan=1)
        opciones = [
            "Registrar nuevo alumno",
            "Consultar alumnos"
        ]
        fila=0
        for opcion in opciones:
            print (opcion)
            crear_boton(opcion,fila,self._botones,lambda opcion_actual=opcion: self.mostrar_opcion_elegida(opcion_actual)) #lambda para que no se me ejecuten las funciones 
            fila+=1 #opcion_actual congela la variable y la guarda, si no, se ejecuta siempre la ultima opcion
    
        


from tkinter import *
from Servicios.alumno_service import *
from Servicios.inscripcion_service import *
from Servicios.curso_service import *
from Servicios.clase_service import *
from Dominio.alumno import *
from Presentacion.elementos import *
from Presentacion.ventana_inscripciones import *
from tkinter import messagebox


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
        ventana.geometry("550x650")
        ventana.maxsize(550,650)
        ventana.configure(bg=blanco)
        form_frame = Frame(ventana, bg="white", highlightbackground=azul, highlightthickness=1, padx=40, pady=30)
        form_frame.pack(expand=True, pady=20)
        Label(
            form_frame,
            text="Registrar nuevo alumno",
            font=("Arial", 18, "bold"),
            bg="white",
            fg=azul
        ).grid(row=0, column=0, columnspan=2, pady=(0, 30))


        #datoss
        
        nombre = StringVar()
        apellido = StringVar()
        dni = StringVar()
        email = StringVar()
        telefono = StringVar()
        dia= StringVar()
        mes= StringVar()
        anio= StringVar()
        Label(
            form_frame,
            text="Nombre",
            font=("Arial", 12, "bold")
            
        ).grid(column=0, row=1)
        entry_nombre = Entry(
            form_frame,
            font=("Arial", 12),
            textvariable=nombre, highlightbackground=azul_oscuro, highlightthickness=1
        )
        entry_nombre.grid(pady=(5, 15), column=1, row=1,columnspan=2)

        Label(
            form_frame,
            text="Apellido",
            font=("Arial", 12, "bold")
            
        ).grid(column=0, row=2)

        entry_apellido = Entry(
            form_frame,
            font=("Arial", 12),
            textvariable=apellido, highlightbackground=azul_oscuro, highlightthickness=1
        )
        entry_apellido.grid(pady=(5, 15), column=1, row=2,columnspan=2)
        Label(
            form_frame,
            text="DNI",
            font=("Arial", 12, "bold")
            
        ).grid(column=0, row=3)

        entry_dni = Entry(
            form_frame,
            font=("Arial", 12),
            textvariable=dni, highlightbackground=azul_oscuro, highlightthickness=1
        )

        entry_dni.grid(pady=(5, 15), column=1, row=3,columnspan=2)
        Label(
            form_frame,
            text="Email",
            font=("Arial", 12, "bold")
        ).grid(column=0, row=4)

        entry_email = Entry(
            form_frame,
            font=("Arial", 12),
            textvariable=email, highlightbackground=azul_oscuro, highlightthickness=1
        )

        entry_email.grid(pady=(5, 25), column=1, row=4,columnspan=2)
            
        Label(
                    form_frame,
                    text="Telefono",
                    font=("Arial", 12, "bold")
                ).grid(column=0, row=5)
        entry_telefono = Entry(
                    form_frame,
                    font=("Arial", 12),
                    textvariable=telefono, highlightbackground=azul_oscuro, highlightthickness=1
                )
        
        entry_telefono.grid(pady=(5, 25), column=1, row=5,columnspan=2)
        Label(
                    form_frame,
                    text="Fecha de nacimiento",
                    font=("Arial", 12, "bold")
                ).grid(column=0, row=6)
        Label(
                    form_frame,
                    text="Dia",
                    font=("Arial", 12, "bold")
                    
                ).grid(column=1, row=6)
        entry_dia = Entry(
                            form_frame,
                            font=("Arial", 12),
                            width=7,
                            textvariable=dia, highlightbackground=azul_oscuro, highlightthickness=1
                        )
                
        entry_dia.grid(pady=(5, 25), column=2, row=6)

        Label(
                            form_frame,
                            text="Mes",
                            font=("Arial", 12, "bold")
                            
                        ).grid(column=1, row=7)

        entry_mes = Entry(
                                    form_frame,
                                    font=("Arial", 12),
                                    textvariable=mes,
                                    width=7, highlightbackground=azul_oscuro, highlightthickness=1
                                )
                        
        entry_mes.grid(pady=(5, 25), column=2, row=7)

        Label(
                            form_frame,
                            text="Año",
                            font=("Arial", 12, "bold")
                            
                        ).grid(column=1, row=8)
        entry_anio = Entry(
                                    form_frame,
                                    font=("Arial", 12),
                                    textvariable=anio,
                                    width=7, highlightbackground=azul_oscuro, highlightthickness=1
                                )
                        
        entry_anio.grid(pady=(5, 25), column=2, row=8)
        #sfecha=f"{dia.get()}-{mes.get()}-{anio.get()}"
                    
        #botones

        Button(
            form_frame,
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
            form_frame,
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
        resultado = servicio_alumno.nuevo_alumno(nuevo_alumno)
        if resultado==True:
            messagebox.showinfo("Exito", "Alumno registrado correctamente.", parent=ventana)
            ventana.destroy()
        else:
            messagebox.showerror("Error", resultado, parent=ventana)
        
            
       
    def cancelar(self,ventana):
        ventana.destroy()
    
    def mostrar_opcion_elegida(self,opcion):
        
        if opcion == "Registrar nuevo alumno":
            self.ventana_registro_alumno(None)

        elif opcion == "Inscribir a un Curso":
            from Presentacion.ventana_inscripciones import Ventana_Inscripciones
            ventana_insc=Ventana_Inscripciones(self._contenido)
            ventana_insc.ventana_registro_inscripcion(None)
        else:
            self.lista_de_alumnos()
            
    def lista_de_alumnos(self,contenedor=None):
        if contenedor == None:
            ventana_lista = Toplevel(self._contenido)
            ventana_lista.title("Lista de alumnos")
            ventana_lista.geometry("400x320")
            ventana_lista.maxsize(600, 320)
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
        tree["displaycolumns"] = ("Nombre", "Apellido")
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
        
        
    def detalle_alumno(self,tree=None,ventana=None,datos_actualizacion_ventana=None):
        if datos_actualizacion_ventana is None:
            seleccion = tree.selection()
            if not seleccion:
                messagebox.showinfo("Error","Por favor, seleccione un alumno de la tabla.", parent=ventana)
                return
             
            item_id = seleccion[0]
            datos_alumno = tree.item(item_id)['values']
            if ventana is not None:
                ventana.destroy()
        else:
            datos_alumno = datos_actualizacion_ventana
         
       
       
        ventana_detalle = Toplevel(self._contenido)
        ventana_detalle.title("Detalle del alumno")
        ventana_detalle.geometry("1100x900")
        ventana_detalle.minsize(1100,900)
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
        frame_botones = Frame(ventana_detalle, bg=blanco)
        frame_botones.pack(pady=10)
        Button(
                frame_botones,
                text="Modificar Datos",
                font=("Arial", 11, "bold"),
                bg=gris,
                fg=blanco,
                bd=0,
                padx=20,
                pady=10,
                command=lambda: self.ventana_modificar_alumno(datos_alumno,ventana_detalle)
            ).grid(row=0,column=0,padx=10)
        Button(
                frame_botones,
                text="Inscribir a un Curso",
                font=("Arial", 11, "bold"),
                bg=gris,
                fg=blanco,
                bd=0,
                padx=20,
                pady=10,
                command=lambda: self.inscripcion(datos_alumno,ventana_detalle)
            ).grid(row=0,column=2,padx=10)
        
        Label(ventana_detalle, text="Historial Académico", font=("Arial", 16, "bold"), bg=blanco).pack(pady=(30, 10))
        contenedor_scroll = Frame(ventana_detalle, bg=blanco)
        contenedor_scroll.pack(padx=20, pady=10, fill="both", expand=True)

        canvas = Canvas(contenedor_scroll, bg=blanco, highlightthickness=0)
        scrollbar = ttk.Scrollbar(contenedor_scroll, orient="vertical", command=canvas.yview)

        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        frame_datos_cursada = Frame(canvas, bg=blanco)
        frame_datos_cursada.pack(padx=20, pady=10, fill="both", expand=True)

        canvas_window = canvas.create_window((0, 0), window=frame_datos_cursada, anchor="nw")
        frame_datos_cursada.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.bind(
            "<Configure>",
            lambda e: canvas.itemconfig(canvas_window, width=e.width)
        )
        
        id_alumno = datos_alumno[0]
        servicio_alumno = Alumno_Service()
        servicio_nota = Nota_Service()
        servicio_asistencia = Asistencia_Service()
        historial_cursos = servicio_alumno.cursos_por_alumno(id_alumno)
        if not historial_cursos:
            Label(frame_datos_cursada, text="El alumno no registra inscripciones en ningún curso.", font=("Arial", 12, "italic"), bg=blanco, fg=gris).pack()
            return
        columna_actual = 0
        fila_actual = 0
        max_columnas_por_fila = 3 

        for curso in historial_cursos:
            id_inscripcion = curso[0]
            id_clase = curso[1]
            nombre_curso = curso[2]
            anio = curso[3]
            if curso[4]=="Maniana":
                turno = "Mañana"
            else:
                turno = curso[4]
            estado = curso[5]
           
            promedio = servicio_nota.promedio_alumno_en_clase(id_inscripcion)
            asistencia = servicio_asistencia.calcular_porcentaje_asistencia(id_inscripcion)

            #frame de los datos
            frame_cursos = Frame(frame_datos_cursada, bg='white', highlightbackground="black", highlightthickness=2, padx=10, pady=10)
            frame_cursos.grid(row=fila_actual, column=columna_actual, padx=15, pady=15, sticky="nsew")

            #titulo
            Label(frame_cursos, text=nombre_curso, font=("Arial", 14, "bold"), bg='white').pack(anchor="w", pady=(0, 10))
            
            #separador
            Frame(frame_cursos, height=2, bg="black").pack(fill="x", pady=(0, 10))

            Label(frame_cursos, text=f"Año: {anio}", font=("Arial", 11), bg='white').pack(anchor="w")
            Label(frame_cursos, text=f"Turno: {turno}", font=("Arial", 11), bg='white').pack(anchor="w")
            Label(frame_cursos, text=f"Estado: {estado}", font=("Arial", 11, "italic"), bg='white', fg=gris).pack(anchor="w", pady=(5, 10))
            Label(frame_cursos, text=f"Asistencia: {asistencia}%", font=("Arial", 11, "bold"), bg='white').pack(anchor="w")
            Label(frame_cursos, text=f"Promedio: {promedio}", font=("Arial", 11, "bold"), bg='white').pack(anchor="w", pady=(0, 15))

            frame_botones_card = Frame(frame_cursos, bg='white')
            frame_botones_card.pack(fill="x", side="bottom")

            
            Button(frame_botones_card, text="Notas", font=("Arial", 9), bg=azul,fg="white",command=lambda id_ins=id_inscripcion: self.ver_notas(id_ins)).pack(side="left", padx=2)
            Button(frame_botones_card, text="Asistencia", font=("Arial", 9), bg=azul,fg="white",command=lambda id_ins=id_inscripcion: self.ver_asistencias(id_ins)).pack(side="left", padx=2)
            Button(frame_botones_card, text="Baja", font=("Arial", 9), bg="#ff4c4c", fg="white", command=lambda id_ins=id_inscripcion: self.dar_de_baja(id_ins,ventana_detalle, datos_alumno)).pack(side="right", padx=2)

            columna_actual += 1
            if columna_actual >= max_columnas_por_fila:
                columna_actual = 0
                fila_actual += 1
                
    def inscripcion(self,datos_alumno,ventana_detalle):
        service=Alumno_Service()
        cantidad_inscripciones=service.cantidad_de_inscripciones_activas(datos_alumno[0])
        if cantidad_inscripciones >= 3:
            messagebox.showinfo("Maximo de clases","Este alumno ya esta cursando 3 clases actualmente")
            return
        legajo=datos_alumno[0]
        ventana_insc=Ventana_Inscripciones(self._contenido)
        ventana = Toplevel(self._contenido) 
        ventana_detalle.destroy()   
        ventana.title("Registrar nueva inscripcion")
        ventana.geometry("600x600")
        ventana.configure(bg=blanco)
        Label(
            ventana,
            text="Registrar nueva inscripcion",
            font=("Arial", 20, "bold"),
            bg=blanco,
            fg=texto
        ).grid(pady=(10, 25), column=0, row=0)

        frame_contenido=Frame(ventana, bg=blanco)
        frame_contenido.grid(column=0, row=1, padx=20, pady=10,rowspan=4,columnspan=4)
        ventana_insc.mostrar_cursos(frame_contenido,legajo,ventana)
    
    def dar_de_baja(self, id_inscripcion, ventana_detalle, datos_alumno):
        service=Alumno_Service()
        inactivo=service.es_inactivo(id_inscripcion)
        if inactivo:
            messagebox.showerror("Error","Esta alumno no esta activo en este curso",parent=ventana_detalle)
            return
        valor=messagebox.askokcancel("Confirmacion","¿Estas seguro que quieres dar de baja al alumno?",parent=ventana_detalle)
        if valor==True:
            service=Inscripcion_Service()
            service.dar_de_baja_alumno(id_inscripcion)
            ventana_detalle.destroy()
            self.detalle_alumno(datos_actualizacion_ventana=datos_alumno)
        
    def ver_notas(self, id_inscripcion):
        notas=Nota_Service().obtener_notas_inscripcion(id_inscripcion)
        ventana_notas = Toplevel(self._contenido)
        ventana_notas.title("Notas del alumno")
        ventana_notas.geometry("700x350")
        ventana_notas.maxsize(700,350)
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
                text="Este alumno no tiene notas registradas en este curso.",
                font=("Arial", 12),
                bg=blanco,
                fg=gris
            ).grid(pady=30, column=0, row=1)
            return 

        columnas = ["Fecha", "Descripcion", "Nota"]
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
    
    def ver_asistencias(self, inscripcion):
        asistencia=Asistencia_Service().asistencia_por_inscripcion(inscripcion)
        ventana_asistencias = Toplevel(self._contenido)
        ventana_asistencias.title("Asistencia en el Curso")
        ventana_asistencias.geometry("450x350")
        ventana_asistencias.maxsize(450,350)
        ventana_asistencias.configure(bg=blanco)
    
        if asistencia =="Sin Datos":
            Label(
                ventana_asistencias,
                text="Este alumno no tiene asistencias registradas.",
                font=("Arial", 12),
                bg=blanco,
                fg=gris
            ).grid(pady=30, column=0, row=1)
            return 

        columnas = ["Fecha","Estado"]

        tabla_inasistencias = treeview(ventana_asistencias, columnas, asistencia)
        
        
        Button(
            ventana_asistencias,
            text="Cerrar",
            font=("Arial", 11, "bold"),
            bg=gris,
            fg=blanco,
            padx=20,
            pady=10,
            command=ventana_asistencias.destroy
        ).grid(pady=15, column=0, row=2)
   
    
        
    def ventana_modificar_alumno(self,datos_alumno,ventana_vieja):
        ventana_vieja.destroy()
        ventana = Toplevel(self._contenido)
        ventana.title("Modificar alumno")
        ventana.geometry("600x600")
        ventana.configure(bg=blanco)
        form_frame = Frame(ventana, bg="white", highlightbackground=azul, highlightthickness=1, padx=40, pady=30)
        form_frame.pack(expand=True, pady=20)
        Label(
            form_frame,
            text="Modificar alumno",
            font=("Arial", 20, "bold")
            
        ).grid(pady=(10, 25), column=0, row=0)

        #cargo las variabkes con los datos
        id_alumno = datos_alumno[0] #sin el intvar porque no lo modifico
        nombre = StringVar(value=datos_alumno[1])
        apellido = StringVar(value=datos_alumno[2])
        dni = StringVar(value=datos_alumno[3])
        telefono = StringVar(value=datos_alumno[4])
        email = StringVar(value=datos_alumno[5])
        nacimiento = datos_alumno[6]

        #campos 
        Label(form_frame, text="Nombre", font=("Arial", 12, "bold")).grid(column=0, row=1)
        Entry(form_frame, font=("Arial", 12), textvariable=nombre, highlightbackground=azul_oscuro, highlightthickness=1).grid(pady=(5, 15), column=1, row=1, columnspan=2)

        Label(form_frame, text="Apellido", font=("Arial", 12, "bold")).grid(column=0, row=2)
        Entry(form_frame, font=("Arial", 12), textvariable=apellido, highlightbackground=azul_oscuro, highlightthickness=1).grid(pady=(5, 15), column=1, row=2, columnspan=2)

        Label(form_frame, text="DNI", font=("Arial", 12, "bold")).grid(column=0, row=3)
        Entry(form_frame, font=("Arial", 12), textvariable=dni, highlightbackground=azul_oscuro, highlightthickness=1).grid(pady=(5, 15), column=1, row=3, columnspan=2)

        Label(form_frame, text="Email", font=("Arial", 12, "bold")).grid(column=0, row=4)
        Entry(form_frame, font=("Arial", 12), textvariable=email, highlightbackground=azul_oscuro, highlightthickness=1).grid(pady=(5, 25), column=1, row=4, columnspan=2)

        Label(form_frame, text="Telefono", font=("Arial", 12, "bold")).grid(column=0, row=5)
        Entry(form_frame, font=("Arial", 12), textvariable=telefono, highlightbackground=azul_oscuro, highlightthickness=1).grid(pady=(5, 25), column=1, row=5, columnspan=2)

        Button(
            form_frame,
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
            form_frame,
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
        resultado=servicio_alumno.modificar_alumno(alumno_actualizado)
        if resultado==True:
            messagebox.showinfo("Éxito", "Alumno modificado correctamente.", parent=ventana)
            ventana.destroy()
        else:
            messagebox.showerror("Error", resultado, parent=ventana)
    
                
    def mostrar(self):
        
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
            "Consultar alumnos",
            "Inscribir a un Curso"
        ]
        fila=0
        for opcion in opciones:
            
            crear_boton(opcion,fila,self._botones,lambda opcion_actual=opcion: self.mostrar_opcion_elegida(opcion_actual)) #lambda para que no se me ejecuten las funciones 
            fila+=1 #opcion_actual congela la variable y la guarda, si no, se ejecuta siempre la ultima opcion
    
        


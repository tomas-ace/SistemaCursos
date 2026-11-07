from tkinter import *
from Presentacion.elementos import *
from Dominio.clase import *
from Servicios.clase_service import *
from Dominio.asistencia import *
from Servicios.asistencia_service import *
from Dominio.nota import *
from Servicios.notas_service import *
from tkinter import messagebox
from datetime import datetime
from Servicios.curso_service import *


class Ventana_Clases():
        def __init__(self,contenido):
                    self._contenido = contenido
                    self._botones = Frame(contenido, bg=blanco)
        def mostrar_opcion_elegida(self,opcion):
            if opcion == "Registrar nueva clase":
                self.ventana_registro_clase(None)
            else:
                self.lista_de_clases()
       
                    
                    
        def lista_de_clases(self, contenedor=None,filtro_actual="Todas"):
            if contenedor is None:
                ventana_lista = Toplevel(self._contenido)
            else:
                ventana_lista = contenedor
                for elemento in contenedor.winfo_children():
                    elemento.destroy()
                    
            ventana_lista.geometry("1200x600")
            Label(
                    ventana_lista,
                    text="Lista de clases",
                    font=("Arial", 20, "bold"),
                    bg=blanco,
                    fg=texto
                ).grid(pady=(10, 25), column=0, row=0)
            ventana_lista.title("Lista de clases")
            ventana_lista.configure(bg=blanco)
            columnas = ["IDClase", "Anio", "Turno", "Estado", "Curso"]
            frame_filtros=Frame(ventana_lista,bg=blanco)
            frame_filtros.grid(padx=5,row=1,column=0)
            opcion_filtro=StringVar(value=filtro_actual)
            Radiobutton(frame_filtros, text="Todas", variable=opcion_filtro, value="Todas", bg=blanco, font=("Arial", 10)).grid(padx=5,row=1,column=0)
            Radiobutton(frame_filtros, text="Activas", variable=opcion_filtro, value="Activa", bg=blanco, font=("Arial", 10)).grid(padx=5,row=1,column=1)
            Radiobutton(frame_filtros, text="Inactivas", variable=opcion_filtro, value="Inactiva", bg=blanco, font=("Arial", 10)).grid(padx=5,row=1,column=2)
            Button(frame_filtros,text="Aplicar Filtros",font=("Arial", 11, "bold"),bg=azul,fg=blanco,bd=0,padx=20,pady=10,command=lambda: self.lista_de_clases(contenedor=ventana_lista,filtro_actual=opcion_filtro.get())).grid(padx=5,row=1,column=3)
            frame_treeview=Frame(ventana_lista,bg=blanco)
            frame_treeview.grid(column=0,row=2)
            datos_clases = Clase_Service().listar_clases(filtro_actual)
            tree=treeview(frame_treeview, columnas, datos_clases)
            frame_acciones = Frame(ventana_lista, bg=blanco)
            frame_acciones.grid(column=0, row=3, padx=20, pady=10)

            Button(
                frame_acciones,
                text="Agregar Nuevo",
                font=("Arial", 11, "bold"),
                bg=azul,
                fg=blanco,
                bd=0,
                padx=20,
                pady=10,
                command=lambda: self.ventana_registro_clase(ventana_lista)
            ).pack(side="left", padx=10)
    
            Button(
                frame_acciones,
                text="Modificar Estado",
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
                command=lambda: self.detalle_clase(tree,ventana_lista)
            ).pack(side="left", padx=10)
            return tree
        
        def detalle_clase(self,tree,ventana):
                seleccion = tree.selection()
                if not seleccion:
                    print("Por favor, seleccione una clase de la tabla.")
                    return
                 
                item_id = seleccion[0]
                datos_clase = tree.item(item_id)['values']
                ventana.destroy()
                ventana_detalle = Toplevel(self._contenido)
                ventana_detalle.title("Detalle de la clase")
                ventana_detalle.geometry("600x600")
                ventana_detalle.configure(bg=blanco)
        
        
                Label(
                    ventana_detalle,
                    text="Detalle de la clase",
                    font=("Arial", 20, "bold"),
                    bg=blanco,
                    fg=texto
                ).pack(pady=(20, 20))
        
               
                frame_datos = Frame(ventana_detalle, bg=blanco)
                frame_datos.pack(pady=10)
                titulos_columnas = ["ID:", "Año:", "Turno:", "Estado:", "Curso"]
                for i in range(len(titulos_columnas)):
                    if i==0:
                        continue
                    titulo = titulos_columnas[i]
                    Label(
                        frame_datos,
                        text=titulo,
                        font=("Arial", 12, "bold"),
                        bg=blanco,
                        fg=texto,
                        width=18
                    ).grid(row=i, column=0, pady=8, padx=10)
        
                   
                    Label(
                        frame_datos,
                        text=str(datos_clase[i]),
                        font=("Arial", 12),
                        bg=blanco,
                        fg=gris,
                    ).grid(row=i, column=1, pady=8, padx=10)
        
                frame_datos_cursada = Frame(ventana_detalle, bg=blanco)
                frame_datos_cursada.pack(pady=40)
        
                Button(
                    frame_datos_cursada,
                    text="Presencias",
                    font=("Arial", 11, "bold"),
                    bg=azul,
                    fg=blanco,
                    bd=0,
                    padx=20,
                    pady=10,
                    command=lambda: self.lista_presencias(datos_clase[0])
                ).grid(column=0,row=0, padx=10)
        
                Button(
                    frame_datos_cursada,
                    text="Notas",
                    font=("Arial", 11, "bold"),
                    bg=azul,
                    fg=blanco,
                    bd=0,
                    padx=20,
                    pady=10,
                    command=lambda: self.lista_notas(datos_clase[0])
                ).grid(column=1,row=0, padx=10)
        
                Button(
                    frame_datos_cursada,
                    text="Tomar Lista",
                    font=("Arial", 11, "bold"),
                    bg=azul,
                    fg=blanco,
                    bd=0,
                    padx=20,
                    pady=10,
                    command=lambda: self.ventana_tomar_lista(datos_clase[0])
                ).grid(column=2,row=0, padx=10)
                
                        
                Button(
                    frame_datos_cursada,
                    text="Agregar Notas",
                    font=("Arial", 11, "bold"),
                    bg=azul,
                    fg=blanco,
                    bd=0,
                    padx=20,
                    pady=10,
                    command=lambda: self.ventana_agregar_notas(datos_clase[0])
                ).grid(column=3,row=0, padx=10)
                
                Button(
                        frame_datos_cursada,
                        text="Lista de Alumnos",
                        font=("Arial", 11, "bold"),
                        bg=azul,
                        fg=blanco,
                        bd=0,
                        padx=20,
                        pady=10,
                        command=lambda: self.ventana_lista_de_alumnos(datos_clase[0])
                    ).grid(column=4,row=0, padx=10)
                
                
        def ventana_lista_de_alumnos(self,id_clase,contenedor=None,filtro_actual="Todos"):
            if contenedor !=None:
                for elemento in contenedor.winfo_children():
                    elemento.destroy()
                ventana_asistencias=contenedor
            else:
                ventana_asistencias = Toplevel(self._contenido)
                ventana_asistencias.title("Lista de Alumnos")
                ventana_asistencias.geometry("600x400")
                
                
                ventana_asistencias.configure(bg="white") 
            
            Label(
                ventana_asistencias, 
                text="Lista de Alumnos", 
                font=("Arial", 16, "bold"), 
                bg="white"
            ).grid(pady=15,row=0,column=0)
            
            opcion_filtro=StringVar(value=filtro_actual)
            Radiobutton(ventana_asistencias, text="Todos", variable=opcion_filtro, value="Todos", bg=blanco, font=("Arial", 10)).grid(padx=5,row=1,column=0)
            Radiobutton(ventana_asistencias, text="En Curso", variable=opcion_filtro, value="En Curso", bg=blanco, font=("Arial", 10)).grid(padx=5,row=1,column=1)
            Radiobutton(ventana_asistencias, text="Libre", variable=opcion_filtro, value="Libre", bg=blanco, font=("Arial", 10)).grid(padx=5,row=1,column=2)
            Radiobutton(ventana_asistencias, text="Baja", variable=opcion_filtro, value="Baja", bg=blanco, font=("Arial", 10)).grid(padx=5,row=1,column=3)
            Radiobutton(ventana_asistencias, text="Aprobado", variable=opcion_filtro, value="Aprobado", bg=blanco, font=("Arial", 10)).grid(padx=5,row=1,column=4)
            Radiobutton(ventana_asistencias, text="Desaprobado", variable=opcion_filtro, value="Desaprobado", bg=blanco, font=("Arial", 10)).grid(padx=5,row=1,column=5)
            Button(ventana_asistencias,text="Aplicar Filtros",font=("Arial", 11, "bold"),bg=azul,fg=blanco,bd=0,padx=20,pady=10,command=lambda: self.ventana_lista_de_alumnos(id_clase,contenedor=ventana_asistencias,filtro_actual=opcion_filtro.get())).grid(padx=5,row=2,column=2,columnspan=2,pady=10)
            servicio_clase = Clase_Service()
            datos_clases = servicio_clase.lista_con_estado(id_clase,filtro_actual) 
            
            
            encabezados = ["Nombre","Apellido","Estado"]
            
            
            frame_tabla = Frame(ventana_asistencias)
            frame_tabla.grid(row=3,column=1,columnspan=6, padx=20, pady=10)
            treeview(frame_tabla, encabezados, datos_clases)
    
        def lista_presencias(self,id_clase):
            ventana_asistencias = Toplevel(self._contenido)
            ventana_asistencias.title(f"Asistencias - Clase {id_clase}")
            ventana_asistencias.geometry("1200x400")
            
            
            ventana_asistencias.configure(bg="white") 
            
            Label(
                ventana_asistencias, 
                text="Registro de Asistencias", 
                font=("Arial", 16, "bold"), 
                bg="white"
            ).pack(pady=15)
            
            servicio_asistencia = Asistencia_Service()
            
            
            datos_asistencias = servicio_asistencia.asistencia_por_clase(id_clase) 
            
           
            encabezados = ["IdInsc","Nombre","Apellido", "Fecha", "Estado"]
            
          
            frame_tabla = Frame(ventana_asistencias)
            frame_tabla.pack(fill="both", expand=True, padx=20, pady=10)
            
           
            tree=treeview(frame_tabla, encabezados, datos_asistencias)
            tree["displaycolumns"] = ("Nombre", "Apellido", "Fecha", "Estado")
            frame_boton=Frame(ventana_asistencias)
            frame_boton.pack(padx=20, pady=10)
            Button(
                    frame_boton, text="Editar Estado", bg=azul, fg=blanco, font=("Arial", 12, "bold"),
                    command=lambda: self.editar_asistencia(tree,ventana_asistencias,id_clase)
                ).pack(pady=20)
            
        def editar_asistencia(self,tree,ventana,id_clase):
            seleccion = tree.selection()
            if not seleccion:
                return
            
            item_id = seleccion[0]
            datos_clase = tree.item(item_id)['values']
            ventana.destroy()
            id_insc=datos_clase[0]
            fecha=datos_clase[3]
            estado=datos_clase[4]
            service=Asistencia_Service()
            service.editar_estado(id_insc,fecha,estado)
            self.lista_presencias(id_clase)
            
            
        def lista_notas(self,id_clase,contenedor=None):
            if contenedor is None:
                ventana_notas = Toplevel(self._contenido)
                ventana_notas.title(f"Notas - Clase {id_clase}")
                ventana_notas.geometry("1000x400")
                ventana_notas.configure(bg="white")
            else:
                ventana_notas = contenedor
                for elemento in ventana_notas.winfo_children():
                    elemento.destroy()
            Label(
                ventana_notas, 
                text="Registro de Notas", 
                font=("Arial", 16, "bold"), 
                bg="white"
            ).pack(pady=15)
        
            servicio_notas = Nota_Service()
            datos_notas = servicio_notas.notas_por_alumno(id_clase)
            encabezados = ["Id","Nombre","Apellido","Descripción", "Nota", "Fecha"]
            frame_tabla = Frame(ventana_notas)
            frame_tabla.pack(fill="both", expand=True, padx=20, pady=10)
            
     
            tree = treeview(frame_tabla, encabezados, datos_notas)
            tree["displaycolumns"] = ("Nombre", "Apellido", "Descripción", "Nota", "Fecha")
            frame_edicion = Frame(ventana_notas, bg="white")
            frame_edicion.pack(pady=10,anchor="w")
            Label(frame_edicion, text="Editar nota (seleccione nota para editar):", font=("Arial", 11, "bold"), bg="white").grid(row=0, column=0, padx=5)
            Label(frame_edicion, text="Nueva Nota:", font=("Arial", 11, "bold"), bg="white").grid(row=1, column=0, padx=5)

            entry_nota = Entry(frame_edicion, font=("Arial", 11), width=8)
            entry_nota.grid(row=1, column=1, padx=5)

            Button(
                frame_edicion, 
                text="Guardar Cambio", 
                font=("Arial", 10, "bold"), 
                bg=azul, 
                fg="white", 
                bd=0, 
                padx=15, 
                pady=5,
                command=lambda: self.guardar_edicion_nota(tree, entry_nota, id_clase, ventana_notas)
            ).grid(row=1, column=2, padx=10)
            
            Button(
                frame_edicion, 
                text="Agregar Notas", 
                font=("Arial", 10, "bold"), 
                bg=azul, 
                fg="white", 
                bd=0, 
                padx=15, 
                pady=5,
                command=lambda: self.ventana_agregar_notas(id_clase)
            ).grid(row=0, column=2, padx=10)
            
        def guardar_edicion_nota(self, tree, entry, id_clase, ventana):
            seleccion = tree.selection()
            
            if not seleccion:
                messagebox.showwarning("Atención", "Seleccione una nota de la tabla para editar.", parent=ventana)
                return
                
            nueva_nota_texto = entry.get()
            item_id = seleccion[0]
            datos_fila = tree.item(item_id)['values']
            id_nota = datos_fila[0] 
            servicio_notas = Nota_Service()
            resultado=servicio_notas.editar_nota(id_nota, nueva_nota_texto) 
            
            if resultado==True:
                messagebox.showinfo("Exito", "Nota modificada correctamente",parent=ventana)
            else:
                messagebox.showerror("Error", resultado,parent=ventana)
        
            self.lista_notas(id_clase, contenedor=ventana) 
                
        def ventana_agregar_notas(self, id_clase):
                    servicio_classe=Clase_Service()
                    alumnos=servicio_classe.lista_de_alumnos_por_clase(id_clase)
                    ventana = Toplevel(self._contenido)
                    ventana.title("Agregar Notas")
                    ventana.geometry("700x600")
                    ventana.configure(bg=blanco)
        
                    frame_fecha = Frame(ventana, bg=blanco)
                    frame_fecha.pack(pady=20)
                    
                    Label(frame_fecha, text="Día:", bg=blanco).grid(row=0, column=0)
                    entry_dia = Entry(frame_fecha, width=5)
                    entry_dia.grid(row=0, column=1, padx=10)
        
                    Label(frame_fecha, text="Mes:", bg=blanco).grid(row=0, column=2)
                    entry_mes = Entry(frame_fecha, width=10)
                    entry_mes.grid(row=0, column=3, padx=10)
                    
                    Label(frame_fecha, text="Año:", bg=blanco).grid(row=0, column=4)
                    entry_anio = Entry(frame_fecha, width=8)
                    entry_anio.grid(row=0, column=5, padx=10)
                    
                    Label(frame_fecha, text="Descripcion:", bg=blanco).grid(row=1, column=0)
                    entry_descripcion = Entry(frame_fecha, width=12)
                    entry_descripcion.grid(row=1, column=1, padx=10, columnspan=4)
        
                    lista_notas = [] 
        
                    frame_alumnos = Frame(ventana, bg=blanco)
                    frame_alumnos.pack(pady=10)
        
                    fila = 0
                    for alumno in alumnos:
                        nombre = f"{alumno[1]} {alumno[2]}"
                        id_inscripcion=alumno[3]
                        nota = StringVar(value="1") 
                        
                        lista_notas.append([id_inscripcion, nota])

                        Label(
                            frame_alumnos, text=nombre,bd=1, width=25,padx=10, pady=5
                        ).grid(row=fila, column=0, pady=5, padx=20)
        
                        Entry(frame_alumnos, textvariable=nota).grid(row=fila, column=1)
                        
                        fila += 1 
        
                    Button(
                        ventana, text="Guardar Nota", bg=azul, fg=blanco, font=("Arial", 12, "bold"),
                        command=lambda: self.guardar_notas(entry_descripcion.get(),entry_dia.get(), entry_mes.get(), entry_anio.get(), ventana,lista_notas)
                    ).pack(pady=20)
        
        
        def guardar_notas(self,descripcion, dia, mes, anio, ventana,lista):
                    print ("entre a guardar notas")
                    fecha_completa = f"{anio}-{mes}-{dia}"
                    nota_detalle_service= Nota_Service()
                    todas_validas=True
                    for alumno in lista:
                        print(alumno)
                        id_inscripcion=alumno[0]
                        nota = alumno[1].get() 
                        nota_detalle=Nota(None,fecha_completa,nota,descripcion,id_inscripcion)
                        validacion=nota_detalle_service.datos_validos(nota_detalle)
                        if validacion != True:
                            messagebox.showerror("Error", validacion,parent=ventana)
                            todas_validas=False
                            break
                    if todas_validas:
                        for alumno in lista:
                            id_inscripcion=alumno[0]
                            nota = alumno[1].get() 
                            nota_detalle=Nota(None,fecha_completa,nota,descripcion,id_inscripcion)
                            nota_detalle_service.registrar_nota(nota_detalle)
                        messagebox.showinfo("Exito", "Notas registradas correctamente.",parent=ventana)
                        ventana.destroy()
                    
                        
                
        def ventana_tomar_lista(self, id_clase):
            servicio_classe=Clase_Service()
            fecha_actual = datetime.now().strftime("%Y-%m-%d")
            servicio_asistencia = Asistencia_Service()
            if servicio_asistencia.existe_asistencia(fecha_actual, id_clase):
                messagebox.showinfo("Información", "La asistencia para esta clase ya ha sido registrada hoy.")
                return
            alumnos=servicio_classe.lista_de_alumnos_por_clase(id_clase)
            ventana = Toplevel(self._contenido)
            ventana.title("Tomar Lista")
            ventana.geometry("700x600")
            ventana.configure(bg=blanco)

            

            lista_asistencia = [] 

            frame_alumnos = Frame(ventana, bg=blanco)
            frame_alumnos.pack(pady=10)

            fila = 0
            for alumno in alumnos:
                nombre = f"{alumno[1]} {alumno[2]}"
                id_inscripcion=alumno[3]
                presencia = StringVar(value="Ausente") 
                
                lista_asistencia.append([id_inscripcion, presencia])

                Label(
                    frame_alumnos, text=nombre, bg=blanco, bd=1, width=25, anchor="w", padx=10, pady=5
                ).grid(row=fila, column=0, pady=5, padx=20)

                Radiobutton(frame_alumnos, text="Presente", variable=presencia, value="Presente", bg=blanco).grid(row=fila, column=1)
                Radiobutton(frame_alumnos, text="Ausente", variable=presencia, value="Ausente", bg=blanco).grid(row=fila, column=2)
                
                fila += 1 

            Button(
                ventana, text="Guardar Asistencia", bg=azul, fg=blanco, font=("Arial", 12, "bold"),
                command=lambda: self.guardar_asistencia(fecha_actual, ventana,lista_asistencia,id_clase)
            ).pack(pady=20)


        def guardar_asistencia(self, fecha, ventana,lista,id_clase):
            asistencia_service= Asistencia_Service()
            quedo_alguno_libre=False
            for alumno in lista:
                print(alumno)
                id_inscripcion=alumno[0]
                estado = alumno[1].get() 
                asistencia=Asistencia(fecha,estado,id_inscripcion)
                
                resultado=asistencia_service.registrar_asistencia(asistencia)
                if resultado==True:
                    quedo_alguno_libre=True
            if quedo_alguno_libre:
                messagebox.showwarning("Atención", "Uno o mas alumnos han superado el límite de inasistencias y su estado cambió automáticamente a 'Libre'.")
            asistencia_service.registrar_libres(fecha,id_clase)
            ventana.destroy()
                
        def preparar_modificacion(self,tree,ventana_lista):
            seleccion = tree.selection()
            if not seleccion:
                return
    
            item_id = seleccion[0]
            datos_clase = tree.item(item_id)['values']
            ventana_lista.destroy()  
            self.ventana_modificar_clase(datos_clase)
                    
        def ventana_modificar_clase(self,datos_clase):
                ventana = Toplevel(self._contenido)
                ventana.title("Modificar Estado")
                ventana.geometry("600x600")
                ventana.configure(bg=blanco)
                id_clase = datos_clase[0]
                print(datos_clase)
                estado_actual = datos_clase[3]
                Label(
                    ventana,
                    text="Modificar Estado",
                    font=("Arial", 20, "bold"),
                    bg=blanco,
                    fg=texto
                ).grid(pady=(10, 25), column=0, row=0)
        
        
                #campos 
                Label(ventana, text="Estado", font=("Arial", 12, "bold"), bg=blanco, fg=texto).grid(column=0, row=1)
                
                estado=StringVar(value=estado_actual)
                estado.set(estado_actual)
                Radiobutton(ventana, text="Activo", variable=estado, value="Activa", font=("Arial", 12), bg=blanco, fg=texto).grid(column=0, row=2)
                Radiobutton(ventana, text="Inactivo", variable=estado, value="Inactiva", font=("Arial", 12), bg=blanco, fg=texto).grid(column=0, row=3)
                
                
                Button(
                    ventana,
                    text="Guardar Cambios",
                    font=("Arial", 12),
                    bg=azul,
                    fg=blanco,
                    bd=0,
                    padx=20,
                    pady=12,
                    command=lambda: self.guardar_modificacion(id_clase,estado.get(),ventana)
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
        def guardar_modificacion(self, id_clase, estado, ventana):
                servicio_clase = Clase_Service()
                servicio_clase.modificar_estado_de_clase(id_clase, estado)
                ventana.destroy()         
        def mostrar(self):
            print("hola")
            Label(
                self._contenido,
                text="Clases",
                font=("Arial", 16, "bold"),
                bg=blanco,
                fg=texto
            ).grid(column=0, row=0, padx=20, pady=10)
    
            Label(
                self._contenido,
                text="Seleccione la opcion que desee.",
                font=("Arial", 11),
                bg=blanco,
                fg=gris
            ).grid(column=0, row=1, padx=20, pady=10)
    
            
            self._botones.grid(column=0, row=2, padx=20, pady=10)#coloca el contenedor y le dice que se ezpanda
            opciones = [
                "Registrar nueva clase",
                "Consultar clases" 
            ]
            fila = 0
            for opcion in opciones:
                    crear_boton(opcion,fila,self._botones,lambda opcion_actual=opcion: self.mostrar_opcion_elegida(opcion_actual))
                    fila += 1

        def ventana_registro_clase(self,ventana_none):
            from Presentacion.ventana_cursos import Ventana_Cursos
            if ventana_none == None:
                pass
            else:
                ventana_none.destroy()
            ventana = Toplevel(self._contenido)
    
            ventana.title("Registrar clase")
            ventana.geometry("600x600")
            ventana.configure(bg=blanco)
            Label(
                ventana,
                text="Registrar nueva clase",
                font=("Arial", 20, "bold"),
                bg=blanco,
                fg=texto
            ).grid(pady=(10, 25), column=0, row=0)
    
    
            #datoss
            
            
            turno = StringVar(value="Mañana")
            anio = StringVar(value="2026")
            
            
            Label(
                    ventana,
                    text="Año",
                    font=("Arial", 12, "bold"),
                    bg=blanco,
                    fg=texto
                ).grid(column=0, row=1)
            self._descripcion = Entry(
                ventana,
                font=("Arial", 12),
                textvariable=anio
            )
            self._descripcion.grid(pady=(5, 15), column=1, row=1,columnspan=2)
    
            Label(
                ventana,
                text="Turno",
                font=("Arial", 12, "bold"),
                bg=blanco,
                fg=texto
            ).grid(column=0, row=2)
    
            Radiobutton(ventana, text="Mañana", variable=turno, value="Mañana", font=("Arial", 12), bg=blanco, fg=texto).grid(column=1, row=2)
            Radiobutton(ventana, text="Tarde", variable=turno, value="Tarde", font=("Arial", 12), bg=blanco, fg=texto).grid(column=1, row=3)
            Radiobutton(ventana, text="Noche", variable=turno, value="Noche", font=("Arial", 12), bg=blanco, fg=texto).grid(column=1, row=4)

            frame_lista_cursos = Frame(ventana, bg=blanco)
            frame_lista_cursos.grid(column=0, row=5, padx=20, pady=10,rowspan=4,columnspan=4)
            lista_de_cursos=Ventana_Cursos(frame_lista_cursos)
            tree=lista_de_cursos.lista_de_cursos(frame_lista_cursos)
            
                        
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
                command=lambda: self.registrar(anio.get(), turno.get(), tree, ventana)
            ).grid(padx=(0, 10), column=0, row=11)
                
    
            Button(
                ventana,
                text="Cancelar",
                font=("Arial", 12),
                bg=gris,
                fg=blanco,
                bd=0,
                padx=30,
                pady=12,
                command=lambda: ventana.destroy()
            ).grid(padx=(0, 10), column=1, row=11)
            

        def registrar(self, anio, turno, tree, ventana):
            seleccion = tree.selection()
            if not seleccion:
                return
    
            item_id = seleccion[0]
            datos_curso = tree.item(item_id)['values']
            id_curso = datos_curso[0]
            print(id_curso, anio, turno)
            
            
            
            nueva_clase=Clase(None,anio,turno,"Activa",id_curso)
            servicio_clase=Clase_Service()
            resultado = servicio_clase.nueva_clase(nueva_clase)
            if resultado==True:
                messagebox.showinfo("Exito", "Curso registrado correctamente.", parent=ventana)
                ventana.destroy()
            else:
                messagebox.showerror("Error", resultado, parent=ventana)
                
        def vista_tarjetas_clases(self, contenedor=None, filtro_estado="Todas", filtro_curso="Todos los Cursos"):
            if contenedor is None:
                ventana_clases = Toplevel(self._contenido)
                ventana_clases.title("Gestión de Clases")
                ventana_clases.geometry("1100x700")
                ventana_clases.configure(bg=blanco)
            else:
                ventana_clases = contenedor
                for elemento in ventana_clases.winfo_children():
                    elemento.destroy()

            Label(ventana_clases, text="Gestión de Clases", font=("Arial", 20, "bold"), bg=blanco).pack(pady=(20, 10))

            frame_filtros = Frame(ventana_clases, bg=blanco)
            frame_filtros.pack(pady=10)

            opcion_estado = StringVar(value=filtro_estado)
            Radiobutton(frame_filtros, text="Todas", variable=opcion_estado, value="Todas", bg=blanco).grid(row=0, column=0, padx=5)
            Radiobutton(frame_filtros, text="Activas", variable=opcion_estado, value="Activa", bg=blanco).grid(row=0, column=1, padx=5)
            Radiobutton(frame_filtros, text="Inactivas", variable=opcion_estado, value="Inactiva", bg=blanco).grid(row=0, column=2, padx=10)

            Label(frame_filtros, text="Curso:", bg=blanco, font=("Arial", 10, "bold")).grid(row=0, column=3, padx=(10, 5))
            
            servicio_curso = Curso_Service() 
            nombres_cursos = ["Todos los Cursos"]
            lista_de_cursos = servicio_curso.listar_cursos()
            for curso in lista_de_cursos:
                nombre = curso[1]
                nombres_cursos.append(nombre)
            
            
            combo_cursos = ttk.Combobox(frame_filtros, values=nombres_cursos, state="readonly", width=30)
            combo_cursos.set(filtro_curso)
            combo_cursos.grid(row=0, column=4, padx=5)

            
            Button(
                frame_filtros, text="Aplicar Filtros", bg=azul, fg="white", font=("Arial", 10, "bold"), bd=0, padx=15, pady=5,
                command=lambda: self.vista_tarjetas_clases(ventana_clases, opcion_estado.get(), combo_cursos.get())
            ).grid(row=0, column=5, padx=15)

            Button(
                frame_filtros, text="Agregar Nueva Clase", bg=gris, fg="white", font=("Arial", 10, "bold"), bd=0, padx=15, pady=5,
                command=lambda: self.ventana_registro_clase(ventana_clases)
            ).grid(row=0, column=6, padx=5)

            frame_grid = Frame(ventana_clases, bg=blanco)
            frame_grid.pack(padx=20, pady=10, fill="both", expand=True)

            
            servicio_clases = Clase_Service()
            datos_clases = servicio_clases.obtener_clases_filtradas(filtro_estado, filtro_curso)

            if not datos_clases:
                Label(frame_grid, text="No se encontraron clases con estos filtros.", font=("Arial", 12, "italic"), bg=blanco, fg=gris).pack(pady=40)
                return

            columna_actual = 0
            fila_actual = 0
            max_columnas_por_fila = 7

            for clase in datos_clases:
                id_clase = clase[0]
                nombre_curso = clase[1]
                turno = clase[2]
                anio = clase[3]
                estado = clase[4]
                cant_alumnos = clase[5]

                
                card = Frame(frame_grid, bg="white", highlightbackground="black", highlightthickness=2, padx=15, pady=15)
                card.grid(row=fila_actual, column=columna_actual, padx=15, pady=15, sticky="nsew")

                Label(card, text=nombre_curso, font=("Arial", 14, "bold"), bg="white", wraplength=220).pack(anchor="w", pady=(0, 5))
                Frame(card, height=2, bg="black").pack(fill="x", pady=(0, 10))

                Label(card, text=f"ID Clase: {id_clase}", font=("Arial", 11), bg="white").pack(anchor="w")
                Label(card, text=f"Año: {anio} | Turno: {turno}", font=("Arial", 11), bg="white").pack(anchor="w")
                Label(card, text=f"Estado: {estado}", font=("Arial", 11, "italic"), bg="white", fg=gris).pack(anchor="w", pady=(5, 5))
                
                Label(card, text=f"Alumnos Activos: {cant_alumnos}", font=("Arial", 11, "bold"), bg="white").pack(anchor="w", pady=(0, 15))

                frame_botones_card = Frame(card, bg="white")
                frame_botones_card.pack(fill="x", side="bottom")

                Button(frame_botones_card, text="Notas", font=("Arial", 9, "bold"), bg=azul, fg="white", bd=0, padx=15, command=lambda id_c=id_clase: self.lista_notas(id_c)).grid(row=0,column=0,padx=5)
                Button(frame_botones_card, text="Asistencias", font=("Arial", 9, "bold"), bg=azul, fg="white", bd=0, padx=15, command=lambda id_c=id_clase: self.lista_presencias(id_c)).grid(row=0,column=1,padx=5)
                Button(frame_botones_card, text="Cambiar a Inactiva", font=("Arial", 9, "bold"), bg="red", fg="white", bd=0, padx=10, command=lambda id_c=id_clase: self.modificar_estado(id_c)).grid(row=1,column=0, columnspan=2,pady=5)

                columna_actual += 1
                if columna_actual >= max_columnas_por_fila:
                    columna_actual = 0
                    fila_actual += 1
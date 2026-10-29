from tkinter import *
from Presentacion.treeview import *
from Dominio.clase import *
from Servicios.clase_service import *
from Dominio.asistencia import *
from Servicios.asistencia_service import *
from Dominio.nota import *
from Servicios.notas_service import *

# Colores
azul = "#2864e8"
azul_oscuro = "#093068"
blanco = "#ffffff"
gris = "#6b7280"
texto = "#111827"
borde = "#d1d5db"

class Ventana_Clases():
        def __init__(self,contenido):
                    self._contenido = contenido
                    self._botones = Frame(contenido, bg=blanco)
        def mostrar_opcion_elegida(self,opcion):
            if opcion == "Registrar nueva clase":
                self.ventana_registro_clase(None)
            else:
                self.lista_de_clases()
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
                    ).grid(column=2, row=fila, padx=10, pady=10)
                    
                    
        def lista_de_clases(self, contenedor=None):
            if contenedor is None:
                ventana_lista = Toplevel(self._contenido)
                ventana_lista.title("Lista de clases")
                ventana_lista.geometry("600x600")
                ventana_lista.configure(bg=blanco)
                Label(
                    ventana_lista,
                    text="Lista de clases",
                    font=("Arial", 20, "bold"),
                    bg=blanco,
                    fg=texto
                ).grid(pady=(10, 25), column=0, row=0)
            else:
                ventana_lista = contenedor
            columnas = ["IDClase", "Anio", "Turno", "Estado", "Curso"]
            datos_clases = Clase_Service().listar_clases()
            tree=treeview(ventana_lista, columnas, datos_clases)
            frame_acciones = Frame(ventana_lista, bg=blanco)
            frame_acciones.grid(column=0, row=2, padx=20, pady=10)

            if contenedor is None:
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
                        anchor="e",
                        width=18
                    ).grid(row=i, column=0, pady=8, padx=10, sticky="e")
        
                   
                    Label(
                        frame_datos,
                        text=str(datos_clase[i]),
                        font=("Arial", 12),
                        bg=blanco,
                        fg=gris,
                        anchor="w"
                    ).grid(row=i, column=1, pady=8, padx=10, sticky="w")
        
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
                
        def lista_presencias(self,id_clase):
            ventana_asistencias = Toplevel(self._contenido)
            ventana_asistencias.title(f"Asistencias - Clase {id_clase}")
            ventana_asistencias.geometry("600x400")
            
            
            ventana_asistencias.configure(bg="white") 
            
            Label(
                ventana_asistencias, 
                text="Registro de Asistencias", 
                font=("Arial", 16, "bold"), 
                bg="white"
            ).pack(pady=15)
            
            servicio_asistencia = Asistencia_Service()
            
            
            datos_asistencias = servicio_asistencia.asistencia_por_alumno(id_clase) 
            
           
            encabezados = ["Alumno", "Fecha", "Estado"]
            
          
            frame_tabla = Frame(ventana_asistencias)
            frame_tabla.pack(fill="both", expand=True, padx=20, pady=10)
            
           
            treeview(frame_tabla, encabezados, datos_asistencias)
        def lista_notas(self,id_clase):
            ventana_notas = Toplevel(self._contenido)
            ventana_notas.title(f"Notas - Clase {id_clase}")
            ventana_notas.geometry("600x400")
            ventana_notas.configure(bg="white")
            
            Label(
                ventana_notas, 
                text="Registro de Notas", 
                font=("Arial", 16, "bold"), 
                bg="white"
            ).pack(pady=15)
        
            servicio_notas = Nota_Service()
            

            datos_notas = servicio_notas.notas_por_alumno(id_clase)
            
    
            encabezados = ["Alumno", "Descripción", "Nota", "Fecha"]
            
           
            frame_tabla = Frame(ventana_notas)
            frame_tabla.pack(fill="both", expand=True, padx=20, pady=10)
            
     
            treeview(frame_tabla, encabezados, datos_notas)
                
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
                        nota = IntVar(value=1) 
                        
                        lista_notas.append([id_inscripcion, nota])

                        Label(
                            frame_alumnos, text=nombre, bg=blanco, relief="solid", bd=1, width=25, anchor="w", padx=10, pady=5
                        ).grid(row=fila, column=0, pady=5, padx=20)
        
                        Entry(frame_alumnos, textvariable=nota, bg=blanco).grid(row=fila, column=1)
                        
                        fila += 1 
        
                    Button(
                        ventana, text="Guardar Nota", bg=azul, fg=blanco, font=("Arial", 12, "bold"),
                        command=lambda: self.guardar_notas(entry_descripcion.get(),entry_dia.get(), entry_mes.get(), entry_anio.get(), ventana,lista_notas)
                    ).pack(pady=20)
        
        
        def guardar_notas(self,descripcion, dia, mes, anio, ventana,lista):
                    fecha_completa = f"{anio}-{mes}-{dia}"
                    for alumno in lista:
                        print(alumno)
                        id_inscripcion=alumno[0]
                        nota = alumno[1].get() 
                        nota_detalle=Nota(None,fecha_completa,nota,descripcion,id_inscripcion)
                        nota_detalle_service= Nota_Service()
                        nota_detalle_service.registrar_nota(nota_detalle)
        
                        
                    ventana.destroy()
                
        def ventana_tomar_lista(self, id_clase):
            servicio_classe=Clase_Service()
            alumnos=servicio_classe.lista_de_alumnos_por_clase(id_clase)
            ventana = Toplevel(self._contenido)
            ventana.title("Tomar Lista")
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
                    frame_alumnos, text=nombre, bg=blanco, relief="solid", bd=1, width=25, anchor="w", padx=10, pady=5
                ).grid(row=fila, column=0, pady=5, padx=20)

                Radiobutton(frame_alumnos, text="Presente", variable=presencia, value="Presente", bg=blanco).grid(row=fila, column=1)
                Radiobutton(frame_alumnos, text="Ausente", variable=presencia, value="Ausente", bg=blanco).grid(row=fila, column=2)
                
                fila += 1 

            Button(
                ventana, text="Guardar Asistencia", bg=azul, fg=blanco, font=("Arial", 12, "bold"),
                command=lambda: self.guardar_asistencia(entry_dia.get(), entry_mes.get(), entry_anio.get(), ventana,lista_asistencia)
            ).pack(pady=20)


        def guardar_asistencia(self, dia, mes, anio, ventana,lista):
            fecha_completa = f"{anio}-{mes}-{dia}"
            for alumno in lista:
                print(alumno)
                id_inscripcion=alumno[0]
                estado = alumno[1].get() 
                asistencia=Asistencia(fecha_completa,estado,id_inscripcion)
                asistencia_service= Asistencia_Service()
                asistencia_service.registrar_asistencia(asistencia)

                
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
                    self.crear_boton(opcion,fila)
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
            
            
            turno = StringVar()
            anio = IntVar()
            
            
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
                command=lambda: self.cancelar(ventana)
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
            servicio_clase.nueva_clase(nueva_clase)
            ventana.destroy()
from tkinter import *
from Presentacion.treeview import *
from Dominio.clase import *
from Servicios.clase_service import *

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
            return tree
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
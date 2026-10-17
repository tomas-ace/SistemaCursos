import sqlite3

class Curso_DAO():
    def __init__(self,curso):
        self._curso=curso
    def registrar_curso(self):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        datos=[
            self._curso.get_descripcion(),
            self._duracion.get_duracion()
        ]
        cursor.execute("""
            INSERT INTO Curso
            (Descripcion, Duracion)   
            VALUES (?,?)   
        """,datos)
        
        conexion.commit()
        conexion.close()
    def obtener_curso(self,nombre):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
           SELECT * FROM Curso where descripcion=? 
        """,(nombre,))
    def modificar_curso(self,curso_con_nuevos_datos):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        nuevosDatos=[
            curso_con_nuevos_datos.get_descripcion(),
            curso_con_nuevos_datos.get_duracion(),
            curso_con_nuevos_datos.get_id()        
        ]
        
        cursor.execute("""
            UPDATE Curso
            SET Descripcion = ?, Duracion = ?
            WHERE id= ?
        """,nuevosDatos)
    def dar_de_baja_curso(self):
        pass
    

import sqlite3

class Curso_DAO():
    def __init__(self):
        pass
    def registrar_curso(self,curso):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        datos=[
            curso.get_descripcion(),
            curso.get_duracion()
        ]
        cursor.execute("""
            INSERT INTO Curso
            (Descripcion, Duracion)   
            VALUES (?,?)   
        """,datos)
        
        conexion.commit()
        conexion.close()
    def obtener_curso_por_nombre(self,nombre):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
           SELECT * FROM Curso where descripcion=? 
        """,(nombre,))
        curso = cursor.fetchone()
        conexion.close()
        return curso
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
            WHERE idCurso= ?
        """,nuevosDatos)
        conexion.commit()    
        conexion.close()
    def dar_de_baja_curso(self):
        pass
    def obtener_curso_por_id(self,id):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
           SELECT * FROM Curso where id=? 
        """,(id,))
        curso = cursor.fetchone()
        conexion.close()
        return curso
    def contar_cursos(self):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
           SELECT COUNT(*) FROM Curso
        """)
        curso = cursor.fetchone()
        conexion.commit()
        conexion.close()
        return curso[0]
    def listar_cursos(self):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT idCurso, Descripcion, Duracion
            FROM Curso
        """)
        cursos = cursor.fetchall()
        conexion.commit()
        conexion.close()
        return cursos
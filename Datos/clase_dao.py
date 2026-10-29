import sqlite3
class Clase_DAO():
    def __init__(self):
        pass
    def registrar_clase(self,clase):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        datos=[
            clase.get_año(),
            clase.get_turno(),
            clase.get_estado(),
            clase.get_id_curso()
        ]
        cursor.execute("""
            insert into Clase
            (Anio, Turno, Estado, IdCurso)
            VALUES (?, ?, ?, ?)
            """,datos)
        
        conexion.commit()
        conexion.close()
    def obtener_clase_por_id(self,id):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT * FROM Clase WHERE IdClase = ?
        """,(id,))
        clase = cursor.fetchone()
        conexion.close()
        return clase
    def modificar_estado(self,id_clase, nuevo_estado):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        nuevosDatos=[
            nuevo_estado,
            id_clase
            
        ]
        cursor.execute("""
            UPDATE Clase
            SET Estado = ?
            WHERE IdClase = ?
        """,nuevosDatos)
        
        conexion.commit()
        conexion.close()
    def contar_clases_activas(self):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT COUNT(*) FROM Clase WHERE Estado = "Activa"
        """)
        clases = cursor.fetchone()
        conexion.commit()
        conexion.close()
        return clases[0]
    
    def listar_clases(self):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT c.IdClase,c.Anio,c.Turno,c.Estado, Cu.Descripcion
            FROM Clase c
            JOIN Curso cu ON c.IdCurso = cu.IdCurso
        """)
        clases = cursor.fetchall()
        conexion.commit()
        conexion.close()
        return clases
    
    def lista_de_alumnos_en_clase(self,clase):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT a.Legajo, a.Nombre, a.Apellido, i.IdInscripcion
            FROM Alumno a
                JOIN Inscripcion i ON a.Legajo = i.Legajo
                JOIN Clase c ON i.IdClase = c.IdClase 
                WHERE c.IdClase = ?;
                """,(clase,))
        alumnos=cursor.fetchall()
        conexion.commit()
        conexion.close()
        return alumnos
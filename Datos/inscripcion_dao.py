import sqlite3

class Inscripcion_DAO():
    def __init__(self):
        pass
    def registrar_inscripcion(self, inscripcion):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        datos=[
            inscripcion.get_fecha(),
            inscripcion.get_estado(),
            inscripcion.get_legajo(),
            inscripcion.get_id_clase()
        ]
        cursor.execute("""
            INSERT INTO Inscripcion
            (Fecha_Inscripcion, Estado, Legajo, IdClase)
            VALUES (?, ?, ?, ?)
        """,datos)
        
        conexion.commit()
        conexion.close()
    
    def modificar_estado(self,id_inscripcion, nuevo_estado):
            conexion=sqlite3.connect("Datos/cursos_db.db")
            cursor = conexion.cursor()
            
            nuevosDatos=[
                nuevo_estado,
                id_inscripcion
                
            ]
            cursor.execute("""
                UPDATE Inscripcion
                SET Estado = ?
                WHERE IdInscripcion = ?
            """,nuevosDatos)
            
            conexion.commit()
            conexion.close()
    def obtener_inscripcion_por_id(self,id):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT * FROM Inscripcion WHERE Id = ?
        """,(id,))
        inscripcion = cursor.fetchone()
        conexion.close()
        return inscripcion
    def contar_inscripciones_activas(self):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT COUNT(*) FROM Inscripcion WHERE Estado = "En Curso"
        """)
        inscripciones = cursor.fetchone()
        conexion.commit()
        conexion.close()
        return inscripciones[0]

    def listar_inscripciones(self):
            conexion=sqlite3.connect("Datos/cursos_db.db")
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT i.IdInscripcion, i.Fecha_Inscripcion, i.Estado, a.Nombre, a.Apellido, c.Descripcion, cl.Anio, cl.Turno
                FROM Inscripcion i
                JOIN Alumno a ON i.Legajo = a.Legajo
                JOIN Clase cl ON i.IdClase = cl.IdClase
                JOIN Curso c ON cl.IdCurso = c.IdCurso
            """)
            inscripciones = cursor.fetchall()
            conexion.commit()
            conexion.close()
            return inscripciones

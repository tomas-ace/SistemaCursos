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
        
    def ya_esta_inscripto(self,legajo, id_curso, anio):
            conexion = sqlite3.connect("Datos/cursos_db.db")
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT COUNT(*) 
                FROM Inscripcion i
                JOIN Clase cl ON i.IdClase = cl.IdClase
                WHERE i.Legajo = ? AND cl.IdCurso = ? AND cl.Anio = ?
            """, (legajo, id_curso, anio))
            cantidad = cursor.fetchone()[0]
            conexion.close()
            return cantidad>0
        
    def contar_inscripciones_de_alumno_activas(self, legajo):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT COUNT(*) 
            FROM Inscripcion i
            JOIN Clase cl ON i.IdClase = cl.IdClase
            WHERE i.Legajo = ? AND cl.Estado = 'Activa' AND i.Estado = 'En Curso'
        """, (legajo, ))
        cantidad = cursor.fetchone()[0]
        conexion.close()
        return cantidad


    def cantidad_alumnos_por_clase(self, id_clase):
            conexion = sqlite3.connect("Datos/cursos_db.db")
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT COUNT(*) FROM Inscripcion
                WHERE IdClase = ?
            """, (id_clase,))
            cantidad = cursor.fetchone()[0]
            conexion.close()
            return cantidad
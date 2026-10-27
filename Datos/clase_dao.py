import sqlite3
class Clase_DAO():
    def __init__(self,clase):
        self._clase=clase
    def registrar_clase(self):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        datos=[
            self._clase.get_año(),
            self._clase.get_turno(),
            self._clase.get_estado(),
            self._clase.get_id_curso()
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
    def modificar_clase(self,asistencia_con_nuevos_datos):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        nuevosDatos=[
            asistencia_con_nuevos_datos.get_anio(),
            asistencia_con_nuevos_datos.get_turno(),
            asistencia_con_nuevos_datos.get_estado(),
            asistencia_con_nuevos_datos.get_id_curso(),
            asistencia_con_nuevos_datos.get_id()
        ]
        cursor.execute("""
            UPDATE Clase
            SET Anio = ?, Turno = ?, Estado = ?, IdCurso = ?
            WHERE IdClase = ?
        """,nuevosDatos)
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
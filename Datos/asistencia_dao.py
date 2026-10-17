import sqlite3
class Asistencia_DAO():
    def __init__(self,asistencia):
        self._asistencia=asistencia
    def registrar_asistencia(self):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        datos = [
            self._asistencia.get_id_inscripcion(),
            self._asistencia.get_fecha(),
            self._asistencia.get_estado()
        ]
        cursor.execute("""
            INSERT INTO Asistencia
            (Fecha, IdInscripcion, Estado)
            VALUES (?, ?, ?)
        """, datos)
        
        conexion.commit()
        conexion.close()
    def obtener_asistencia_por_fecha_y_alumno(self,fecha,alumno):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT * FROM Asistencia WHERE Fecha = ? AND IdInscripcion = ?
        """, (fecha,alumno))
        asistencia = cursor.fetchone()
        conexion.close()
        return asistencia 
    def modificar_asistencia(self,asistencia_con_nuevos_datos):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        nuevosDatos = [
            asistencia_con_nuevos_datos.get_id_inscripcion(),
            asistencia_con_nuevos_datos.get_fecha(),
            asistencia_con_nuevos_datos.get_estado()
        ]
        cursor.execute("""
            UPDATE Asistencia
            SET Fecha = ?, IdInscripcion = ?, Estado = ?
            WHERE IdInscripcion = ?
        """, nuevosDatos)
    def obtener_asistencia_por_id(self,id):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT * FROM Asistencia WHERE Id = ?
        """, (id,))
        asistencia = cursor.fetchone()
        conexion.close()
        return asistencia
  
import sqlite3
class Asistencia_DAO():
    def __init__(self):
        pass
    def registrar_asistencia(self,asistencia):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        datos = [
            asistencia.get_fecha(),
            asistencia.get_id_inscripcion(),
            asistencia.get_estado()
        ]
        cursor.execute("""
            INSERT INTO Asistencia
            (Fecha, IdInscripcion, Estado)
            VALUES (?, ?, ?)
        """, datos)
        
        conexion.commit()
        conexion.close()
    def modificar_asistencia(self,asistencia_con_nuevos_datos):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        nuevosDatos = [
            asistencia_con_nuevos_datos.get_estado(),
            asistencia_con_nuevos_datos.get_id_inscripcion(),  
            asistencia_con_nuevos_datos.get_fecha()]
        cursor.execute("""
            UPDATE Asistencia
            SET Estado = ?
            WHERE IdInscripcion = ? and Fecha = ?
        """, nuevosDatos)
        conexion.commit()
        conexion.close()
    
    
    def obtener_asistencias_por_clase(self, id_clase):
            conexion = sqlite3.connect("Datos/cursos_db.db")
            cursor = conexion.cursor()
            cursor.execute("""
                    SELECT al.Nombre, al.Apellido, a.Fecha, a.Estado
                    FROM Asistencia a 
                    join Inscripcion i on i.IdInscripcion =  a.IdInscripcion
                    join Alumno al on i.Legajo = al.Legajo
                    WHERE i.IdClase = ?
                """, (id_clase,))
            datos = cursor.fetchall()
            conexion.close()
            return datos
  
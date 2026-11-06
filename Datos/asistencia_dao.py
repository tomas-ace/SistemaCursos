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
  
    def existe_asistencia_para_fecha_y_clase(self, fecha, id_clase):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT COUNT(*) 
            FROM Asistencia a
            JOIN Inscripcion i ON a.IdInscripcion = i.IdInscripcion
            WHERE a.Fecha = ? AND i.IdClase = ?
        """, (fecha, id_clase))
        resultado = cursor.fetchone()[0]
        conexion.close()
        return resultado > 0
    
    def cantidad_presencias(self, id_inscripcion):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM Asistencia WHERE idInscripcion = ? AND estado = 'Presente'", (id_inscripcion,))
        presentes = cursor.fetchone()[0]
        conexion.close()
        return presentes
    
    def cantidad_ausencias(self,id_inscripcion):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM Asistencia WHERE idInscripcion = ? AND estado = 'Ausente'", (id_inscripcion,))
        ausencias = cursor.fetchone()[0]
        conexion.close()
        return ausencias
    
    def obtener_asistencia_por_inscripcion(self,inscripcion):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT Fecha, Estado FROM Asistencia WHERE idInscripcion = ?" ,  (inscripcion,))
        asistencia = cursor.fetchall()
        print("en la consulta", asistencia)
        if not asistencia:
                conexion.close()
                return "Sin Datos"
        conexion.close()
        return asistencia
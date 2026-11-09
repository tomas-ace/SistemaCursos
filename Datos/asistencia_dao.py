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
    
    
    
    def obtener_asistencias_por_clase(self, id_clase):
            conexion = sqlite3.connect("Datos/cursos_db.db")
            cursor = conexion.cursor()
            cursor.execute("""
                    SELECT a.IdInscripcion,al.Nombre, al.Apellido, a.Fecha, a.Estado
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
    
    def cambiar_estado_a_libre(self, id_inscripcion):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Inscripcion 
            SET Estado = 'Libre' 
            WHERE IdInscripcion = ?
        """, (id_inscripcion,))
        conexion.commit()
        conexion.close()
        
    def obtener_duracion_para_inscripcion(self,id_inscripcion):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        cursor.execute("""
            SELECT c.Duracion 
            FROM Inscripcion i
            JOIN Clase cl ON i.IdClase = cl.IdClase
            JOIN Curso c ON cl.IdCurso = c.IdCurso
            WHERE i.IdInscripcion = ?
        """, (id_inscripcion,))
        
        resultado = cursor.fetchone()
        conexion.close()
        
        if resultado is None:
            return 0
            
        return resultado[0]
    
    def obtener_faltas_actuales(self,id_inscripcion):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT COUNT(*) 
            FROM Asistencia 
            WHERE IdInscripcion = ? AND Estado = 'Ausente'
        """, (id_inscripcion,))
        
        faltas = cursor.fetchone()[0]
        conexion.close()
        
        return faltas
    def alumnos_libres_sin_asistencia(self,id_clase,fecha):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT IdInscripcion 
            FROM Inscripcion 
            WHERE Estado = 'Libre' AND IdClase = ?
              AND IdInscripcion NOT IN (
                  SELECT IdInscripcion FROM Asistencia WHERE Fecha = ?
              )
        """, (id_clase, fecha))
        
        resultados = cursor.fetchall()
        conexion.close()
        
        return resultados
  
    def editar_asistencia(self, id_inscripcion, fecha, nuevo_estado):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Asistencia
            SET Estado = ?
            WHERE IdInscripcion = ? AND Fecha = ?
        """, (nuevo_estado, id_inscripcion, fecha))
        
        conexion.commit()
        conexion.close()
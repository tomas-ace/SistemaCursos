import sqlite3

class Alumno_DAO():
    def __init__(self):
        pass
    def registrar_alumno(self,alumno):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()

        datos = [
            alumno.get_nombre(),
            alumno.get_apellido(),
            alumno.get_fecha_nacimiento(),
            alumno.get_dni(),
            alumno.get_telefono(),
            alumno.get_mail()
        ]

        cursor.execute("""
            INSERT INTO Alumno
            (Nombre, Apellido, Fecha_Nac, DNI, Telefono, Email)
            VALUES (?, ?, ?, ?, ?, ?)
        """, datos)

        conexion.commit()
        conexion.close()
    def obtener_alumno_por_dni(self,dni):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT * FROM Alumno WHERE DNI = ?
        """, (dni,))
        alumno = cursor.fetchone()
        conexion.close()
        return alumno
    def modificar_alumno(self,alumno_con_nuevos_datos):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        nuevosDatos = [
            alumno_con_nuevos_datos.get_nombre(),
            alumno_con_nuevos_datos.get_apellido(),
            alumno_con_nuevos_datos.get_fecha_nacimiento(),
            alumno_con_nuevos_datos.get_dni(),
            alumno_con_nuevos_datos.get_telefono(),
            alumno_con_nuevos_datos.get_mail(),
            alumno_con_nuevos_datos.get_legajo()
        ]
        cursor.execute("""
            UPDATE Alumno
            SET Nombre = ?, Apellido = ?, Fecha_Nac = ?, DNI = ?, Telefono = ?, Email = ?
            WHERE Legajo = ?
        """, nuevosDatos)
        
        conexion.commit()
        conexion.close()
    
    def obtener_alumno_por_legajo(self,legajo):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT * FROM Alumno WHERE legajo = ?
        """, (legajo,))
        alumno = cursor.fetchone()
        conexion.close()    
        return alumno
    def contar_alumnos(self):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT COUNT(*) FROM Alumno
        """)
        alumnos = cursor.fetchone()
        conexion.close()
        return alumnos[0]
    
    def listar_alumnos(self):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT Legajo, Nombre, Apellido, DNI, Telefono, Email, Fecha_Nac
            FROM Alumno
        """)
        alumnos = cursor.fetchall()
        conexion.close()
        return alumnos

    def obtener_cursos_por_alumno(self, alumno_id):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT c.Descripcion,c.Duracion ,cl.Turno,cl.Anio, i.Fecha_Inscripcion, i.Estado
            FROM Curso c
            JOIN Clase cl ON cl.IdCurso = c.IdCurso
            JOIN Inscripcion i ON i.IdClase = cl.IdClase
            WHERE i.Legajo = ?
        """, (alumno_id,))
        cursos = cursor.fetchall()
        conexion.close()
        return cursos
    def obtener_notas_por_alumno(self, alumno_id):
            conexion = sqlite3.connect("Datos/cursos_db.db")
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT n.Fecha, n.Descripcion, c.Descripcion, cl.Anio, n.Nota
                FROM Nota n
                JOIN Inscripcion i ON i.IdInscripcion = n.IdInscripcion
                JOIN Clase cl ON cl.IdClase = i.IdClase
                JOIN Curso c ON c.IdCurso = cl.IdCurso
                WHERE i.Legajo = ?
            """, (alumno_id,))
            notas = cursor.fetchall()
            conexion.close()
            return notas
    def obtener_inasistencias_por_alumno(self, alumno_id):
                conexion = sqlite3.connect("Datos/cursos_db.db")
                cursor = conexion.cursor()
                cursor.execute("""
                    SELECT c.Descripcion, cl.Anio, a.Fecha
                    FROM Asistencia a
                    JOIN Inscripcion i ON i.IdInscripcion = a.IdInscripcion
                    JOIN Clase cl ON cl.IdClase = i.IdClase
                    JOIN Curso c ON c.IdCurso = cl.IdCurso
                    WHERE i.Legajo = ? and a.Estado='Ausente'
                """, (alumno_id,))
                inasistencias = cursor.fetchall()
                conexion.close()
                return inasistencias

                

print(Alumno_DAO().obtener_cursos_por_alumno(2))
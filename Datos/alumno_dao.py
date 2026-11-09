import sqlite3

class Alumno_DAO():
    def __init__(self):
        pass
    def registrar_alumno(self,alumno):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()

        datos = [
            alumno.get_nombre().strip(),
            alumno.get_apellido().strip(),
            alumno.get_fecha_nacimiento(),
            alumno.get_dni(),
            alumno.get_telefono(),
            alumno.get_mail().strip()
        ]

        cursor.execute("""
            INSERT INTO Alumno
            (Nombre, Apellido, Fecha_Nac, DNI, Telefono, Email)
            VALUES (?, ?, ?, ?, ?, ?)
        """, datos)

        conexion.commit()
        conexion.close()
   
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
            SELECT i.IdInscripcion, cl.IdClase, c.Descripcion, cl.Anio, cl.Turno, i.Estado
            FROM Curso c
            JOIN Clase cl ON cl.IdCurso = c.IdCurso
            JOIN Inscripcion i ON i.IdClase = cl.IdClase
            WHERE i.Legajo = ?
        """, (alumno_id,))
        cursos = cursor.fetchall()
        conexion.close()
        return cursos
    
        

    def existe_dni(self, dni):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        cursor.execute("SELECT Legajo FROM Alumno WHERE Dni = ?", (dni,))
        resultado = cursor.fetchone()
        conexion.close()
        
        return resultado != None
    def existe_dni_en_otro_alumno(self, dni, legajo):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        cursor.execute("SELECT Legajo FROM Alumno WHERE Dni = ? AND Legajo != ?", (dni, legajo))
        resultado = cursor.fetchone()
        conexion.close()
        
        return resultado != None

    def listar_nombre_y_apellido(self):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT a.Legajo, a.Nombre, a.Apellido
            FROM Alumno a
            LEFT JOIN Inscripcion i ON a.Legajo = i.Legajo AND i.Estado = 'En Curso'
            GROUP BY a.Legajo, a.Nombre, a.Apellido
            HAVING COUNT(i.IdInscripcion) <= 2;
        """)
        alumnos = cursor.fetchall()
        conexion.close()
        return alumnos

    def obtener_cantidad_insc_activas(self,legajo):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT COUNT(*) 
            FROM Inscripcion 
            WHERE Legajo = ? AND Estado = 'En Curso'
        """, (legajo,))
        
        resultado = cursor.fetchone()
        conexion.close()
                    
        return resultado[0]
    
    def estado_de_inscripcion(self,id_inscripcion):
            conexion = sqlite3.connect("Datos/cursos_db.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT Estado FROM Inscripcion WHERE IdInscripcion = ?", (id_inscripcion,))
            resultado = cursor.fetchone()
            conexion.close() 
            return resultado[0]
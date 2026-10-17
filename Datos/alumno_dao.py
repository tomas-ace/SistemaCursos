import sqlite3

class Alumno_DAO():
    def __init__(self,alumno):
        self._alumno=alumno
    def registrar_alumno(self):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()

        datos = [
            self._alumno.get_nombre(),
            self._alumno.get_apellido(),
            self._alumno.get_fecha_nacimiento(),
            self._alumno.get_dni(),
            self._alumno.get_telefono(),
            self._alumno.get_mail()
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
    
    def obtener_alumno_por_id(self,id):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT * FROM Alumno WHERE Id = ?
        """, (id,))
        alumno = cursor.fetchone()
        conexion.close()    
        return alumno

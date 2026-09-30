import sqlite3

class Alumno_DAO():
    def __init__(self,alumno):
        self._alumno=alumno
    def registrar_alumno(self,alumno):
        conexion = sqlite3.connect("SistemaCursos.db")
        cursor = conexion.cursor()

        datos = [
            alumno.nombre,
            alumno.apellido,
            alumno.fechaNacimiento,
            alumno.dni,
            alumno.nacionalidad,
            alumno.telefono,
            alumno.email
        ]

        cursor.execute("""
            INSERT INTO Alumno
            (Nombre, Apellido, FechaNacimiento, DNI, Nacionalidad, Telefono, Email)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, datos)

        conexion.commit()
        conexion.close()
    def modificar_alumno(self,nuevosDatos):
        pass
    def dar_de_baja_alumno(self):
        pass
    def datos_alumno(self):
        pass
    
    
    
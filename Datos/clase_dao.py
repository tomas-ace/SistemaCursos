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
            SELECT * FROM Clase WHERE Id = ?
        """,(id,))
        clase = cursor.fetchone()
        conexion.close()
        return clase
    def modificar_clase(self,nuevosDatos):
        pass
    def dar_de_baja_clase(self):
        pass
    def datos_clase(self):
        pass
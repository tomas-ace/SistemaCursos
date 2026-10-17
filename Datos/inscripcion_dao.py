import sqlite3

class Inscripcion_DAO():
    def __init__(self,inscripcion):
        self._inscripcion=inscripcion
    def registrar_inscripcion(self):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        datos=[
            self._inscripcion.get_fecha(),
            self._inscripcion.get_estado(),
            self._inscripcion.get_legajo(),
            self._inscripcion.get_id_clase()
        ]
        cursor.execute("""
            INSERT INTO Inscripcion
            (Fecha_Inscripcion, Estado, Legajo, IdClase)
            VALUES (?, ?, ?, ?)
        """,datos)
        
        conexion.commit()
        conexion.close()
    def modificar_inscripcion(self,nuevosDatos):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        nuevosDatos=[
            self._inscripcion.get_fecha(),
            self._inscripcion.get_estado(),
            self._inscripcion.get_legajo(),
            self._inscripcion.get_id_clase(),
            self._inscripcion.get_id()
        ]
        cursor.execute("""
            UPDATE Inscripcion
            SET Fecha_Inscripcion = ?, Estado = ?, Legajo = ?, IdClase = ?
            WHERE Id = ?
        """,nuevosDatos)
        
        conexion.commit()
        conexion.close()
    def obtener_inscripcion_por_id(self,id):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT * FROM Inscripcion WHERE Id = ?
        """,(id,))
        inscripcion = cursor.fetchone()
        conexion.close()
        return inscripcion
    
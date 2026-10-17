import sqlite3
class Nota_DAO():
    def __init__(self,nota):
        self._nota=nota
    def registrar_nota(self):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        datos=[
            self._nota.get_fecha(),
            self._nota.get_estado(),
            self._nota.get_nota(),
            self._nota.get_descripcion()
        ]
        cursor.execute("""
            INSERT INTO Nota
            (Fecha, Estado, Nota, Descripcion)
            VALUES (?, ?, ?, ?)
        """,datos)
        
        conexion.commit()
        conexion.close()
    def modificar_nota(self,nuevosDatos):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        nuevosDatos=[
            self._nota.get_id_inscripcion(),
            self._nota.get_fecha(),
            self._nota.get_estado(),
            self._nota.get_id_clase(),
            self._nota.get_nota()
        ]
        cursor.execute("""
            UPDATE Nota
            SET Fecha = ?, Estado = ?, IdClase = ?, Nota = ?
            WHERE Id = ?
        """,nuevosDatos)
        
        conexion.commit()
        conexion.close()
 
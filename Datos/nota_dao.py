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
            self._nota.get_id_inscripcion()
        ]
        cursor.execute("""
            INSERT INTO Nota
            (Fecha, Nota, Descripcion, idInscripcion)
            VALUES (?, ?, ?, ?)
        """,datos)
        
        conexion.commit()
        conexion.close()
    def modificar_nota(self,nota_con_nuevos_datos):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        nuevosDatos=[
            nota_con_nuevos_datos.get_fecha(),
            nota_con_nuevos_datos.get_IdInscripcion(),
            nota_con_nuevos_datos.get_nota(),
            nota_con_nuevos_datos.get_descripcion(),
            nota_con_nuevos_datos.get_id()
        ]
        cursor.execute("""
            UPDATE Nota
            SET Fecha = ?, Estado = ?, IdInscripcion = ?, Nota = ?, Descripcion = ?
            WHERE IdNota = ?
        """,nuevosDatos)
        
        conexion.commit()
        conexion.close()
 
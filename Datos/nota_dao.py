import sqlite3
class Nota_DAO():
    def __init__(self):
        pass
    def registrar_nota(self,nota):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        datos=[
            nota.get_fecha(),
            nota.get_nota(),
            nota.get_descripcion(),
            nota.get_id_inscripcion()
        ]
        cursor.execute("""
            INSERT INTO Nota
            (Fecha, Nota, Descripcion, idInscripcion)
            VALUES (?, ?, ?, ?)
        """,datos)
        
        conexion.commit()
        conexion.close()
    def modificar_nota(self,id_nota,nueva_nota):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        cursor.execute("""
            UPDATE Nota
            SET Nota = ?
            WHERE IdNota = ?
        """,(nueva_nota,id_nota))
        
        conexion.commit()
        conexion.close()
    def obtener_notas_por_clase(self, id_clase):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
                SELECT n.IdNota,a.Nombre,a.Apellido, n.Descripcion, n.Nota ,n.Fecha
                FROM Nota n
                join Inscripcion i on n.IdInscripcion=i.IdInscripcion
                join Alumno a on a.Legajo=I.legajo
                where i.IdClase = ?
            """, (id_clase,))
        datos = cursor.fetchall()
        conexion.close()
        return datos
 
    def obtener_promedio_alumno_por_clase(self,id_inscripcion):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
                SELECT AVG(Nota)
                FROM Nota n
                WHERE IdInscripcion = ? AND n.Nota != 1
            """, (id_inscripcion,))
        promedio = cursor.fetchone()[0]
        conexion.close()
        return promedio
    
    def notas_inscripcion(self,id_inscripcion):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
                SELECT Fecha, Descripcion, Nota 
                FROM Nota
                WHERE idInscripcion = ? 
            """, (id_inscripcion,))
        notas = cursor.fetchall()
        if notas is None:
            conexion.close()
            return "Sin notas"
        conexion.close()
        return notas
       

import sqlite3
class Clase_DAO():
    def __init__(self):
        pass
    def registrar_clase(self,clase):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        datos=[
            clase.get_año(),
            clase.get_turno(),
            clase.get_estado(),
            clase.get_id_curso()
        ]
        cursor.execute("""
            insert into Clase
            (Anio, Turno, Estado, IdCurso)
            VALUES (?, ?, ?, ?)
            """,datos)
        
        conexion.commit()
        conexion.close()
    
    def modificar_estado(self,id_clase, nuevo_estado):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        nuevosDatos=[
            nuevo_estado,
            id_clase
            
        ]
        cursor.execute("""
            UPDATE Clase
            SET Estado = ?
            WHERE IdClase = ?
        """,nuevosDatos)
        
        conexion.commit()
        conexion.close()
    def contar_clases_activas(self):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT COUNT(*) FROM Clase WHERE Estado = "Activa"
        """)
        clases = cursor.fetchone()
        conexion.commit()
        conexion.close()
        return clases[0]
    
    def listar_clases(self):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT c.IdClase,c.Anio,c.Turno,c.Estado, Cu.Descripcion
            FROM Clase c
            JOIN Curso cu ON c.IdCurso = cu.IdCurso
        """)
        clases = cursor.fetchall()
        conexion.commit()
        conexion.close()
        return clases
    
    def listar_clases_con_filtro(self,filtro):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT c.IdClase,c.Anio,c.Turno,c.Estado, Cu.Descripcion
            FROM Clase c
            JOIN Curso cu ON c.IdCurso = cu.IdCurso
            where c.Estado= ?
        """,(filtro,))
        clases = cursor.fetchall()
        conexion.commit()
        conexion.close()
        return clases
    
    def lista_de_alumnos_en_clase(self,clase):
        conexion=sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT a.Legajo, a.Nombre, a.Apellido, i.IdInscripcion
            FROM Alumno a
                JOIN Inscripcion i ON a.Legajo = i.Legajo
                JOIN Clase c ON i.IdClase = c.IdClase 
                WHERE c.IdClase = ? and i.Estado = "En Curso";
                """,(clase,))
        alumnos=cursor.fetchall()
        conexion.commit()
        conexion.close()
        return alumnos
    
    def lista_de_alumnos_con_estado(self,clase):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        cursor.execute("""
            SELECT a.Nombre, a.Apellido, i.Estado
            FROM Alumno a
            JOIN Inscripcion i ON a.Legajo = i.Legajo
            WHERE i.IdClase = ?
        """, (clase,)) 
        
        resultados = cursor.fetchall()
        conexion.close()
        
        return resultados
    def lista_de_alumnos_con_estado_y_filtro(self,clase,filtro):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        
        cursor.execute("""
            SELECT a.Nombre, a.Apellido, i.Estado
            FROM Alumno a
            JOIN Inscripcion i ON a.Legajo = i.Legajo
            WHERE i.IdClase = ? and i.Estado= ?
        """, (clase,filtro)) 
        
        resultados = cursor.fetchall()
        
        conexion.close()
        return resultados 
    
    def listar_por_descripcion_y_turno(self):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT c.IdClase,cu.Descripcion, c.Turno
            FROM Clase c
            JOIN Curso cu ON c.IdCurso = cu.IdCurso
            where c.estado="Activa"
        """)
        clases = cursor.fetchall()
        conexion.close()
        return clases
    
    def contar_clase_por_curso_y_anio(self, id_curso, anio):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT COUNT(*) FROM Clase
            WHERE IdCurso = ? AND Anio = ?
        """, (id_curso, anio))
        cantidad = cursor.fetchone()[0]
        conexion.close()
        return cantidad
    def anio_de_clase(self, id_clase):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        print("antes de la consulta el id es ", id_clase)
        cursor.execute("""
            SELECT Anio FROM Clase
            WHERE IdClase = ?
        """, (id_clase,))
        
        anio = cursor.fetchone()[0]
        print("el anio es ", anio)
        conexion.close()
        return anio
    def curso_de_clase(self, id_clase):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT IdCurso FROM Clase
            WHERE IdClase = ?
        """, (id_clase,))
        id_curso = cursor.fetchone()[0]
        conexion.close()
        return id_curso
    def listar_todas_las_clases(self):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT c.IdClase, cu.Descripcion, c.Turno, c.Anio, c.Estado,
                   (SELECT COUNT(*) FROM Inscripcion i WHERE i.IdClase = c.IdClase AND i.Estado = 'En Curso') as Cant_Alumnos
            FROM Clase c
            JOIN Curso cu ON c.IdCurso = cu.IdCurso
        """)
        clases = cursor.fetchall()
        conexion.close()
        return clases
    
    def listar_clases_por_curso(self, nombre_curso):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT c.IdClase, cu.Descripcion, c.Turno, c.Anio, c.Estado,
                   (SELECT COUNT(*) FROM Inscripcion i WHERE i.IdClase = c.IdClase AND i.Estado = 'En Curso') as Cant_Alumnos
            FROM Clase c
            JOIN Curso cu ON c.IdCurso = cu.IdCurso
            WHERE cu.Descripcion = ?
        """, (nombre_curso,))
        clases = cursor.fetchall()
        conexion.close()
        return clases
    
    def listar_clases_por_estado(self, estado):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT c.IdClase, cu.Descripcion, c.Turno, c.Anio, c.Estado,
                   (SELECT COUNT(*) FROM Inscripcion i WHERE i.IdClase = c.IdClase AND i.Estado = 'En Curso') as Cant_Alumnos
            FROM Clase c
            JOIN Curso cu ON c.IdCurso = cu.IdCurso
            WHERE c.Estado = ?
        """, (estado,))
        clases = cursor.fetchall()
        conexion.close()
        return clases
    
    def listar_clases_por_estado_y_curso(self, estado, nombre_curso):
        conexion = sqlite3.connect("Datos/cursos_db.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT c.IdClase, cu.Descripcion, c.Turno, c.Anio, c.Estado,
                   (SELECT COUNT(*) FROM Inscripcion i WHERE i.IdClase = c.IdClase AND i.Estado = 'En Curso') as Cant_Alumnos
            FROM Clase c
            JOIN Curso cu ON c.IdCurso = cu.IdCurso
            WHERE c.Estado = ? AND cu.Descripcion = ?
        """, (estado, nombre_curso))
        clases = cursor.fetchall()
        conexion.close()
        return clases
    
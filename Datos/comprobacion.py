
import sqlite3

conexion = sqlite3.connect("Datos/cursos_db.db")

cursor = conexion.cursor()

#cursor.execute("""
#    INSERT INTO Alumno (Nombre, Apellido, Fecha_Nac, DNI, Telefono, Email)
#    VALUES
#    ('Juan', 'Perez', '2002-05-14', '42123456', '1123456789', 'juan.perez@gmail.com');
#""")

cursor.execute("""
     INSERT INTO Alumno (Nombre, Apellido, Fecha_Nac, DNI, Telefono, Email)
     VALUES
     ('Juan', 'Perez', '2002-05-14', '42113456', '231656', 'juan.perez@gmail.com');
 """)



#tablas = cursor.fetchall()
#print(tablas)
#for tabla in tablas:
#    print(tabla[0])
conexion.commit()
conexion.close()
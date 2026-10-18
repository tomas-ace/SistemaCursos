from Dominio.alumno import Alumno
from Datos.alumno_dao import Alumno_DAO

#PRUEBA REGISTRAR ALUMNO (CAMBIAR DATOS PORQUE YA ESTAN REPETIDOS)
# alumno = Alumno(None,"Juan","Perez","2002-05-14","1235","21221","juanz@gmail.com")
# alumno_dao = Alumno_DAO(alumno)
# alumno_dao.registrar_alumno()

#PRUEBA OBTENER ALUMNO POR DNI Y MODIFICARLO
# dao=Alumno_DAO(alumno=None)
# dni_a_probar=1235
# alumno_encontrado = dao.obtener_alumno_por_dni(dni_a_probar)
# print(alumno_encontrado)

# nuevosDatos = Alumno(alumno_encontrado[0],alumno_encontrado[1],alumno_encontrado[2],alumno_encontrado[3],alumno_encontrado[4],"1234",alumno_encontrado[6])
# dao.modificar_alumno(nuevosDatos)

# print(dao.obtener_alumno_por_dni(dni_a_probar))


# hola={
#     "hola":"21313",
#     "1321":"jjvkuvu",
#     "-lnl":"1321"
# }

# print(hola.items())
# for nombre, boton in hola.items():
#     print(nombre)
#     print(boton)
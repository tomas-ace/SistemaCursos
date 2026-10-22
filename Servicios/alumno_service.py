from Datos.alumno_dao import Alumno_DAO
class Alumno_Service():
    def __init__(self):
        self._dao=Alumno_DAO()
        
    def nuevo_alumno(self,alumno):
        self._dao.registrar_alumno(alumno)
    
    def cantidad_de_alumnos(self):
        return self._dao.contar_alumnos()

    def listar_alumnos(self):
        return self._dao.listar_alumnos()

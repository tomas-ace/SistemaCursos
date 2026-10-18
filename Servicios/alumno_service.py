from Datos.alumno_dao import Alumno_DAO
class Alumno_Service():
    def __init__(self):
        self._dao=Alumno_DAO(None)
        
    def nuevo_alumno(self):
        pass
    
    def cantidad_de_alumnos(self):
        return self._dao.contar_alumnos()
    

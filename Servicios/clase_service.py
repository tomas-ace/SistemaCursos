from Datos.clase_dao import Clase_DAO
class Clase_Service():
    def __init__(self):
        self._dao=Clase_DAO(None)
        
    def nuevo_alumno(self):
        pass
    
    def cantidad_de_clases_activas(self):
        return self._dao.contar_clases_activas()
    

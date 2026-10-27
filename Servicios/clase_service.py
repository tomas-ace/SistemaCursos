from Datos.clase_dao import Clase_DAO
class Clase_Service():
    def __init__(self):
        self._dao=Clase_DAO(None)
        
    def listar_clases(self):
        return self._dao.listar_clases()
    
    def cantidad_de_clases_activas(self):
        return self._dao.contar_clases_activas()
    

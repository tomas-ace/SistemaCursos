from Datos.clase_dao import Clase_DAO
class Clase_Service():
    def __init__(self):
        self._dao=Clase_DAO()   
    
    def nueva_clase(self, clase):
        
        self._dao.registrar_clase(clase)
        
    def listar_clases(self):
        return self._dao.listar_clases()
    
    def cantidad_de_clases_activas(self):
        return self._dao.contar_clases_activas()
    
    def modificar_estado_de_clase(self, id_clase, nuevo_estado):
        self._dao.modificar_estado(id_clase, nuevo_estado)
    

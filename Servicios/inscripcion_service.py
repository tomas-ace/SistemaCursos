from Datos.inscripcion_dao import Inscripcion_DAO
class Inscripcion_Service():
    def __init__(self):
        self._dao=Inscripcion_DAO(None)
        
    def cantidad_de_inscripciones_activas(self):
        return self._dao.contar_inscripciones_activas() 
    
    def listar_inscripciones(self):
        return self._dao.listar_inscripciones()
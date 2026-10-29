from Datos.inscripcion_dao import Inscripcion_DAO
class Inscripcion_Service():
    def __init__(self):
        self._dao=Inscripcion_DAO()
        
    def cantidad_de_inscripciones_activas(self):
        return self._dao.contar_inscripciones_activas() 
    
    def listar_inscripciones(self):
        return self._dao.listar_inscripciones()
    
    def nueva_inscripcion(self, inscripcion):
        return self._dao.registrar_inscripcion(inscripcion)
    
    def modificar_estado_de_inscripcion(self, id_inscripcion, nuevo_estado):
        return self._dao.modificar_estado(id_inscripcion, nuevo_estado)
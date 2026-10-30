from Datos.asistencia_dao import *
class Asistencia_Service():
    def __init__(self):
        self._dao=Asistencia_DAO()
    def registrar_asistencia(self,asistencia):
        self._dao.registrar_asistencia(asistencia)
    def asistencia_por_clase(self,id_clase):
        return self._dao.obtener_asistencias_por_clase(id_clase)
from Datos.asistencia_dao import *
class Asistencia_Service():
    def __init__(self):
        self._dao=Asistencia_DAO()
    def registrar_asistencia(self,asistencia):
        self._dao.registrar_asistencia(asistencia)
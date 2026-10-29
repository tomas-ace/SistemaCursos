from Datos.asistencia_dao import *
class Asistencia_Service():
    def __init__(self):
        self._dao=Asistencia_DAO()
    def registrar_asistencia(self,asistencia):
        self._dao.registrar_asistencia(asistencia)
    def asistencia_por_alumno(self,id_inscripcion):
        self._dao.obtener_asistencias_por_inscripcion(id_inscripcion)
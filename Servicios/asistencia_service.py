from Datos.asistencia_dao import *
class Asistencia_Service():
    def __init__(self):
        self._dao=Asistencia_DAO()
    def registrar_asistencia(self,asistencia):
        self._dao.registrar_asistencia(asistencia)
    def asistencia_por_clase(self,id_clase):
        return self._dao.obtener_asistencias_por_clase(id_clase)
    
    def existe_asistencia(self, fecha, id_clase):
        return self._dao.existe_asistencia_para_fecha_y_clase(fecha, id_clase)
    
    def calcular_porcentaje_asistencia(self,id_inscripcion):
        ausencias=self._dao.cantidad_ausencias(id_inscripcion)
        presencias=self._dao.cantidad_presencias(id_inscripcion)
        if ausencias+presencias==0:
            return 0
        porcentaje = (presencias / (ausencias+presencias)) * 100
        return porcentaje
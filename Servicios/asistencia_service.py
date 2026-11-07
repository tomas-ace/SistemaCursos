from Datos.asistencia_dao import *
from Dominio.asistencia import *
class Asistencia_Service():
    def __init__(self):
        self._dao=Asistencia_DAO()
    def registrar_asistencia(self,asistencia):
        self._dao.registrar_asistencia(asistencia)
        
        return self.evaluar_condicion_libre(asistencia.get_id_inscripcion())
    
    def evaluar_condicion_libre(self, id_inscripcion):
            duracion = self._dao.obtener_duracion_para_inscripcion(id_inscripcion)
            faltas_actuales=self._dao.obtener_faltas_actuales(id_inscripcion)
            limite_ausencias = duracion * 0.3 
            if faltas_actuales > limite_ausencias:
                self._dao.cambiar_estado_a_libre(id_inscripcion)
                return True
                
            return False
        
    def registrar_libres(self,fecha,id_clase):
        libres_a_procesar = self._dao.alumnos_libres_sin_asistencia(id_clase, fecha)
        for inscripcion in libres_a_procesar:
            asistencia_libre = Asistencia(fecha, 'Ausente', inscripcion[0])
            self._dao.registrar_asistencia(asistencia_libre)
        
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
        return f"{porcentaje:.2f}"
    
    def asistencia_por_inscripcion(self,inscripcion):
        return self._dao.obtener_asistencia_por_inscripcion(inscripcion)
    
    def editar_estado(self,id_insc,fecha,estado):
        if estado=="Presente":
            self._dao.editar_asistencia(id_insc,fecha,"Ausente")
        else:
            self._dao.editar_asistencia(id_insc,fecha,"Presente")
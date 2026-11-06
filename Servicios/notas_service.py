from Datos.nota_dao import *
from Servicios.fechas_service import Fechas_Service
class Nota_Service():
    def __init__(self):
        self._dao=Nota_DAO()
    def registrar_nota(self,nota):
        resultado = self.datos_validos(nota)
        if resultado != True:
            return resultado
        else:
            self._dao.registrar_nota(nota)
            return True
        
    def datos_validos(self,nota):
        fecha_valida = Fechas_Service().validar_fecha(nota.get_fecha(), "Nota")
        if nota.get_nota().isdigit():
            nota_entero = int(nota.get_nota())
            nota.set_nota(nota_entero)
        else:            
            return "La nota debe ser un número, si el alumno no asistio, ingrese 1."
        
        if nota.get_nota() < 1 or nota.get_nota() > 10:
            return "La nota debe estar entre 1 y 10."
        if nota.get_descripcion() == "":
            return "El campo Descripción no puede estar vacío."
        elif fecha_valida != True:
            return fecha_valida
        return True
        
    def notas_por_alumno(self,id_clase):
        return self._dao.obtener_notas_por_clase(id_clase)
    
    def promedio_alumno_en_clase(self, id_inscripcion):
        promedio= self._dao.obtener_promedio_alumno_por_clase(id_inscripcion)
        print("el promedio es ", promedio)
        if promedio == None:
            return "Sin notas"
        else:
            return f"{promedio:.2f}"
    def obtener_notas_inscripcion(self,id_inscripcion):
        return self._dao.notas_inscripcion(id_inscripcion)
from Datos.inscripcion_dao import Inscripcion_DAO
from Datos.clase_dao import Clase_DAO
class Inscripcion_Service():
    def __init__(self):
        self._dao=Inscripcion_DAO()
        
    def cantidad_de_inscripciones_activas(self):
        return self._dao.contar_inscripciones_activas() 
    
    def listar_inscripciones(self):
        return self._dao.listar_inscripciones()
    
    def nueva_inscripcion(self, inscripcion):
        print("el id del alumnoo es ", inscripcion.get_legajo())
        clase_dao = Clase_DAO()
        anio = clase_dao.anio_de_clase(inscripcion.get_id_clase())
        print("el anio de la clase es ", anio)
        curso= clase_dao.curso_de_clase(inscripcion.get_id_clase())
        print("el curso de la clase es ", curso)
        if self._dao.ya_esta_inscripto(inscripcion.get_legajo(), curso, anio):
            return "El alumno ya está inscripto en el curso para este año."
        elif self._dao.contar_inscripciones_de_alumno_activas(inscripcion.get_legajo()) >= 2:
            return "El alumno ya tiene 2 inscripciones este año."
        elif self._dao.cantidad_alumnos_por_clase(inscripcion.get_id_clase()) >= 20:
            return "La clase seleccionada ya tiene 20 alumnos inscriptos."
        else:
            self._dao.registrar_inscripcion(inscripcion)
            return True
        
        
    
    def modificar_estado_de_inscripcion(self, id_inscripcion, nuevo_estado):
        return self._dao.modificar_estado(id_inscripcion, nuevo_estado)
from Datos.clase_dao import Clase_DAO
from Servicios.notas_service import *
class Clase_Service():
    def __init__(self):
        self._dao=Clase_DAO()   
    
    def nueva_clase(self, clase):
        resultado = self.datos_validos(clase)
        if resultado != True:
            return resultado
        else:
            self._dao.registrar_clase(clase)
            return True
        
    def datos_validos(self, clase):
        if clase.get_año().isdigit():
                anio_entero = int(clase.get_año())
                clase.set_año(anio_entero)
        else:
            return "El año de la clase debe ser un número entero válido."
        
        if clase.get_año()=="" or clase.get_turno()=="":
            return "No se pueden dejar campos vacíos."
        elif clase.get_año() <= 2025:
            return "Ingrese un año válido para la clase."
        elif self._dao.contar_clase_por_curso_y_anio(clase.get_id_curso(), clase.get_año()) >= 3:
            return "Ya existen 3 clases para este curso en el año seleccionado."
        else:
            return True
        
    
        
    def listar_clases(self,filtro):
        if filtro=="Todas":
            return self._dao.listar_clases()
        else:
            return self._dao.listar_clases_con_filtro(filtro)
    
    def cantidad_de_clases_activas(self):
        return self._dao.contar_clases_activas()
    
    def modificar_estado_de_clase(self, id_clase, nuevo_estado):
        self._dao.modificar_estado(id_clase, nuevo_estado)
        
    def lista_de_alumnos_por_clase(self,clase):
        return self._dao.lista_de_alumnos_en_clase(clase)

    def listar_por_descripcion(self):
        return self._dao.listar_por_descripcion_y_turno()
    
    def lista_con_estado(self,clase,filtro):
        if filtro=="Todos":
            return self._dao.lista_de_alumnos_con_estado(clase)
        else:
            return self._dao.lista_de_alumnos_con_estado_y_filtro(clase, filtro)
    
    def listar_clases_con_filtros(filtro_estado,filtro_curso):
        pass
    
    def obtener_clases_filtradas(self, filtro_estado, filtro_curso):
        if filtro_estado == "Todas" and filtro_curso == "Todos los Cursos":
            return self._dao.listar_todas_las_clases()
            
        elif filtro_estado != "Todas" and filtro_curso == "Todos los Cursos":
            return self._dao.listar_clases_por_estado(filtro_estado)
            
        elif filtro_estado == "Todas" and filtro_curso != "Todos los Cursos":
            return self._dao.listar_clases_por_curso(filtro_curso)
            
        else:
            return self._dao.listar_clases_por_estado_y_curso(filtro_estado, filtro_curso)

        
    def cerrar_clase_y_evaluar(self, id_clase):
        self._dao.marcar_clase_inactiva(id_clase)
        inscripciones_a_evaluar = self._dao.obtener_alumnos_evaluables(id_clase)
        servicio_nota = Nota_Service()
        
        for id_inscripcion in inscripciones_a_evaluar:
            promedio = servicio_nota.promedio_alumno_en_clase(id_inscripcion[0])
            
            if promedio=="Sin notas":
                promedio=0
            promedio_int=float(promedio)    
            if promedio_int >= 7.0:
                nuevo_estado = "Aprobado"
            else:
                nuevo_estado = "Desaprobado"
            self._dao.actualizar_estado_inscripcion(id_inscripcion[0], nuevo_estado)
            
    def curso_finalizado(self,id_clase):
        duracion_total = self._dao.obtener_duracion_por_clase(id_clase)
        clases_dictadas = self._dao.obtener_cantidad_clases_dictadas(id_clase)
        
        return clases_dictadas >= duracion_total
            
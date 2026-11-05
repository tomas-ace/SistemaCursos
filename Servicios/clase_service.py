from Datos.clase_dao import Clase_DAO
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
        
    
        
    def listar_clases(self):
        return self._dao.listar_clases()
    
    def cantidad_de_clases_activas(self):
        return self._dao.contar_clases_activas()
    
    def modificar_estado_de_clase(self, id_clase, nuevo_estado):
        self._dao.modificar_estado(id_clase, nuevo_estado)
        
    def lista_de_alumnos_por_clase(self,clase):
        return self._dao.lista_de_alumnos_en_clase(clase)

    def listar_por_descripcion(self):
        return self._dao.listar_por_descripcion_y_turno()
    

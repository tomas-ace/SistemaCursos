from Datos.curso_dao import Curso_DAO
class Curso_Service():
    def __init__(self):
        self._dao=Curso_DAO()
    
    def nuevo_curso(self,curso):
        resultado = self.datos_validos(curso)
        if resultado != True:
            return resultado
        else:
            self._dao.registrar_curso(curso)
            return True
        
    def cantidad_de_cursos(self):
        return self._dao.contar_cursos()
    def listar_cursos(self):
        return self._dao.listar_cursos()
    def modificar_curso(self,curso):
        resultado = self.datos_validos(curso,modificar=True)
        if resultado != True:
            return resultado
        elif self._dao.existe_curso_en_otro_curso(curso.get_descripcion(), curso.get_id()):
            return "El curso ingresado ya existe en otro curso. Por favor, ingrese un curso válido."
        else:
            self._dao.modificar_curso(curso)
            return True
            
    def datos_validos(self, curso,modificar=False):
        if curso.get_duracion().isdigit():
                duracion_entero = int(curso.get_duracion())
                curso.set_duracion(duracion_entero)
        else:
            return "La duración del curso debe ser un número entero válido."
        if curso.get_descripcion()=="" or curso.get_descripcion().strip()=="":
            return "No se pueden dejar campos vacíos."
        elif curso.get_duracion() <= 0:
            return "La duración del curso debe ser un número positivo."
        elif self._dao.existe_curso(curso.get_descripcion()) and not modificar:
                return "El curso ya existe en el sistema."
        else:
            return True
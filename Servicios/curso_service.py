from Datos.curso_dao import Curso_DAO
class Curso_Service():
    def __init__(self):
        self._dao=Curso_DAO()
    
    def nuevo_curso(self,curso):
        self._dao.registrar_curso(curso)
    def cantidad_de_cursos(self):
        return self._dao.contar_cursos()
    def listar_cursos(self):
        return self._dao.listar_cursos()
    def modificar_curso(self,curso):
        self._dao.modificar_curso(curso)

from Datos.curso_dao import Curso_DAO
class Curso_Service():
    def __init__(self):
        self._dao=Curso_DAO(None)
    
    def cantidad_de_cursos(self):
        return self._dao.contar_cursos()
    

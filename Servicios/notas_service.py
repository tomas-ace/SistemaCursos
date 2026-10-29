from Datos.nota_dao import *
class Nota_Service():
    def __init__(self):
        self._dao=Nota_DAO()
    def registrar_nota(self,nota):
        self._dao.registrar_nota(nota)
        
    def notas_por_alumno(self,id_inscripcion):
        self._dao.obtener_notas_por_inscripcion(id_inscripcion)
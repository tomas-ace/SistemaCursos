from Datos.nota_dao import *
class Nota_Service():
    def __init__(self):
        self._dao=Nota_DAO()
    def registrar_nota(self,nota):
        self._dao.registrar_nota(nota)
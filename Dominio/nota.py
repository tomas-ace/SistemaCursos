class Nota():
    def __init__(self,id_nota,fecha,nota,id_inscripcion):
        self._id_nota=id_nota
        self._fecha=fecha
        self._nota=nota
        self._id_inscripcion=id_inscripcion
        
    def get_id(self):
        return self._id_nota
    def get_fecha(self):
            return self._fecha
    def get_nota(self):
            return self._nota
    def get_id_inscripcion(self):
            return self._id_inscripcion

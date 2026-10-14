class Inscripcion():
    def __init__(self,id_inscripcion,fecha,estado,legajo,id_clase):
        self._id_inscripcion=id_inscripcion
        self._fecha=fecha
        self._estado=estado
        self._legajo=legajo
        self._id_clase=id_clase
        
    def get_fecha(self):
        return self._fecha
    def get_id(self):
            return self._id_inscripcion
    def get_estado(self):
            return self._estado
    def get_legajo(self):
            return self._legajo
    def get_id_clase(self):
            return self._id_clase

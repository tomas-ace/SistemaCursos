class Asistencia():
    def __init__(self,fecha,estado,id_inscripcion):
        self._fecha=fecha
        self._estado=estado
        self._id_inscripcion=id_inscripcion
        
    def get_fecha(self):
        return self._fecha
    def get_estado(self):
        return self._estado
    def get_id(self):
        return self._id_inscripcion

class Clase():
    def __init__(self,id,año,turno,estado,id_curso):
        self._id_clase=id
        self._id_curso=id_curso
        self._año=año
        self._turno=turno
        self._estado=estado
        
    def get_id(self):
        return self._id_clase
    def get_id_curso(self):
        return self._id_curso
    def get_año(self):
        return self._año
    def get_turno(self):
        return self._turno
    def get_estado(self):
        return self._estado
    

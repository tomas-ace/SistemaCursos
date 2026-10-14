class Curso():
    def __init__(self,id,descripcion,duracion):
        self._id_curso=id
        self._descripcion=descripcion
        self._duracion=duracion
        
    def get_id(self):
        return self._id_curso
    def get_descripcion(self):
        return self._descripcion
    def get_duracion(self):
        return self._duracion

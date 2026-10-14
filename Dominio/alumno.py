class Alumno():
    def __init__(self,legajo,nombre,apellido,fecha_nacimiento,DNI,telefono,email):
        self._legajo=legajo
        self._nombre=nombre
        self._apellido=apellido
        self._nacimiento=fecha_nacimiento
        self._dni=DNI
        self._telefono=telefono
        self._mail=email
        
    def get_legajo(self):
        return self._legajo
    def get_nombre(self):
        return self._nombre
    def get_legajo(self):
        return self._legajo
    def get_apellido(self):
        return self._apellido
    def get_fecha_nacimiesnto(self):
        return self._nacimiento
    def get_dni(self):
        return self._dni
    def get_telefono(self):
        return self._telefono
    def get_mail(self):
        return self._mail

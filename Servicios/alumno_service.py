from Datos.alumno_dao import Alumno_DAO
from Servicios.fechas_service import Fechas_Service
class Alumno_Service():
    def __init__(self):
        self._dao=Alumno_DAO()
        
    def nuevo_alumno(self,alumno):
        print("DNI del alumno:", alumno.get_dni())  
        resultado = self.datos_validos(alumno)
        if resultado != True:
            return resultado
        else:
            self._dao.registrar_alumno(alumno)
            return True
    
    def cantidad_de_alumnos(self):
        return self._dao.contar_alumnos()

    def datos_validos(self, alumno):
        fecha_valida = Fechas_Service().validar_fecha(alumno.get_fecha_nacimiento(),"Nacimiento")
        if alumno.get_dni() == "":
            return "El campo DNI no puede estar vacío."
        elif self._dao.existe_dni(alumno.get_dni()):
            return "DNI ya existe en el sistema."
        elif not alumno.get_dni().isdigit() or (len(alumno.get_dni()) != 8 and len(alumno.get_dni()) != 7):
            return "El campo DNI debe contener solo números y tener 7 u 8 dígitos."
        elif alumno.get_nombre() == "":
            return "El campo Nombre no puede estar vacío."
        elif alumno.get_apellido() == "":
            return "El campo Apellido no puede estar vacío."
        elif not alumno.get_telefono().isdigit() or not (7 <= len(alumno.get_telefono()) <= 15):
            return "El campo Teléfono debe contener solo números y tener entre 7 y 15 dígitos."
        elif fecha_valida != True:
            return fecha_valida
        else:
            return True
    def listar_alumnos(self):
        return self._dao.listar_alumnos()
    
    def modificar_alumno(self,alumno):
        resultado = self.datos_validos(alumno)
        if not resultado:
                return resultado
        elif self._dao.existe_dni_en_otro_alumno(alumno.get_dni(), alumno.get_legajo()):
            return "El DNI ingresado ya existe en otro alumno. Por favor, ingrese un DNI válido."
        else:
            self._dao.modificar_alumno(alumno)
            return True
    def cursos_por_alumno(self, alumno_id):
        return self._dao.obtener_cursos_por_alumno(alumno_id)
    def notas_por_alumno(self, alumno_id):
        return self._dao.obtener_notas_por_alumno(alumno_id)
    def inasistencias_por_alumno(self, alumno_id):
        return self._dao.obtener_inasistencias_por_alumno(alumno_id)

    def lista_por_nombre_apellido(self):
        return self._dao.listar_nombre_y_apellido()

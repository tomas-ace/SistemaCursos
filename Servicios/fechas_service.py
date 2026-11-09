from datetime import *


class Fechas_Service():
    def __init__(self):
        pass

    def validar_fecha(self, fecha, uso):
        partes_fecha = fecha.split("-")
        if not self.es_fecha(fecha):
            return f"El campo Fecha de {uso} es inválido o no cumple con el formato AAAA-MM-DD."
        elif uso=="Nacimiento" and (int(partes_fecha[0]) < 1900 or int(partes_fecha[0]) > 2008):
            return f"El año en el campo Fecha de {uso} debe estar entre 1900 y 2008."
        elif (uso=="Inscripcion" or uso=="Nota" or uso=="Asistencia") and int (partes_fecha[0]) < 2026:
            return f"El año en el campo Fecha debe ser posterior a 2025."
        else:
            return True
        
    def es_fecha(self,fecha_texto):
        try:
            fecha_valida = datetime.strptime(fecha_texto, "%Y-%m-%d")
            return True
        except ValueError:
            return False
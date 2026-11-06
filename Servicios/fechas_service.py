from datetime import *


class Fechas_Service():
    def __init__(self):
        pass

    def validar_fecha(self, fecha, uso):
        partes_fecha = fecha.split("-")
        # if len(partes_fecha) != 3 or partes_fecha[0] == "" or partes_fecha[1] == "" or partes_fecha[2] == "":
        #     return f"El campo Fecha de {uso} está incompleto o vacío."
        # elif not partes_fecha[0].isdigit() or not partes_fecha[1].isdigit() or not partes_fecha[2].isdigit():
        #     return f"El campo Fecha de {uso} debe contener solo números."
        # elif len(partes_fecha[0]) != 4 or len(partes_fecha[1]) != 2 or len(partes_fecha[2]) != 2:
        #     return f"El campo Fecha de {uso} debe tener el formato DD-MM-AAAA."
        # elif int(partes_fecha[1]) < 1 or int(partes_fecha[1]) > 12:
        #     return f"El mes en el campo Fecha de {uso} debe estar entre 01 y 12."
        # elif int(partes_fecha[2]) < 1 or int(partes_fecha[2]) > 31:
        #     return f"El día en el campo Fecha de {uso} debe estar entre 01 y 31."
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
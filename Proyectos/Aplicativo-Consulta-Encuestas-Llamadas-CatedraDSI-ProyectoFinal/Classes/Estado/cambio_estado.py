import os
import sys
from datetime import datetime, date

this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, ".../"))

from Classes.Estado.estado import Estado


class CambioEstado:
    def __init__(self, fecha_hora_inicio: datetime, estado: Estado):
        # Atributo propio
        self.__fecha_hora_inicio = fecha_hora_inicio

        # Atributo referencia
        self.__estado = estado


    # Getter fecha_hora_inicio
    @property
    def fecha_hora_inicio(self):
        # Executes this code when object.att
        return self.__fecha_hora_inicio 

    # Setter fecha_hora_inicio
    @fecha_hora_inicio.setter
    def fecha_hora_inicio(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__fecha_hora_inicio = value

    # Getter estado
    @property
    def estado(self):
        # Executes this code when object.att
        return self.__estado
    
    # Setter estado
    @estado.setter
    def estado(self, value):
        # Executes this code when object.att
        self.__estado = value


    # Mensajes de CU

    # Mensaje 22
    def get_nombre_estado(self):
        # Mensaje 23
        return self.estado.nombre


if __name__ == "__main__":
    pass
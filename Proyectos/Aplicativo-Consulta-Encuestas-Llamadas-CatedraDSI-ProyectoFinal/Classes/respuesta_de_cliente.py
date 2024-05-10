import os
import sys
from datetime import date

this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from Classes.respuesta_posible import RespuestaPosible


class RespuestaDeCliente:
    def __init__(self, fecha_encuesta: date, respuesta_seleccionada: RespuestaPosible):
        # Atributos propios
        self.__fecha_encuesta = fecha_encuesta

        # Atributo referencia
        self.__respuesta_seleccionada = respuesta_seleccionada  # Asociation

    # -------------------
    # Getters & Setters -
    # -------------------

    # Getter fecha_encuesta
    @property
    def fecha_encuesta(self):
        # Executes this code when object.att
        return self.__fecha_encuesta

    # Setter fecha_encuesta
    @fecha_encuesta.setter
    def fecha_encuesta(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__fecha_encuesta = value


    # Getter respuesta_seleccionada
    @property
    def respuesta_seleccionada(self):
        # Executes this code when object.att
        return self.__respuesta_seleccionada

    # Setter respuesta_seleccionada
    @respuesta_seleccionada.setter
    def respuesta_seleccionada(self, value):
        # Executes this code when object.att = value
        self.__respuesta_seleccionada = value


    # MEnsajes de CU

    # Mensaje 27
    def get_descripcion_rta(self):
        return self.respuesta_seleccionada.descripcion
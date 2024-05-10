import os
import sys

this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

from Classes.respuesta_posible import RespuestaPosible

class Pregunta:
    def __init__(self, pregunta: str):
        # Atributos propios
        self.__pregunta = pregunta

        # Atributos referencia
        self.__respuestas = []

    # -------------------
    # Getters & Setters -
    # -------------------

    # Getter pregunta
    @property
    def pregunta(self):
        # Executes this code when w1.name
        return self.__pregunta

    # Setter pregunta
    @pregunta.setter
    def pregunta(self, value):
        # Executes this code when w1.name = something
        if len(value) > 15:
            raise Exception("Flayaste, muy largo")
        else:
            self.__pregunta = value

    # Getter respuestas
    @property
    def respuestas(self):
        # Executes this code when w1.name
        return self.__respuestas

    # Add respuesta posible
    def add_respuesta(self, respuesta: RespuestaPosible):
        self.__respuestas.append(respuesta)

    
    # Metodos de CU


    # Metodo utilizado en el 24

    def tiene_respuesta(self, rta):
        return rta in self.listar_respuestas_posibles()



    # Mensaje 31.1
    def listar_respuestas_posibles(self):
        """
        Busca en todas sus respuestas posibles, las descripciones
        """
        # Mensaje 31.2
        descripciones_respuestas = [rta.descripcion for rta in self.respuestas]
        # for rta in self.respuestas:
        #     descripciones_respuestas.append(rta.descripcion)  # mensaje 31.b
        return descripciones_respuestas



if __name__ == "__main__":
    # p1 = Pregunta("hola")
    # p1.add_respuesta(RespuestaPosible("1", "2"))
    # p1.add_respuesta(RespuestaPosible("4", "52"))
    # p1.add_respuesta(RespuestaPosible("gw", "25"))

    # print(p1.tiene_respuesta("3"))
    pass
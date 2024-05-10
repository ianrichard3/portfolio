import os
import sys
from datetime import date
from typing import List

this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

import Classes.cliente as cliente_class
import Classes.Estado.cambio_estado as cambio_estado
from Classes.respuesta_de_cliente import RespuestaDeCliente

from Classes.PatronIterator.i_agregado import IAgregado
from Classes.PatronIterator.iterador_respuestas_cliente import IteradorRespuestasDeCliente



class Llamada(IAgregado):
    def __init__(self, descripcion_operador: str, detalle_accion: str,
                 encuesta_enviada: bool, observacion_auditor: str, 
                 cliente: cliente_class.Cliente, duracion: float):
        # Validaciones
        # assert duracion > 0.0, "La duracion debe ser mayor a cero"

        # Atributos propios

        self.__descripcion_operador = descripcion_operador
        self.__detalle_accion = detalle_accion
        self.__encuesta_enviada = encuesta_enviada
        self.__observacion_auditor = observacion_auditor
        self.__duracion = duracion

        # Atributos referencia
        self.__respuestas_de_encuesta = []
        self.__cambios_estado = []
        self.__cliente = cliente


    # -------------------
    # Getters & Setters -
    # -------------------

    # Getter descripcion_operador
    @property
    def descripcion_operador(self):
        # Executes this code when object.att
        return self.__descripcion_operador

    # Setter descripcion_operador
    @descripcion_operador.setter
    def descripcion_operador(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__descripcion_operador = value

    # Getter detalle_accion
    @property
    def detalle_accion(self):
        # Executes this code when object.att
        return self.__detalle_accion


    # Setter detalle_accion
    @detalle_accion.setter
    def detalle_accion(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__detalle_accion = value


    # Getter encuesta_enviada
    @property
    def encuesta_enviada(self):
        # Executes this code when object.att
        return self.__encuesta_enviada

    # Setter encuesta_enviada
    @encuesta_enviada.setter
    def encuesta_enviada(self, value):
        # Executes this code when object.att = value
        self.__encuesta_enviada = value


    # Getter encuesta_enviada
    @property
    def encuesta_is_enviada(self):
        # Executes this code when object.att
        return self.__encuesta_is_enviada

    # Setter encuesta_enviada
    @encuesta_is_enviada.setter
    def encuesta_is_enviada(self, value):
        # Executes this code when object.att = value
        self.__encuesta_is_enviada = value


    # Getter observacion_auditor
    @property
    def observacion_auditor(self):
        # Executes this code when object.att
        return self.__observacion_auditor

    # Setter observacion_auditor
    @observacion_auditor.setter
    def observacion_auditor(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__observacion_auditor = value

    # Getter duracion
    @property
    def duracion(self):
        # Executes this code when object.att
        return self.__duracion

    # Setter duracion
    @duracion.setter
    def duracion(self, value):
        # Executes this code when object.att = value
        if value < 0.0:
            raise Exception("No puede ser negativo")
        else:
            self.__duracion = value

    # Getter duracion
    @property
    def cliente(self):
        # Executes this code when object.att
        return self.__cliente

    # Setter duracion
    @cliente.setter
    def cliente(self, value):
        # Executes this code when object.att = value
        self.__cliente = value

    # Getter respuestas_de_encuesta
    @property
    def respuestas_de_encuesta(self):
        # Executes this code when object.att
        return self.__respuestas_de_encuesta
    
    # Add respuesta de encuesta
    def add_respuesta_encuesta(self, respuesta_encuesta: RespuestaDeCliente):
        self.__respuestas_de_encuesta.append(respuesta_encuesta)

    # Getter cambio_estado
    @property
    def cambios_estado(self):
        # Executes this code when object.att
        return self.__cambios_estado
    
    # Add cambio de estado
    def add_cambio_estado(self, cambio_estado: cambio_estado.CambioEstado):
        # Puede ser que haga falta hacer un add in order
        self.__cambios_estado.append(cambio_estado)


    # Metodos

    def calcular_duracion(self):
        fecha_hora_inicio_llamada = self.cambios_estado[0].fecha_hora_inicio
        fecha_hora_fin_llamada = self.cambios_estado[-1].fecha_hora_inicio
        duracion = fecha_hora_fin_llamada - fecha_hora_inicio_llamada 
        return round(duracion.seconds/60, 2)
    
    def get_fecha_inicio(self):
        # primer_cambio_estado = self.cambios_estado[0]
        primer_cambio_estado = min(self.cambios_estado, key=lambda cambio: cambio.fecha_hora_inicio)

        fecha_inicio_llamada = primer_cambio_estado.fecha_hora_inicio.date()
        return fecha_inicio_llamada

    
    # Metodos de ejecucion de CU

    # mensaje 9
    def es_de_periodo(self, fecha_inicio_periodo: date, fecha_fin_periodo: date):
        fecha_inicio_llamada = self.get_fecha_inicio()
        # print(type(fecha_inicio_llamada))
        if fecha_inicio_periodo < fecha_inicio_llamada < fecha_fin_periodo:
            print(f"[ Llamada en periodo encontrada ] ")
            return True
        return False
    
    # mensaje 10   - y el mensaje 11 con el len
    def tiene_respuesta_encuesta(self):
        # Mensaje 11
        return len(self.respuestas_de_encuesta) > 0  
        # return self.respuestas_de_encuesta.existe_respuesta() (mensaje 11)
        # return self.respuestas_de_encuesta

    # mensaje 17
    def get_nombre_de_cliente(self):
        # Mensaje 18
        return self.cliente.nombre_completo

    # mensaje 20
    def buscar_ultimo_estado(self):
        # Mensaje 21      (Acceder al ultimo elemento de la lista cambios de estado)
        # ultimo_cambio_estado = self.cambios_estado[-1]

        # Obtener el de la fecha hora inicio mas antigua

        # ultima_fecha = max([c.fecha_hora_inicio for c in self.cambios_estado])
        # ultimo_cambio_estado = list(filter(lambda x: x.fecha_hora_inicio == ultima_fecha, self.cambios_estado))[0]
        
        ultimo_cambio_estado = max(self.cambios_estado, key=lambda cambio: cambio.fecha_hora_inicio)
        

        
        # Mensaje 22
        return ultimo_cambio_estado.get_nombre_estado()
    


    def crear_iterador(self, elementos: List[RespuestaDeCliente]) -> IteradorRespuestasDeCliente:
        return IteradorRespuestasDeCliente(elem=elementos)


    # Mensaje 25
    def buscar_datos_de_respuestas(self, encuesta_asociada) -> list:


        preguntas_y_respuestas = []


        iterador = self.crear_iterador(self.respuestas_de_encuesta)


        iterador.primero()
        

        while not iterador.ha_terminado():
            
            respuesta_actual = iterador.actual()

            # 26 y 27
            descripcion_rta_actual = respuesta_actual.get_descripcion_rta()

            # 28     {pregunta: p, respuesta: r}
            datos_de_respuesta = self.buscar_datos_respuesta(descripcion_rta_actual, encuesta_asociada)

            preguntas_y_respuestas.append(datos_de_respuesta)

            iterador.siguiente()
        
        return preguntas_y_respuestas

            


    
    # Metodo 28
    def buscar_datos_respuesta(self, respuesta_actual, encuesta_asociada) -> dict:


        # 29
        datos_preguntas_y_respuestas = encuesta_asociada.buscar_datos_preguntas_por_respuesta(respuesta_actual)
        return datos_preguntas_y_respuestas



    # Utilizado en metodo 24
    def get_respuesta_filtro(self):
        if self.respuestas_de_encuesta:
            return self.respuestas_de_encuesta[0].get_descripcion_rta()



    # def buscar_datos_encuesta_llamada_loopeando_encuestas(self, respuesta_actual) -> dict:

    #     # Obtener TODAS las encuestas para poder loopear





if __name__ == "__main__":
    pass
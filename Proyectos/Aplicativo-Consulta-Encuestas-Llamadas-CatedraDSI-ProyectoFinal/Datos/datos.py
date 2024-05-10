import sys
import os
from datetime import date, datetime

this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "..\\"))
from Support.funciones_soporte import from_string_to_date
from Classes.llamada import Llamada
from Classes.cliente import Cliente
from Classes.Estado.cambio_estado import CambioEstado
from Classes.Estado.estado import Estado
from Classes.respuesta_de_cliente import RespuestaDeCliente
from Classes.respuesta_posible import RespuestaPosible
from Classes.encuesta import Encuesta
from Classes.pregunta import Pregunta
from Classes import pregunta
from Classes.gestor_consulta_encuesta import GestorConsultaEncuesta


# LLAMADAS

llamadas = []

estado_iniciado = Estado("Inicializado")
estado_finalizado = Estado("Finalizado")


# Aca creamos el listado de llamadas
def crear_llamada(fecha_hora_ce1, fecha_hora_ce2, dni, nombre, nro, operador,
                  detalle, encuesta_enviada, observacion, 
                  rtas):
    ce1 = CambioEstado(fecha_hora_ce1, estado_iniciado)
    ce2 = CambioEstado(fecha_hora_ce2, estado_iniciado)
    cliente = Cliente(dni, nombre, nro)
    llamada = Llamada(operador, detalle, encuesta_enviada, observacion, cliente, ce1)
    llamada.add_cambio_estado(ce2)
    for rta in rtas:
        rta_add = RespuestaDeCliente(rta[0], rta[1])
        llamada.add_respuesta_encuesta(rta_add)
    return llamada


# llamada 1   (encuesta 1)
llamadas.append(crear_llamada(datetime(2022,5,3,16,10), datetime(2022,5,3,16,50),
              "23456789", "María Rodríguez", "3672345678",
              "Operador2", "Denunciar robo", True, "ConObservacion",
              [(date(2020,4,5), RespuestaPosible("Si", "1")),
               (date(2020,4,6), RespuestaPosible("Bien", "2")),
               (date(2020,4,7), RespuestaPosible("Si, Si se soluciono", "1"))]))



# llamada 2    (encuesta 4)
llamadas.append(crear_llamada(datetime(2017,3,8,13,13), datetime(2017,3,8,13,43),
              "12345678", "Juan Perez", "5551234567",
              "Operador1", "Comunicar Saldo", True, "SinObservacion",
              [(date(2017,4,5), RespuestaPosible("No, no se solucionó", "2")),
               (date(2017,4,5), RespuestaPosible("Insatisfecho", "2")),
               (date(2017,4,5), RespuestaPosible("No, no lo recomendaría", "2"))]))


# llamada 3    (Encuesta 1)
llamadas.append(crear_llamada(datetime(2021,8,5,10,23), datetime(2021,8,5,10,55),
              "34567890", "Carlos González", "5763456789",
              "Operador3", "Dar baja tarjeta", True, "SinObservacion",
              [(date(2021,8,5), RespuestaPosible("Si", "1")),
               (date(2021,8,5), RespuestaPosible("Bien", "2"))]))


# llamada 4   (encuesta 2)
llamadas.append(crear_llamada(datetime(2013,2,5,20,0), datetime(2013,2,5,20,36),
              "23456789", "Juan Cruz", "3541237683",
              "Operador2", "Comunicar Saldo", True, "ConObservacion",
              [(date(2013,2,6), RespuestaPosible("Regular", "3")),
               (date(2013,2,7), RespuestaPosible("Si, si lo recomendaría", "2"))]))


# llamada 5   (encuesta 3)
llamadas.append(crear_llamada(datetime(2015,4,16,15,15), datetime(2015,4,16,16,0),
              "38942011", "Lionel Messi", "3551213652",
              "Operador4", "Comunicar Saldo", True, "SinObservacion",
              [(date(2015,4,17), RespuestaPosible("Satisfecho", "4")),
               (date(2015,4,17), RespuestaPosible("No, no se solucionó", "2")),]))


# llamada 6   (encuesta 5)
llamadas.append(crear_llamada(datetime(2019,1,14,14,10), datetime(2019,1,14,14,35),
              "40221156", "Jonas Sarmiento", "3512125328",
              "Operador3", "Dar baja tarjeta", True, "ConObservacion",
              [(date(2019,1,14), RespuestaPosible("Mala", "2")),
               (date(2019,1,14), RespuestaPosible("No, no se solucionó", "2")),
               (date(2019,1,15), RespuestaPosible("Tal vez", "3"))]))

# llamada 7   (encuesta 2)
llamadas.append(crear_llamada(datetime(2019,5,22,11,25), datetime(2019,5,22,12,5),
              "38424377", "Milagros Reseña", "3515622158",
              "Operador1", "Dar baja tarjeta", True, "SinObservacion",
              [(date(2019,5,22), RespuestaPosible("Muy Buena", "5")),
               (date(2019,5,23), RespuestaPosible("Si, lo recomendaría", "1"))]))

#Fin de la creacion del listado de llamadas




# ENCUESTAS

def crear_pregunta(preg, rtas):
    p = Pregunta(preg)
    for rta in rtas:
        r = RespuestaPosible(rta[0], rta[1])
        p.add_respuesta(r)
    return p

def crear_encuesta(desc, fecha_vig, preguntas):
    e = Encuesta(desc, fecha_vig)
    for pre in preguntas:
        e.add_pregunta(pre)
    return e

encuestas = []

# Encuesta 1

p1 = crear_pregunta("¿Se soluciono su problema?", 
                    [("Si, Si se soluciono", "1"),
                     ("No, No se soluciono", "2")])

p2 = crear_pregunta("¿Como califica al representante que atendio su consulta?", 
                    [("Mal", "1"),
                     ("Bien", "2"),
                     ("Muy Bien", "3")])

p3 = crear_pregunta("¿Recomendaria nuestro servicio a otras personas?", 
                    [("Si", "1"),
                     ("No", "2"),
                     ("Tal vez", "3")])

encuestas.append(crear_encuesta(
    "Atención al Cliente", date(2023,9,25), [p1, p2, p3]
))



# Encuesta 2

p1 = crear_pregunta("¿Que tal ha sido la atencion proporcionada?", 
                    [("Muy mala", "1"),
                     ("Mala", "2"),
                     ("Regular", "3"),
                     ("Buena", "4"),
                     ("Muy Buena", "5")
                     ])

p2 = crear_pregunta("¿Recomendaría nuestro servicio a otras personas?", 
                    [("Si, lo recomendaría", "1"),
                     ("No, no lo recomendaría", "2")])




encuestas.append(crear_encuesta(
    "Atención al Cliente", date(2025,12,8), [p1, p2]
))



# Encuesta 3


p1 = crear_pregunta("¿Que tan satisfecho quedó después de la llamada?", 
                    [("Muy insatisfecho", "1"),
                     ("Insatisfecho", "2"),
                     ("Regular", "3"),
                     ("Satisfecho", "4"),
                     ("Muy Satisfecho", "5")
                     ])

p2 = crear_pregunta("¿Se logró solucionar su problema?", 
                    [("Si, se solucionó", "1"),
                     ("No, no se solucionó", "2")])




encuestas.append(crear_encuesta(
    "Atención al Cliente", date(2026,12,1), [p1, p2]
))



# Encuesta 4


p1 = crear_pregunta("¿Se soluciono su problema?", 
                    [("Si, Si se soluciono", "1"),
                     ("No, No se soluciono", "2")])

p2 = crear_pregunta("¿Recomendaría nuestro servicio a otras personas?", 
                    [("Si, lo recomendaría", "1"),
                     ("No, no lo recomendaría", "2")])

p3 = crear_pregunta("¿Que tan satisfecho quedó después de la llamada?", 
                    [("Muy insatisfecho", "1"),
                     ("Insatisfecho", "2"),
                     ("Regular", "3"),
                     ("Satisfecho", "4"),
                     ("Muy Satisfecho", "5")
                     ])

encuestas.append(crear_encuesta(
    "Atención al Cliente", date(2022,9,15), [p1, p2, p3]
))



# Encuesta 5


p1 = crear_pregunta("¿Que tal ha sido la atencion proporcionada?", 
                    [("Muy mala", "1"),
                     ("Mala", "2"),
                     ("Regular", "3"),
                     ("Buena", "4"),
                     ("Muy Buena", "5")
                     ])

p2 = crear_pregunta("¿Se soluciono su problema?", 
                    [("Si, Si se soluciono", "1"),
                     ("No, No se soluciono", "2")])

p3 = crear_pregunta("¿Recomendaria nuestro servicio a otras personas?", 
                    [("Si", "1"),
                     ("No", "2"),
                     ("Tal vez", "3")])

encuestas.append(crear_encuesta(
    "Atención al Cliente", date(2028,6,1), [p1, p2, p3]
))


if __name__ == "__main__":
    for e in encuestas:
        print(e.descripcion)

    for l in llamadas:
        print(l.descripcion_operador)

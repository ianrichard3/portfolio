# CADA INSTANCIA DE CADA CLASE DEBE SER CREADA EN EL ARCHIVO DE LA CLASE CORRESPONDIENTE, 
# ASI CUANDO IMPORTEMOS CADA MODULO, SE IMPORTA LA CLASE Y LOS OBJETOS, EN ESTE CASO DE PRUEBA

from datetime import date, datetime
import sys
import os

this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))
from Support.funciones_soporte import from_string_to_date

from Classes.llamada import Llamada
from Classes.cliente import Cliente
from Classes.Estado.cambio_estado import CambioEstado
from Classes.Estado.estado import Estado
from Classes.respuesta_de_cliente import RespuestaDeCliente
from Classes.respuesta_posible import RespuestaPosible
from Classes.encuesta import Encuesta
from Classes.pregunta import Pregunta
from Classes.gestor_consulta_encuesta import GestorConsultaEncuesta
from Classes.GUI.pantalla_consultar_encuesta import PantallaConsultarEncuesta

import Datos.datos as datos



"""
#  //// TEST mensajes 8-11

r_posible = RespuestaPosible("Correcto", "12")

r_cliente = RespuestaDeCliente(datetime(2001, 4, 12, 18, 34, 20), r_posible)

estado_iniciado = Estado("Iniciado")
cambio_estado_1 = CambioEstado(datetime(2001, 4, 12, 18, 14, 20), estado_iniciado) 
cambio_estado_2 = CambioEstado(datetime(2012, 4, 12, 18, 14, 20), estado_iniciado) 

# cambio_estado_3 = CambioEstado(datetime(2022, 4, 12, 18, 14, 20), estado_iniciado) 

cliente1 = Cliente("23453432", "Humberto Primo", "3513433777")

llamada1 = Llamada("Flaquito 1", "Llama profesional", 3.3, True, "Completada", cliente1, cambio_estado_1)
llamada1.add_respuesta_encuesta(r_cliente)

llamada2 = Llamada("Furroberto", "Llama a Motel", 6.7, True, "Completada", cliente1, cambio_estado_2)


fecha_inicio_periodo = date(2000, 4, 21)
fecha_fin_periodo = date(2009, 4, 21)

gestor = GestorConsultaEncuesta()
gestor.fecha_inicio_periodo = fecha_inicio_periodo
gestor.fecha_fin_periodo = fecha_fin_periodo
gestor.llamadas.append(llamada1)
gestor.llamadas.append(llamada2)

for llamada_found in gestor.buscar_llamadas_en_periodo():
    print(llamada_found.descripcion_operador)

"""
"""
#  //// Test mensajes 24-33

# Ejemplos encuestas

fecha_fin_vigencia = date(2010, 4, 21)

# pregunta 1
pregunta1_encuesta1 = Pregunta("Te gusto?")
rta1_pregunta1_encuesta1 = RespuestaPosible("Si", "Si")
rta2_pregunta1_encuesta1 = RespuestaPosible("No", "No")
pregunta1_encuesta1.add_respuesta(rta1_pregunta1_encuesta1)
pregunta1_encuesta1.add_respuesta(rta2_pregunta1_encuesta1)

# pregunta 2

pregunta2_encuesta1 = Pregunta("Reseña de llamada:")
rta1_pregunta2_encuesta1 = RespuestaPosible("Buena", "Buena")
rta2_pregunta2_encuesta1 = RespuestaPosible("Mala", "Mala")
rta3_pregunta2_encuesta1 = RespuestaPosible("Muy buena", "Muy buena")
rta4_pregunta2_encuesta1 = RespuestaPosible("Muy mala", "Muy mala")
pregunta2_encuesta1.add_respuesta(rta1_pregunta2_encuesta1)
pregunta2_encuesta1.add_respuesta(rta2_pregunta2_encuesta1)
pregunta2_encuesta1.add_respuesta(rta3_pregunta2_encuesta1)
pregunta2_encuesta1.add_respuesta(rta4_pregunta2_encuesta1)

# pregunta 3 (p 1 encuesta 2)
pregunta1_encuesta2 = Pregunta("Como andas amigo")
rta1_pregunta3_encuesta1 = RespuestaPosible("Bien", "Bien")
rta2_pregunta3_encuesta1 = RespuestaPosible("Mal", "Mal")
pregunta1_encuesta2.add_respuesta(rta1_pregunta3_encuesta1)
pregunta1_encuesta2.add_respuesta(rta2_pregunta3_encuesta1)


encuesta1 = Encuesta("Encuesta numero 1", fecha_fin_vigencia)
encuesta1.add_pregunta(pregunta1_encuesta1)
encuesta1.add_pregunta(pregunta2_encuesta1)

encuesta2 = Encuesta("Encuesta numero 2", fecha_fin_vigencia)
encuesta2.add_pregunta(pregunta1_encuesta2)


# datos llamada
cliente1 = Cliente("23453432", "Humberto Primo", "3513433777")
estado_iniciado = Estado("Iniciado")
cambio_estado_1 = CambioEstado(datetime(2001, 4, 12, 18, 14, 20), estado_iniciado) 
llamada1 = Llamada("Flaquito 1", "Llama profesional", 3.3, True, "Completada", cliente1, cambio_estado_1)
r_cliente1 = RespuestaDeCliente(datetime(2001, 4, 12, 18, 34, 20), rta1_pregunta2_encuesta1)
r_cliente2 = RespuestaDeCliente(datetime(2001, 4, 12, 18, 34, 20), rta1_pregunta3_encuesta1)
r_cliente3 = RespuestaDeCliente(datetime(2001, 4, 12, 18, 34, 20), rta4_pregunta2_encuesta1)


llamada1.add_respuesta_encuesta(r_cliente1)
llamada1.add_respuesta_encuesta(r_cliente2)
llamada1.add_respuesta_encuesta(r_cliente3)


# Creacion Gestor

gestor = GestorConsultaEncuesta()
gestor.llamada_seleccionada = llamada1
gestor.add_encuesta(encuesta1)
gestor.add_encuesta(encuesta2)

datos_encuestas = gestor.buscar_encuesta_de_respuesta()

# print(datos_encuestas)
for datos_encuesta in datos_encuestas:
    # print(datos_encuesta)
    preg = datos_encuesta.get("pregunta")
    rta = datos_encuesta.get("respuesta")
    enc = datos_encuesta.get("encuesta")
    print(f"Pregunta: '{preg}'  |  Respuesta: '{rta}'  |  Encuesta:  '{enc}'")



# Prueba mensajes 16-23


fecha_hora_inicio_ce1 = datetime(2023, 2, 14, 14, 34, 2)     # 14/2/23  14:34:02
fecha_hora_inicio_ce2 = datetime(2023, 3, 14, 16, 34, 2)     # 14/3/23  16:34:02
fecha_hora_inicio_ce3 = datetime(2023, 1, 20, 11, 34, 2)     # 20/1/23  11:34:02


# Objetos estado
estado_finalizado = Estado("Finalizado")
estado_pendiente = Estado("Pendiente")
estado_creado = Estado("Creado")

# Objetos cambio de estado
cambio_estado_1 = CambioEstado(fecha_hora_inicio_ce1, estado_creado)
cambio_estado_2 = CambioEstado(fecha_hora_inicio_ce2, estado_pendiente)
cambio_estado_3 = CambioEstado(fecha_hora_inicio_ce3, estado_finalizado)

# Objetos cliente
cliente1 = Cliente("58325392", "Ian El amigo", "214214124")

# Objetos de llamada
llamada1 = Llamada("Operador Flaquito", "Llamada profesional", 2.4, True, "", cliente1, cambio_estado_1)
llamada1.add_cambio_estado(cambio_estado_2)
llamada1.add_cambio_estado(cambio_estado_3)

# Objeto de Gestor
gestor = GestorConsultaEncuesta()
gestor.add_llamada(llamada1)
gestor.llamada_seleccionada = llamada1


datos_llamada = gestor.buscar_datos_llamada()
print(datos_llamada.get("duracion"))
print(datos_llamada.get("estado_actual"))
print(datos_llamada.get("cliente"))

""" 

# Prueba 16 - 33

"""
# Objeto de Gestor
gestor = GestorConsultaEncuesta()
for l in datos.llamadas:
    gestor.add_llamada(l)
for e in datos.encuestas:
    gestor.add_encuesta(e)

gestor.llamada_seleccionada = datos.llamadas[1]

datos_llamada = gestor.buscar_datos_llamada()
print(datos_llamada.get("duracion"))
print(datos_llamada.get("estado_actual"))
print(datos_llamada.get("cliente"))
print(datos_llamada.get("datos_encuesta"))

"""

from UI.pantalla_cons2 import PantallaCons2


from Persistencia.ConversoresPersistencia.llamada_conversor import LlamadaConversor
from Persistencia.ConversoresPersistencia.encuesta_conversor import EncuestaConversor



def mapear_objetos_persistentes():
    llamadas = [LlamadaConversor.mapear_llamada(l) for l in  LlamadaConversor.get_all()]
    encuestas = [EncuestaConversor.mapear_encuesta(e) for e in  EncuestaConversor.get_all()]
    return llamadas, encuestas


def main():
    gestor1 = GestorConsultaEncuesta()
    # pantalla1 = PantallaConsultarEncuesta()
    pantalla2 = PantallaCons2()


    # gestor1.pantalla = pantalla1
    # pantalla1.gestor = gestor1

    gestor1.pantalla = pantalla2
    pantalla2.gestor = gestor1

    llamadas, encuestas = mapear_objetos_persistentes()

    for llamada in llamadas:
        gestor1.add_llamada(llamada)
        
    for e in encuestas:
        gestor1.add_encuesta(e)

    # pantalla1.opcion_consultar_encuesta()

    pantalla2.opcion_consultar_encuesta()
    



if __name__ == "__main__":
    main()




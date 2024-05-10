import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))
sys.path.append(os.path.join(this_file_path, ".../"))


from database_config import session
from Entidades.llamada import Llamada as LlamadaPersistente
from Classes.llamada import Llamada


from ConversoresPersistencia.respuesta_cliente_conversor import RespuestaClienteConversor
from ConversoresPersistencia.cambio_estado_conversor import CambioEstadoConversor
from ConversoresPersistencia.cliente_conversor import ClienteConversor





class LlamadaConversor:

    @staticmethod
    def get_all():


        resultados = session.query(LlamadaPersistente).all()

        return resultados
    

    @staticmethod
    def mapear_llamada(llamada_persistente: LlamadaPersistente):

        descripcion_operador = llamada_persistente.descripcion_operador
        detalle_accion_requerida = llamada_persistente.detalle_accion_requerida
        duracion = llamada_persistente.duracion
        encuesta_enviada = llamada_persistente.encuesta_enviada
        observacion_auditor = llamada_persistente.observacion_auditor

        cliente = ClienteConversor.get_mapped_by_id(llamada_persistente.id_cliente)
        

        llamada_mapeada = Llamada(descripcion_operador,
                                  detalle_accion_requerida,
                                  encuesta_enviada,
                                  observacion_auditor,
                                  cliente, 
                                  duracion)


        respuestas_encuesta_persistentes = RespuestaClienteConversor.get_all_by_id_llamada(llamada_persistente.id_llamada)
        # Convertir persistentes en Mapeadas y agregarlas a la lista
        [
            llamada_mapeada.add_respuesta_encuesta(
            RespuestaClienteConversor.mapear_respuesta(r)
            )
            for r in respuestas_encuesta_persistentes
        ]





        cambios_estado_persistentes = CambioEstadoConversor.get_all_by_id_llamada(llamada_persistente.id_llamada)
        # Convertir persistentes en Mapeados y agregarlas a la lista
        [
            llamada_mapeada.add_cambio_estado(
            CambioEstadoConversor.mapear_cambio_estado(e)
            )
            for e in cambios_estado_persistentes
        ]

        


        return llamada_mapeada
    




found = LlamadaConversor.get_all()
print(found[0].id_cliente)

m = LlamadaConversor.mapear_llamada(found[0])

print(m.descripcion_operador) 



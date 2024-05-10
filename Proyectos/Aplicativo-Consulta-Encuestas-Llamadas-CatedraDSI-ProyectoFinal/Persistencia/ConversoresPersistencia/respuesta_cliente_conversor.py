import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))
sys.path.append(os.path.join(this_file_path, ".../"))


from database_config import session
from Entidades.respuesta_de_cliente import RespuestaDeCliente as RespuestaDeClientePersistente
from Classes.respuesta_de_cliente import RespuestaDeCliente


from ConversoresPersistencia.respuesta_posible_conversor import RespuestaPosibleConversor 







class RespuestaClienteConversor:

    @staticmethod
    def get_all():

        resultados = session.query(RespuestaDeClientePersistente).all()

        return resultados
    
    @staticmethod
    def mapear_respuesta(respuesta_persistente: RespuestaDeClientePersistente):

        fecha_encuesta = respuesta_persistente.fecha_encuesta

        rta_seleccionada = RespuestaPosibleConversor.\
                        get_mapped_by_id(respuesta_persistente.id_respuesta_posible)



        rta_mapeada = RespuestaDeCliente(fecha_encuesta, rta_seleccionada)

        return rta_mapeada
    


    @staticmethod
    def get_all_by_id_llamada(id):

        res = session.query(RespuestaDeClientePersistente).filter(
            RespuestaDeClientePersistente.id_llamada == id
        ).all()

        return res



found = RespuestaClienteConversor.get_all()

m = RespuestaClienteConversor.mapear_respuesta(found[0])

print(m.get_descripcion_rta())


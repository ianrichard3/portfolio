import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))
sys.path.append(os.path.join(this_file_path, ".../"))


from database_config import session
from Entidades.cambio_estado import CambioEstado as CambioEstadoPersistente
from Classes.Estado.cambio_estado import CambioEstado


from ConversoresPersistencia.estado_conversor import EstadoConversor 







class CambioEstadoConversor:

    @staticmethod
    def get_all():

        resultados = session.query(CambioEstadoPersistente).all()

        return resultados
    
    @staticmethod
    def mapear_cambio_estado(cambio_persistente: CambioEstadoPersistente):

        fecha_hora_inicio = cambio_persistente.fecha_hora_inicio

        estado = EstadoConversor.\
                        get_mapped_by_id(cambio_persistente.id_estado)



        estado_mapeado = CambioEstado(fecha_hora_inicio, estado)

        return estado_mapeado
    


    @staticmethod
    def get_all_by_id_llamada(id):

        res = session.query(CambioEstadoPersistente).filter(
            CambioEstadoPersistente.id_llamada == id
        ).all()

        return res

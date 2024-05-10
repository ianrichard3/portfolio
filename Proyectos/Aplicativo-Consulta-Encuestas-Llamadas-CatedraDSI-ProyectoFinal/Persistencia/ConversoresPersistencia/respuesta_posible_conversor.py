import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))
sys.path.append(os.path.join(this_file_path, ".../"))


from database_config import session
from Entidades.respuesta_posible import RespuestaPosible as RespuestaPosiblePersistente
from Classes.respuesta_posible import RespuestaPosible






class RespuestaPosibleConversor:

    @staticmethod
    def get_all():

        resultados = session.query(RespuestaPosiblePersistente).all()

        return resultados
    
    @staticmethod
    def get_all_by_id_pregunta(id: int):

        res = session.query(RespuestaPosiblePersistente).filter(
            RespuestaPosiblePersistente.id_pregunta == id
        ).all()

        return res
    
    @staticmethod
    def mapear_respuesta(respuesta_posible_persistente: RespuestaPosiblePersistente):

        respuesta_posible_mapeada = RespuestaPosible(
            respuesta_posible_persistente.descripcion,
            respuesta_posible_persistente.valor)
        
        return respuesta_posible_mapeada
    

    @staticmethod
    def get_mapped_by_id(id):

        return RespuestaPosibleConversor.mapear_respuesta(

        session.query(RespuestaPosiblePersistente).filter(
            RespuestaPosiblePersistente.id_respuesta == id
        ).first()
        
        )
    
    
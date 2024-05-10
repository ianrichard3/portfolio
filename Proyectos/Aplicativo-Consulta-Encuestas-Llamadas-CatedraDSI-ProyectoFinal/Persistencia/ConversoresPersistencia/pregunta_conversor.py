import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))
sys.path.append(os.path.join(this_file_path, ".../"))


from database_config import session
from Entidades.pregunta import Pregunta as PreguntaPersistente
from Classes.pregunta import Pregunta


from ConversoresPersistencia.respuesta_posible_conversor import RespuestaPosibleConversor 






class PreguntaConversor:

    @staticmethod
    def get_all():

        resultados = session.query(PreguntaPersistente).all()

        return resultados
    

    @staticmethod
    def get_all_by_id_encuesta(id: int):

        res = session.query(PreguntaPersistente).filter(
            PreguntaPersistente.id_encuesta == id
        ).all()

        return res

    
    @staticmethod
    def mapear_pregunta(pregunta_persistente: PreguntaPersistente):

        pregunta_mapeada = Pregunta(pregunta_persistente.pregunta)

        respuestas_persistentes = RespuestaPosibleConversor.get_all_by_id_pregunta(pregunta_persistente.id_pregunta)

        # Convertir persistentes en Mapeadas y agregarlas a la lista
        [
            pregunta_mapeada.add_respuesta(
            RespuestaPosibleConversor.mapear_respuesta(r)
            )
            for r in respuestas_persistentes
        ]
        return pregunta_mapeada
    

    
    


# lol = PreguntaConversor.get_all()
# print(PreguntaConversor.mapear_pregunta(lol[0]).respuestas)
import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))
sys.path.append(os.path.join(this_file_path, ".../"))


from database_config import session
from Entidades.encuesta import Encuesta as EncuestaPersistente
from Classes.encuesta import Encuesta


from ConversoresPersistencia.pregunta_conversor import PreguntaConversor



class EncuestaConversor:

    @staticmethod
    def get_all():


        resultados = session.query(EncuestaPersistente).all()

        return resultados
    
    @staticmethod
    def mapear_encuesta(encuesta_persistente: EncuestaPersistente):

        descripcion = encuesta_persistente.descripcion
        fecha_fin_vigencia = encuesta_persistente.fecha_fin_vigencia

        encuesta_mapeada = Encuesta(descripcion, fecha_fin_vigencia)

        preguntas_persistentes = PreguntaConversor.get_all_by_id_encuesta(encuesta_persistente.id_encuesta)

        # Convertir persistentes en Mapeadas y agregarlas a la lista
        [
            encuesta_mapeada.add_pregunta(
            PreguntaConversor.mapear_pregunta(r)
            )
            for r in preguntas_persistentes
        ]
        


        return encuesta_mapeada





# TEST 

# found = EncuestaConversor.get_all()

# m = EncuestaConversor.mapear_encuesta(found[0])

# print(m.descripcion) 

# for p in m.preguntas:
#     print(p.pregunta)
#     for r in p.respuestas:
#         print("\t", r.descripcion)




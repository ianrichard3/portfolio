import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))
sys.path.append(os.path.join(this_file_path, ".../"))


from database_config import session
from Entidades.estado import Estado as EstadoPersistente
from Classes.Estado.estado import Estado






class EstadoConversor:

    @staticmethod
    def get_all():

        resultados = session.query(EstadoPersistente).all()

        return resultados
    
    @staticmethod
    def get_all_by_id_pregunta(id: int):

        res = session.query(EstadoPersistente).filter(
            EstadoPersistente.id_estado == id
        ).all()

        return res
    
    @staticmethod
    def mapear_estado(estado_persistente: EstadoPersistente):

        estado_mapeado = Estado(
            estado_persistente.nombre)
        
        return estado_mapeado
    

    @staticmethod
    def get_mapped_by_id(id):

        return EstadoConversor.mapear_estado(

        session.query(EstadoPersistente).filter(
            EstadoPersistente.id_estado == id
        ).first()
        
        )
    
    
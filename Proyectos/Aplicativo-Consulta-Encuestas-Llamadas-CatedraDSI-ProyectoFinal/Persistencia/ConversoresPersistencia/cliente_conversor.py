import os, sys
this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))
sys.path.append(os.path.join(this_file_path, ".../"))


from database_config import session
from Entidades.cliente import Cliente as ClientePersistente
from Classes.cliente import Cliente






class ClienteConversor:

    @staticmethod
    def get_all():

        resultados = session.query(ClientePersistente).all()

        return resultados
    
    @staticmethod
    def get_all_by_id_pregunta(id):

        res = session.query(ClientePersistente).filter(
            ClientePersistente.dni == id
        ).all()

        return res
    
    @staticmethod
    def mapear_cliente(cliente_persistente: ClientePersistente):
        print(cliente_persistente.dni)

        cliente_mapeado = Cliente(
            cliente_persistente.dni,
            cliente_persistente.nombre_completo,
            cliente_persistente.nro_celular)
        
        return cliente_mapeado
    

    @staticmethod
    def get_mapped_by_id(id: int):
        # print(id)

        return ClienteConversor.mapear_cliente(
            

        session.query(ClientePersistente).filter(
            ClientePersistente.dni == id
        ).first()
        
        )
    
    
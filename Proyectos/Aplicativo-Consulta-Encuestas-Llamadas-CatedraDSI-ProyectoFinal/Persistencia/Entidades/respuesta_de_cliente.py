from database_config import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class RespuestaDeCliente(Base):
    __tablename__ = "respuesta_de_cliente"

    id_respuesta_cliente = Column("id_respuesta_cliente", Integer, primary_key=True)
    id_llamada = Column("id_llamada", Integer, ForeignKey("llamada.id_llamada"))
    fecha_encuesta = Column("fecha_encuesta", String)
    id_respuesta_posible = Column("id_respuesta_posible", String, ForeignKey("respuesta_posible.id_respuesta"))

    def __init__(self, id_respuesta_cliente, id_llamada, fecha_encuesta, respuesta_seleccionada):
        self.id_respuesta_cliente = id_respuesta_cliente
        self.id_llamada = id_llamada
        self.fecha_encuesta = fecha_encuesta
        self.respuesta_seleccionada = respuesta_seleccionada

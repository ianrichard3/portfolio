from database_config import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class RespuestaPosible(Base):
    __tablename__ = "respuesta_posible"

    id_respuesta = Column("id_respuesta", Integer, primary_key=True)
    id_pregunta = Column("id_pregunta", Integer, ForeignKey('pregunta.id_pregunta'))
    descripcion = Column("descripcion", String)
    valor = Column("valor", Integer)

    def __init__(self, id_respuesta, id_pregunta, descripcion, valor):
        self.id_respuesta = id_respuesta
        self.id_pregunta = id_pregunta
        self.descripcion = descripcion
        self.valor = valor




from database_config import Base
from sqlalchemy import Column, Integer, String


class Estado(Base):
    __tablename__ = "estado"

    id_estado = Column("id_estado", Integer, primary_key=True)
    nombre = Column("nombre", String)

    def __init__(self, id_estado, nombre):
        self.id_estado = id_estado
        self.nombre = nombre




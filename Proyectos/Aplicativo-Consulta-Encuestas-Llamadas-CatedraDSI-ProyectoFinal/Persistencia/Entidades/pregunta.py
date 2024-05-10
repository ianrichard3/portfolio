from database_config import Base
from sqlalchemy import Column, Integer, String, ForeignKey



class Pregunta(Base):
    __tablename__ = "pregunta"

    id_pregunta = Column("id_pregunta", Integer, primary_key=True)
    id_encuesta = Column("id_encuesta", Integer, ForeignKey("encuesta.id_encuesta"))
    pregunta = Column("pregunta", String)

    def __init__(self, id_pregunta, pregunta):
        self.id_pregunta = id_pregunta
        self.pregunta = pregunta



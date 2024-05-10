from database_config import Base
from sqlalchemy import Column, Integer, String, Date

class Encuesta(Base):
    __tablename__ = "encuesta"

    id_encuesta = Column("id_encuesta", Integer, primary_key=True)
    descripcion = Column("descripcion", String)
    fecha_fin_vigencia = Column("fecha_fin_vigencia", Date)

    def __init__(self, id_encuesta, descripcion, fecha_fin_vigencia):
        self.id_encuesta = id_encuesta
        self.descripcion = descripcion
        self.fecha_fin_vigencia = fecha_fin_vigencia

    def __repr__(self):
        return f"<Encuesta(id_encuesta={self.id_encuesta}, descripcion={self.descripcion}, fecha_fin_vigencia={self.fecha_fin_vigencia})>"

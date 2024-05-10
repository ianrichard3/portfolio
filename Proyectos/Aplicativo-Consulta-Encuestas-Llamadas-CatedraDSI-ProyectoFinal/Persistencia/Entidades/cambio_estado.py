from database_config import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime

class CambioEstado(Base):
    __tablename__ = "cambio_estado"

    id_cambio_estado = Column("id_cambio_estado", Integer, primary_key=True)
    id_llamada = Column("id_llamada", Integer, ForeignKey('llamada.id_llamada'))
    id_estado = Column("id_estado", Integer, ForeignKey("estado.id_estado"))

    fecha_hora_inicio = Column("fecha_hora_inicio", DateTime)

    def __init__(self, id_cambio_estado, id_llamada):
        self.id_cambio_estado = id_cambio_estado
        self.id_llamada = id_llamada
        fecha_hora_inicio = fecha_hora_inicio
        



# Si no incluyes id_llamada como parte de la clave primaria en la tabla CambioEstado, 
# significa que podrías tener múltiples filas en la tabla CambioEstado con el mismo valor en la columna id_cambio_estado pero diferentes valores en id_llamada. 
# Esto implicaría que podrías tener múltiples cambios de estado con el mismo identificador id_cambio_estado asociados a diferentes llamadas.


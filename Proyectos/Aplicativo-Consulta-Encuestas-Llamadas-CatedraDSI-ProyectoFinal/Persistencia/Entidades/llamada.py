from database_config import Base
from sqlalchemy import Column, Integer, String, Boolean, REAL, ForeignKey



class Llamada(Base):
    __tablename__ = "llamada"

    id_llamada = Column("id_llamada", Integer, primary_key=True)
    descripcion_operador = Column("descripcion_operador", String)
    detalle_accion_requerida = Column("detalle_accion_requerida", String)
    duracion = Column("duracion", REAL)
    encuesta_enviada = Column("encuesta_enviada", Boolean)
    observacion_auditor = Column("observacion_auditor", String)
    id_cliente = Column("id_cliente", String, ForeignKey("cliente.dni"))


    
    
    def __init__(self, id_llamada, descripcion_operador, detalle_accion_requerida, duracion, encuesta_enviada, observacion_auditor):
        self.id_llamada = id_llamada
        self.descripcion_operador = descripcion_operador
        self.detalle_accion_requerida = detalle_accion_requerida
        self.duracion = duracion
        self.encuesta_enviada = encuesta_enviada
        self.observacion_auditor = observacion_auditor







# CREATE TABLE llamada (
#     descripcionOperador TEXT,
#     detalleAccionRequerida TEXT,
#     duracion INTEGER,
#     encuestaEnviada BOOLEAN,
#     observacionAuditor TEXT
# );
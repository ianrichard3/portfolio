from database_config import Base
from sqlalchemy import Column, String, Integer

class Cliente(Base):
    __tablename__ = "cliente"


    # id_cliente = Column("id_cliente", Integer, primary_key=True)
    dni = Column("dni", String, primary_key=True)
    nombre_completo = Column("nombre_completo", String)
    nro_celular = Column("nro_celular", String)


    def __init__(self, dni , nombre_completo, nro_celular):
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.nro_celular = nro_celular





"""
PRAGMA foreign_keys=off;
CREATE TEMPORARY TABLE backup_table AS SELECT * FROM cliente;
DROP TABLE cliente;
CREATE TABLE cliente (
    id_cliente INTEGER PRIMARY KEY,
    dni INTEGER,
    nombre_completo TEXT,
    nro_celular INTEGER
);
INSERT INTO cliente (id_cliente, dni, nombre_completo, nro_celular)
VALUES
    (1, '12345678', 'Juan Pérez', '555-123-4567'),
    (2, '23456789', 'María Rodríguez', '367-234-5678'),
    (3, '34567890', 'Carlos González', '576-345-6789');
DROP TABLE backup_table;
PRAGMA foreign_keys=on;



"""
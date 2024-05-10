from Classes.PatronIterator.i_iterador import IIterador
from typing import List, Dict
from Classes.respuesta_de_cliente import RespuestaDeCliente

class IteradorRespuestasDeCliente(IIterador):
    def __init__(self, elem: List[RespuestaDeCliente]) -> IIterador:
        super().__init__()

        self.elementos: List[RespuestaDeCliente] = elem
        self.posicion_actual: int = None

    
    def primero(self) -> None:
        self.posicion_actual = 0
    
    def siguiente(self) -> RespuestaDeCliente:
        self.posicion_actual += 1

    def ha_terminado(self) -> bool:
        return self.posicion_actual >= len(self.elementos)
    
    def actual(self) -> RespuestaDeCliente:
        return self.elementos[self.posicion_actual]
    
    def cumple_filtro(self, filtros: Dict[object, object]) -> bool:
        return 
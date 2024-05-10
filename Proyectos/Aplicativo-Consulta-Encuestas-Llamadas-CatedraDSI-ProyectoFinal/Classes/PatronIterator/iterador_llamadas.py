from Classes.PatronIterator.i_iterador import IIterador
from typing import List, Dict
from Classes.llamada import Llamada

class IteradorLlamadas(IIterador):
    def __init__(self, elem: List[Llamada]) -> IIterador:
        super().__init__()

        self.elementos: List[Llamada] = elem
        self.posicion_actual: int = None

    
    def primero(self) -> None:
        self.posicion_actual = 0
    
    def siguiente(self) -> Llamada:
        self.posicion_actual += 1

    def ha_terminado(self) -> bool:
        return self.posicion_actual >= len(self.elementos)
    
    def actual(self) -> Llamada:
        return self.elementos[self.posicion_actual]

    
    def cumple_filtro(self, filtros: Dict[object, object]) -> bool:
            return self.actual().es_de_periodo(filtros.get("fecha_inicio_periodo"), filtros.get("fecha_fin_periodo")) \
            and self.actual().tiene_respuesta_encuesta()


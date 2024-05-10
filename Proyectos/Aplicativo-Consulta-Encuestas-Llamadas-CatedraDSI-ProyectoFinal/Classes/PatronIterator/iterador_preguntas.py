from Classes.PatronIterator.i_iterador import IIterador
from typing import List, Dict
from Classes.pregunta import Pregunta

class IteradorPreguntas(IIterador):
    def __init__(self, elem: List[Pregunta]) -> IIterador:
        super().__init__()

        self.elementos: List[Pregunta] = elem
        self.posicion_actual: int = None

    
    def primero(self) -> None:
        self.posicion_actual = 0
    
    def siguiente(self) -> Pregunta:
        self.posicion_actual += 1

    def ha_terminado(self) -> bool:
        return self.posicion_actual >= len(self.elementos)
    
    def actual(self) -> Pregunta:
        return self.elementos[self.posicion_actual]
    
    def cumple_filtro(self, filtros: Dict[object, object]) -> bool:
        # Metodos 31 y 31b
        # ESTE SERIA EL tieneRespuesta()
        
        # return filtros.get("respuesta_de_pregunta") in self.actual().listar_respuestas_posibles()
    
        return self.actual().tiene_respuesta(filtros.get("respuesta_de_pregunta"))
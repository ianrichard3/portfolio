from abc import ABC, abstractmethod
from typing import List

# from i_iterador import IIterador
from Classes.PatronIterator.i_iterador import IIterador

class IAgregado(ABC):
    @abstractmethod
    def crear_iterador(self, elementos: List[object]) -> IIterador:
        pass
from abc import ABC, abstractmethod
from typing import List, Dict

class IIterador(ABC):

    @abstractmethod
    def primero(self) -> None:
        pass

    @abstractmethod
    def siguiente(self) -> None:
        pass

    @abstractmethod
    def actual(self) -> object:
        pass

    @abstractmethod
    def cumple_filtro(self, filtros: Dict[object, object]) -> bool:
        pass

    @abstractmethod
    def ha_terminado(self) -> bool:
        pass

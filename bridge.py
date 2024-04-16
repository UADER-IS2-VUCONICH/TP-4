#*--------------------------------------------------
#* bridge.py
#* excerpt from https://refactoring.guru/design-patterns/bridge/python/example
#*--------------------------------------------------

from __future__ import annotations
from abc import ABC, abstractmethod

class LaminasAbstraction(ABC):

    def __init__(self, implementation: LaminasImplementation) -> None:
        self.implementation = implementation

    @abstractmethod
    def producir_laminas(self) -> None:
        pass

class LaminasExtendedAbstraction(LaminasAbstraction):

    def producir_laminas(self) -> str:
        return (f"{self.implementation.producir_laminas_implementation()}")

class LaminasImplementation(ABC):

    @abstractmethod
    def producir_laminas_implementation(self) -> str:
        pass

class TrenLaminador5m(LaminasImplementation):

    def producir_laminas_implementation(self) -> str:
        return "Produciendo láminas de acero con un tren laminador de 5m."

class TrenLaminador10m(LaminasImplementation):

    def producir_laminas_implementation(self) -> str:
        return "Produciendo láminas de acero con un tren laminador de 10m."

def client_code(abstraction: LaminasAbstraction) -> None:

    print(abstraction.producir_laminas())

if __name__ == "__main__":
    """
    El código cliente debería poder trabajar con cualquier combinación preconfigurada de abstracción e implementación.
    """

    implementation_5m = TrenLaminador5m()


    abstraction_5m = LaminasExtendedAbstraction(implementation_5m)
    

    client_code(abstraction_5m)

    print("\n")


    implementation_10m = TrenLaminador10m()

    abstraction_10m = LaminasExtendedAbstraction(implementation_10m)

    client_code(abstraction_10m)

    print("\n")


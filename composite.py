from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Componente(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass

class Pieza(Componente):

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def operation(self) -> str:
        return f"Pieza: {self.nombre}"

class Conjunto(Componente):

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.componentes: List[Componente] = []

    def agregar(self, componente: Componente) -> None:
        self.componentes.append(componente)

    def remover(self, componente: Componente) -> None:
        self.componentes.remove(componente)

    def operation(self) -> str:
        resultado = [componente.operation() for componente in self.componentes]
        return f"Conjunto: {self.nombre}\n" + "\n".join(resultado)

if __name__ == "__main__":
    pieza1 = Pieza("Pieza 1")
    pieza2 = Pieza("Pieza 2")
    pieza3 = Pieza("Pieza 3")
    pieza4 = Pieza("Pieza 4")

    conjunto1 = Conjunto("Conjunto 1")
    conjunto2 = Conjunto("Conjunto 2")
    conjunto3 = Conjunto("Conjunto 3")

    conjunto1.agregar(pieza1)
    conjunto1.agregar(pieza2)
    conjunto1.agregar(pieza3)
    conjunto1.agregar(pieza4)

    conjunto2.agregar(pieza1)
    conjunto2.agregar(pieza2)
    conjunto2.agregar(pieza3)
    conjunto2.agregar(pieza4)

    conjunto3.agregar(pieza1)
    conjunto3.agregar(pieza2)
    conjunto3.agregar(pieza3)
    conjunto3.agregar(pieza4)

    print(conjunto1.operation())
    print("\n")
    print(conjunto2.operation())
    print("\n")
    print(conjunto3.operation())

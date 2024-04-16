#*--------------------------------------------------
#* decorator.py
#* excerpt from https://refactoring.guru/design-patterns/decorator/python/example
#*--------------------------------------------------

class Component:
    def operation(self) -> str:
        pass


class ConcreteComponent(Component):

    def __init__(self, valor: int) -> None:
        self._valor = valor

    def operation(self) -> str:
        return str(self._valor)


class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:

        return self._component

    def operation(self) -> str:
        return self._component.operation()

class SumarDos(Decorator):
    def operation(self) -> str:
        return str(int(self.component.operation()) + 2)


class MultiplicarPorDos(Decorator):
    def operation(self) -> str:
        return str(int(self.component.operation()) * 2)


class DividirPorTres(Decorator):
    def operation(self) -> str:
        return str(int(self.component.operation()) / 3)



def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end="")


if __name__ == "__main__":
    numero = ConcreteComponent(5)
    print("Numero ingresado:")
    client_code(numero)
    print("\n")

    decorator1 = SumarDos(numero)
    decorator2 = MultiplicarPorDos(decorator1)
    decorator3 = DividirPorTres(decorator2)
    print("(((Numero ingresado +2) * 2) / 3 ):")
    client_code(decorator3)

    print("\n")

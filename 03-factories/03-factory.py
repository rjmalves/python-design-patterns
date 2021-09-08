from enum import Enum
from math import cos, sin

# Uma alternativa à declaração dos métodos de construção
# do objeto na própria classe é a aplicação do SRP
# e, portanto, a definição destes em uma classe cujo
# propósito é criar o objeto.

class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


class PointFactory:

    @staticmethod
    def from_rectangular(x, y):
        return Point(x, y)

    @staticmethod
    def from_polar(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


# Uma forma melhor de organizar os conceitos é
# tornar a classe Factory uma classe interna.

class PointWithFactory:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


    class PointFactory:
        def from_rectangular(x, y):
            return Point(x, y)

        def from_polar(rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))


# Uma terceira forma é criar um objeto singleton
# como instância da classe interna e usá-lo.

class PointWithSingletonFactory:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


    class PointFactory:
        def from_rectangular(self, x, y):
            return Point(x, y)

        def from_polar(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))

    factory = PointFactory()



# Podemos usar os métodos:
if __name__ == "__main__":
    p1 = PointFactory.from_rectangular(1, 1)
    p2 = PointWithFactory.PointFactory.from_polar(1, 1)
    p3 = PointWithSingletonFactory.factory.from_polar(2, 1)
    print(p1)
    print(p2)
    print(p3)

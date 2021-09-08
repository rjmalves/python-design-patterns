from enum import Enum
from math import cos, sin

# Como uma primeira alternativa à criação de diferentes
# construtores em Python, definiremos métodos alternativos
# para a criação dos objetos, os Factory Method

class CoordinateSystem(Enum):
    RECTANGULAR = 0
    POLAR = 1


class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    # O que desejamos é um overload para __init__,
    # mas que não existe (construtor em coordenadas polares):
    # def __init__(self, rho, theta)

    # Uma outra alternativa era criar uma classe enum
    # para definir o tipo de coordenada e passar
    # como argumento opcional:
    # def __init__(self, a, b, system=CoordinateSystem.RECTANGULAR)

    # A melhor forma para atingir o objetivo desejado é criar
    # métodos alternativos para cada construção.
    # Sabendo que o construtor default recebe os parâmetros
    # em forma retangular

    @staticmethod
    def from_rectangular(x, y):
        return Point(x, y)

    @staticmethod
    def from_polar(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


# Podemos usar os métodos:
if __name__ == "__main__":
    p1 = Point.from_rectangular(1, 1)
    p2 = Point.from_polar(1, 1)
    print(p1)
    print(p2)

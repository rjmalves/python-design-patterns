
# A implementação clássica de Decorator é uma classe
# que expande a funcionalidade de outra.

# Supondo que estamos trabalhando com formas, que possuem
# apenas os atributos estritamente necessários

from abc import ABC


class Shape(ABC):
    def __str__(self):
        return ""


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f"A circle of radius {self.radius}"


class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side

    def __str__(self):
        return f"A square with side {self.side}"


# Agora desejamos trabalhar com formas que possuem cores.
# Não podemos herdar de Circle ou Square, porque desejamos
# adicionar a capacidade de lidar com cores em todas as
# formas.

class ColoredShape(Shape):
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def __str__(self):
        return f"{self.shape} has the color {self.color}"


# Podemos combinar vários decorators
class TransparentShape(Shape):
    def __init__(self, shape, transparency) -> None:
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f"{self.shape} has {self.transparency * 100}% transparency"


if __name__ == "__main__":
    circle = Circle(2)
    print(circle)

    # Se quisermos adicionar cor, podemos fazer
    red_cicle = ColoredShape(circle, "red")
    print(red_cicle)

    # Repare que não alteramos o código do Circle, então não
    # violamos o OCP.

    red_half_transparent_circle = TransparentShape(red_cicle, 0.5)
    print(red_half_transparent_circle)

    # Um lado ruim é que nada previne a aplicação repetida de um
    # decorator
    mixed = ColoredShape(ColoredShape(Square(3), "red"), "green")
    print(mixed)

    # Podemos tratar esta situação manualmente fazendo conferência
    # de tipos, mas pode ficar complicado de tratar de modo genérico.

    # Outro ponto é que não podemos usar os métodos específicos
    # das formas de modo transparente..
    # red_circle.resize(2) da erro..

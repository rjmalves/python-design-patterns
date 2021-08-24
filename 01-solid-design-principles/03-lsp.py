# LSP - Liskov Substituion Principle


# Vamos ilustrar o princípio através de um exemplo.
# Suponha que estamos desenvolvendo uma aplicação
# que tenha como entidades algumas formas geométricas,
# entre elas o retângulo. Podemos implementar:

class Rectangle:

    def __init__(self, height, width) -> None:
        self._height = height
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Width: {self.width}, height: {self.height}"


# Para trabalhar com o retângulo, vamos criar uma função
# que o usa:

def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f"Expected an area of {expected}, got {rc.area}")

rc = Rectangle(2, 3)
use_it(rc)

# Até o momento, não há problemas. Entretanto, vamos definir uma
# classe que herda de Rectangle e que irá tornar o nosso código
# inválido


class Square(Rectangle):
    def __init__(self, size) -> None:
        Rectangle.__init__(self, size, size)

    # Redefinimos os setters para garantir que alguém, ao alterar
    # um dos parâmetros, também altere o outro, mantendo a forma
    # de um quadrado.
    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value


# Todavia, a classe Square, da maneira como está definida, viola o
# Liskov Substitution Principle. Mais precisamente, vemos o restulado
# da chamada da função anterior:
sq = Square(5)
use_it(sq)

# Vemos que a função não tem o comportamento esperado. O princípio mencionado
# enuncia que, ao definir uma interface a partir de uma classe base, sempre
# que a classe base for usada em algum lugar, qualquer outra classe que
# herde da classe base também deve poder ser usada sem prejuízo algum.

# Logo, a classe Square não pode ser definida desta forma, pois a função
# use_it não sabe dizer se um Rectangle é um Square em particular.




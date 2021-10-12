# Para ilustrar o Bridge, vamos implementar um esquema
# de renderizacao de formas. Devemos renderizar as formas:
# Circle, Square
# Das maneiras:
# Vector, Raster

from abc import ABC


# Primeiro implementamos os renderizadores

# OBS: A implementacao como foi feita claramente fere o
# Open-Closed Principle, pois cada nova forma tem que ter
# a sua renderizacao implementada em todos os renderers.
# Tambem, se for feito um novo render ele deve reimplementar
# tudo para todas as formas..
# Mas este e o preco de ter a flexibilidade no uso.
# (Existem formas melhores de se fazer isso!)
class Renderer(ABC):
    def render_circle(self, radius):
        pass
    # render_square

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle of radius {radius}")

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing pixels for a circle of radius {radius}")


# Depois implementamos as formas

class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self): pass
    def resize(self, factor): pass


class Circle(Shape):

    # A "ponte" e estabelecida ao passar a interface como
    # parametro no construtor
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    # O uso do padrao bridge e feito na chamada da funcao
    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


# Usando o padrao
if __name__ == "__main__":
    raster = RasterRenderer()
    vector = VectorRenderer()
    raster_circle = Circle(raster, 2)
    vector_circle = Circle(vector, 5)
    raster_circle.draw()
    vector_circle.draw()
    vector_circle.resize(2)
    vector_circle.draw()

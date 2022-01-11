
class GraphicObject:
    def __init__(self, color=None):
        self.color = color
        self.children = []
        self._name = "Group"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    # Método de utilidade para emular o desenho
    # de um GraphicObject
    def _print(self, items, depth):
        items.append("*" * depth)
        if self.color:
            items.append(self.color)
        items.append(f"{self.name}\n")
        # Chama todos os child, aumentando o depth
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items, 0)
        return "".join(items)


class Circle(GraphicObject):

    # Para mostrar que é um Circle, sobrescreve-se o nome
    @property
    def name(self):
        return "Circle"


class Square(GraphicObject):

    @property
    def name(self):
        return "Square"


if __name__ == "__main__":
    drawing = GraphicObject()
    drawing.name = "My Drawing"
    drawing.children.append(Square("Red"))
    drawing.children.append(Circle("Yellow"))

    group = GraphicObject()
    group.children.append(Circle("Blue"))
    group.children.append(Square("Blue"))
    drawing.children.append(group)

    # Ao executar o print, um GraphicObject sabe imprimir
    # outros através do atributo children e o método _print
    print(drawing)

# Suponha que seja fornecida uma API que voce e obrigado
# a usar:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_point(p):
    print(".", end="")

# E voce desenvolveu um codigo para realizar suas tarefas
# de lidar com desenhos geometricos:

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


# Suponha que queremos definir uma funcao draw(), que recebe uma lista de Rectangle
# e desenha cada um deles. Para fazer isso, e necessario chamar a API
# recebida acima, que so desenha objetos Point. Para isso, vamos precisar
# criar um adaptador.

# Como um Rectangle e uma lista de Line, entao para desenhar um Rectangle
# precisamos saber apenas como desenhar Line. Mas nao existe uma descricao
# de Line em termos de Point, isso e o que precisamos fazer.

# O adaptador deve traduzir Line em termos de Point:
class LineToPointAdapter(list):
    count = 0

    def __init__(self, line):
        super().__init__()
        self.count += 1

        print(f"{self.count}: Generating points for line " +
              f"[{line.start.x}, {line.start.y}] ->" +
              f"[{line.end.x}, {line.end.y}]")

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = max(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(top, bottom):
                self.append(Point(left, y))
        elif bottom - top == 0:
            for x in range(left, right):
                self.append(Point(x, top))


# Desta forma podemos definir a funcao de desenho com o uso
# do adaptador
def draw(rectangles):
    print("\n\n--- Drawing some stuff ---\n")
    for r in rectangles:
        for line in r:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)


# Assim podemos chamar a funcao de desenho:

if __name__ == "__main__":
    recs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]

    # Todavia, iremos observar um problema em caso
    # de chamar a funcao de desenho 2 vezes:
    # Os pontos sao gerados a cada construcao do adaptador,
    # o que pode ainda ser otimizado.
    draw(recs)
    draw(recs)

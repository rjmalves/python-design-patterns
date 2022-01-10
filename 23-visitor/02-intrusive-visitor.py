# Como implementação para um Visitor,
# iremos implementar um sistema de avaliação
# de expressões matemáticas.

# Neste sistema poderemos printar as expressões,
# resolvê-las, etc..

# Inicialmente iremos suportar apenas adição entre
# números.


# Classe que representa uma expressão constante (valor)
class DoubleExpression:
    def __init__(self, value) -> None:
        self.value = value

    # O Visitor intrusivo é a própria implementação de um
    # método para realizar a tarefa em cada classe da
    # hierarquia. É indesejado, mas funciona.
    def print(self, buffer):
        buffer.append(str(self.value))

    # Além do print, se desejarmos a função eval, temos
    # que implementar em todas as classes
    def eval(self):
        return self.value

class AdditionExpression:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def print(self, buffer):
        buffer.append("(")
        self.left.print(buffer)
        buffer.append("+")
        self.right.print(buffer)
        buffer.append(")")

    def eval(self):
        return self.left.eval() + self.right.eval()


if __name__ == "__main__":
    # 1 + (2 + 3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    # Notamos que não existe um "visitor". O mais próximo
    # que temos é o buffer, que é o objeto em que os dados
    # são escritos.
    buffer = []
    e.print(buffer)
    print("".join(buffer) + " = " + str(e.eval()))

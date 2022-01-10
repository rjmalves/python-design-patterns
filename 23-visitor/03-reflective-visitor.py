from abc import ABC


class Expression(ABC):
    pass


class DoubleExpression(Expression):
    def __init__(self, value) -> None:
        self.value = value



class AdditionExpression(Expression):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right


# Agora iremos definir as funcionalidades desejadas
# em uma classe externa
class ExpressionPrinter:
    @staticmethod
    def print(e, buffer):
        # No momento, nossa única alternativa é, infelizmente,
        # checar o tipo
        if isinstance(e, DoubleExpression):
            buffer.append(str(e.value))
        elif isinstance(e, AdditionExpression):
            buffer.append("(")
            ExpressionPrinter.print(e.left, buffer)
            buffer.append("+")
            ExpressionPrinter.print(e.right, buffer)
            buffer.append(")")

    # Não é exatamente uma boa prática, mas funciona
    Expression.print = lambda self, b: ExpressionPrinter.print(self, b)


# O nome dessa abordagem é "reflection" porque em algumas linguagens de
# programação, checar o tipo é uma operação chamada de reflexão.

# De outra forma, o lado ruim desse método é que ao adicionar outra operação,
# como por exemplo subtração, então é necessário alterar o método print
# do ExpressionPrinter, violando o OCP.


if __name__ == "__main__":
    # 1 + (2 + 3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    buffer = []
    e.print(buffer)
    print("".join(buffer))

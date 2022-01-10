def _qualname(obj):
    """Get the fully-qualified name of an object (including module)."""
    return obj.__module__ + '.' + obj.__qualname__


def _declaring_class(obj):
    """Get the name of the class that declared an object."""
    name = _qualname(obj)
    return name[:name.rfind('.')]


# Stores the actual visitor methods
_methods = {}


# Delegating visitor implementation
def _visitor_impl(self, arg):
    """Actual visitor method implementation."""
    method = _methods[(_qualname(type(self)), type(arg))]
    return method(self, arg)


# The actual @visitor decorator
def visitor(arg_type):
    """Decorator that creates a visitor method."""

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # Replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator


# O visitor clássico pode ser refinado, já que os métodos
# accept são herdados de linguagens de tipagem estática.
# O próprio printer pode chamar o visit diretamente.
class DoubleExpression:
    def __init__(self, value) -> None:
        self.value = value


class AdditionExpression:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right


# Para adicionar uma nova expressão, criamos a classe
class SubtractionExpression:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right


# A classe responsável pelo print agora tem métodos
# específicos para tratar cada expressão
class ExpressionPrinter:

    def __init__(self) -> None:
        self.buffer = []

    @visitor(DoubleExpression)
    def visit(self, de):
        self.buffer.append(str(de.value))

    @visitor(AdditionExpression)
    def visit(self, ae):
        self.buffer.append("(")
        self.visit(ae.left)
        self.buffer.append("+")
        self.visit(ae.right)
        self.buffer.append(")")

    # Ao adicionar uma nova operação, precisamos
    # adicionar o seu visitor também
    @visitor(SubtractionExpression)
    def visit(self, se):
        self.buffer.append("(")
        self.visit(se.left)
        self.buffer.append("-")
        self.visit(se.right)
        self.buffer.append(")")


    def __str__(self):
        return "".join(self.buffer)



# Podemos também fazer outro Visitor. No caso,
# vamos implementar um avaliador de expressões
class ExpressionEvaluator:

    def __init__(self) -> None:
        self.value = 0

    @visitor(DoubleExpression)
    def visit(self, de):
        self.value = de.value

    @visitor(AdditionExpression)
    def visit(self, ae):
        self.visit(ae.left)
        temp = self.value
        self.visit(ae.right)
        self.value += temp

    @visitor(SubtractionExpression)
    def visit(self, se):
        self.visit(se.right)
        temp = self.value
        self.visit(se.left)
        self.value -= temp

    def __str__(self):
        return str(self.value)


# Esta é provavelmente a melhor maneira de implementar
# o padrão Visitor em Python.

if __name__ == "__main__":
    # 1 + (2 - 3)
    e = AdditionExpression(
        DoubleExpression(1),
        SubtractionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    ep = ExpressionPrinter()
    ep.visit(e)
    ee = ExpressionEvaluator()
    ee.visit(e)
    print(f"{ep}={ee}")

# Para eliminar a necessidade de fazer verificação
# de tipos, iremos usar um decorator que simula uma funcionalidade
# de despacho múltiplo em python.

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



# Em relação aos métodos anteriores, as expressões agora
# tem um método de aceitação de um visitante
class DoubleExpression:
    def __init__(self, value) -> None:
        self.value = value

    def accept(self, visitor):
        visitor.visit(self)


class AdditionExpression:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def accept(self, visitor):
        visitor.visit(self)


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
        ae.left.accept(self)
        self.buffer.append("+")
        ae.right.accept(self)
        self.buffer.append(")")

    # O método de print para facilitar
    def __str__(self):
        return "".join(self.buffer)


# Esta abordagem é muito mais escalável e prática
# em relação a anterior, pois não faz necessário a
# verificação de tipos, implementando algo que, do
# ponto de vista do desenvolvedor, é um despacho duplo.

if __name__ == "__main__":
    # 1 + (2 + 3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    ep = ExpressionPrinter()
    ep.visit(e)
    print(ep)

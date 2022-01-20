
# Para ilustrar o Interpreter, iremos implementar um interpretador
# de expressões matemáticas simplificado.
# Iremos tolerar apenas adição e subtração de números inteiros.

from enum import Enum, auto

# A classe TokenType é um enumerador dos possíveis tipos de token
class TokenType:
    INTEGER = auto()
    PLUS = auto()
    MINUS = auto()
    LPAREN = auto()
    RPAREN = auto()


# A classe Token representa os tokens extraídos da string
class Token:

    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __str__(self):
        return f"`{self.text}`"


# A função lex é a responsável pelo processo de lexing, de quebrar
# a string em tokens significativos, léxicos.
def lex(input):
    result = []
    i = 0
    while i < len(input):
        if input[i] == "+":
            result.append(Token(TokenType.PLUS, "+"))
        elif input[i] == "-":
            result.append(Token(TokenType.MINUS, "-"))
        elif input[i] == "(":
            result.append(Token(TokenType.LPAREN, "("))
        elif input[i] == ")":
            result.append(Token(TokenType.RPAREN, ")"))
        else:
            digits = [input[i]]
            for j in range(i + 1, len(input)):
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1
                else:
                    result.append(Token(TokenType.INTEGER,
                                        "".join(digits)))
                    break
        i += 1
    return result


# Para poder processar os valores (parsing), iremos definir a
# classe dos inteiros
class Integer:
    def __init__(self, value) -> None:
        self.value = value

# Para armazenar as expressões e operações iremos definir operações
# binárias, e também os seus possíveis tipos

class BinaryExpressionType(Enum):
    ADDITION = auto()
    SUBTRACTION = auto()


class BinaryExpression:
    def __init__(self) -> None:
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == BinaryExpressionType.ADDITION:
            return self.left.value + self.right.value
        elif self.type == BinaryExpressionType.SUBTRACTION:
            return self.left.value - self.right.value
        else:
            return None

# Para a interpretação, vamos definir a etapa de parsing
def parse(tokens):
    result = BinaryExpression()
    have_lhs = False
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.type == TokenType.INTEGER:
            integer = Integer(int(token.text))
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        elif token.type == TokenType.PLUS:
            result.type = BinaryExpressionType.ADDITION
        elif token.type == TokenType.MINUS:
            result.type = BinaryExpressionType.SUBTRACTION
        elif token.type == TokenType.LPAREN:
            j = i
            while j < len(tokens):
                if tokens[j].type == TokenType.RPAREN:
                    break
                j += 1
            subexpression = tokens[i + 1:j]
            element = parse(subexpression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            i = j
        i += 1
    return result

# A função calc é a função principal, que recebe a string e calcula
def calc(input):
    tokens = lex(input)
    print(" ".join(map(str, tokens)))
    expression = parse(tokens)
    print(f"{input} = {expression.value}")


if __name__ == "__main__":
    calc("(13+4)-(12+1)")
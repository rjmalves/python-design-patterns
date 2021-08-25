# Creational Patterns
# Builder

# Motivação
# Alguns objetos são simples e podem ser criados em apenas uma
# linha de inicialização.
# Alguns outros objetos necessitam de muita "cerimônia" para
# serem criados.
# Ter um objeto com 10 ou mais argumentos de inicialização
# não é produtivo. Dessa forma, optamos por uma construção
# por partes.
# O padrão builder provê uma API para construir um objeto
# passo a passo.

# Definição formal:
# Quando a construção por partes de um objeto for complicada,
# o padrão Builder provê uma API para torná-la simples.


# Suponha que é desejado construir um parágrafo com texto, e no
# caso particular é desejado fazer um parágrafo em HTML.

# Nesse caso simples, podemos fazer o parágrafo em duas linhas
text = "hello"
parts = ["<p>", text, "</p>"]
print("".join(parts))

# No caso de querer escrever uma lista, temos uma situação um
# pouco mais complicada, que nós gastamos 4 linhas.
words = ["hello", "world"]
parts = ["<ul>"]
for w in words:
    parts.append(f"    <li>{w}</li>")
parts.append("</ul>")
print("\n".join(parts))

# Vemos que a medida que desejamos um elemento HTML mais complexo,
# precisamos de uma lógica mais complicada, que não é ideal de
# ser repetida e customizada a cada vez que se desejar construir
# um objeto HTML. Desta forma, é uma boa ideia levar essa complexidade
# de construção para uma entidade que seja responsável exclusivamente
# por isso. Em particular, podemos usar orientação a objetos.

class HtmlElement:

    indent_size = 2

    def __init__(self, name="", text="") -> None:
        self.text = text
        self.name = name
        # Um elemento HTML pode conter um número qualquer de
        # elementos dentro dele, portanto vamos definir esse
        # atributo.
        self.elements = []

    # Para resolver o problema de printar um elemento HTML, que
    # é uma tarefa recursiva, vamos definir um método auxiliar
    def __str(self, indent):
        lines = []
        i = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{self.text}")

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def __str__(self):
        return self.__str(0)


# Uma vez que o nosso elemento a ser construído está bem
# definido, podemos criar uma classe para auxiliar a construção,
# o Builder.

class HtmlBuilder:

    def __init__(self, root_name) -> None:
        self.root_name = root_name
        # Criamos o objeto raiz
        self.__root = HtmlElement(name=root_name)

    # Para printar, usamos a própria raiz
    def __str__(self) -> str:
        return str(self.__root)

    # Podemos agora criar a API de construção
    def add_child(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))

    # Podemos tornar a API ainda melhor ao criar uma
    # fluent interface
    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))
        return self

# Agora podemos fazer uso do builder
builder = HtmlBuilder("ul")
builder.add_child("li", "hello")
builder.add_child("li", "world")
print("Ordinary builder:")
print(builder)

# Podemos testar também o fluent builder
fluent = HtmlBuilder("ul")
fluent.add_child_fluent("li", "hello").add_child_fluent("li", "world")
print("Fluent builder:")
print(fluent)

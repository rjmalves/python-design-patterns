# OCP

# Vamos ilustrar um princípio de design chamado "Open-Closed Principle"
# através de um exemplo.

# Vamos montar abaixo um exemplo de código para realizar a classificação
# de um objeto, no caso um Product, segundo alguns atributos específicos,
# aqui representado pelos enums Color e Size.

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size) -> None:
        self.name = name
        self.color = color
        self.size = size


# Para realização dos filtros, podemos, por exemplo, criar a
# classe ProductFilter, que inicialmente pode conter apenas
# um método: filter_by_color.
# Então essa classe é testada, são construídos testes automáticos
# para ela e esse código é posto em produção.

class ProductFilter:

    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

    # Surge a necessidade de realizar a filtragem também por tamanho.
    # Para isso, é necessário alterar a classe adicionando mais um método
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    # Ao implementar o método anterior, foi violado o:
    # Open-Closed Principle = open for extension, closed for modification

    # Em resumo, classes devem ser fechadas para modificação. Uma vez que
    # foi construída uma classe, que foi testada e então posta em produção,
    # se for necessário adicionar mais funcionalidades, isso deve ser feito
    # através de uma extensão, não de modificação do código já validado.

    # Surge então a necessidade de realizar a filtragem combinada.
    # Agora devemos filtrar por cor e tamanho. Assim sendo:
    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color: yield p

    # Assim chegamos a outro problema: explosão do espaço de estados.
    # Com apenas 2 critérios, precisamos de pelo menos três funções.
    # Ainda poderíamos filtrar por um critério OU outro, etc...
    # Com 3 critérios, temos já pelo menos 7 funções.
    # Então, ao violar o OCP, encaramos este tipo de problemas.


# Uma solução para contornar esse problema vem do estudo dos
# enterprise patterns. Em especial, temos o padrão chamado:

# Specification

# Construiremos duas classes para resolver esse problema: uma
# chamada Specification e outra Filter.
# No que será implementado, as classes Specification tratam
# de resolver o problema de avaliar de um determinado produto
# atendem ou não a uma condição. A classe Filter apenas aplica
# uma Specification a um conjunto de Products.


# Essa é uma classe base, deve ter seu método sobrescrito
class Specification:

    def is_satisfied(self, item):
        pass

    # Comentar e desconsiderar até ser mencionado
    def __and__(self, other):
        return AndSpecification(self, other)


# Essa também é uma classe base
class Filter:

    # O método filter recebe uma lista
    def filter(self, items, spec):
        pass


# Por exemplo, vamos agora criar especificações
class ColorSpecification(Specification):

    def __init__(self, color) -> None:
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):

    def __init__(self, size) -> None:
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


# E uma implementação específica para o filtro de produto
class BetterFilter(Filter):

    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


apple = Product("Apple", Color.GREEN, Size.SMALL)
tree = Product("Tree", Color.GREEN, Size.LARGE)
house = Product("House", Color.BLUE, Size.LARGE)

products = [apple, tree, house]
pf = ProductFilter()
print("Green products (old):")
for p in pf.filter_by_color(products, Color.GREEN):
    print(f" - {p.name} is GREEN")

bf = BetterFilter()
print("Green products (new):")
green = ColorSpecification(Color.GREEN)
for p in bf.filter(products, green):
    print(f" - {p.name} is GREEN")

print("Large products (new):")
large = SizeSpecification(Size.LARGE)
for p in bf.filter(products, large):
    print(f" - {p.name} is LARGE")


# Agora, se desejamos implementar um filtro combinado,
# não precisamos modificar nenhuma das classes já testadas,
# mas apenas extender a implementação.
class AndSpecification(Specification):

    def __init__(self, *args) -> None:
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item),
                       self.args))


# Desta forma, podemos fazer filtros combinados
blue = ColorSpecification(Color.BLUE)
large_blue = AndSpecification(large, blue)
print("Large blue products (new):")
for p in bf.filter(products, large_blue):
    print(f" - {p.name} is LARGE and BLUE")


# Apesar de agora seguirmos o OCP, a sintaxe ficou razoavelmente pior.
# Em Python, podemos utilizar a sobrescrita de operadores para tornar
# a utilização melhor. Não podemos sobrescrever a palavra chave "and",
# mas podemos fazer isso com o "E LÓGICO" (voltar à definição da classe
# Specification e descomentar a definição do método __and__).

# Assim podemos fazer:
large_blue = large & blue
print("Large blue products (new with &):")
for p in bf.filter(products, large_blue):
    print(f" - {p.name} is LARGE and BLUE")
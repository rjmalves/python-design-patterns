
# Uma maneira diferente de usar o padrão iterator
# é com propriedades armazenadas em listas.

# Por exemplo, num jogo onde existe a classe Creature,
# que possui diferentes atributos.
# Ao invés de criar cada atributo individualmente, podemos
# criar uma lista de atributos, e isso facilita bastante
# algumas operações.

class Creature:
    _strength = 0
    _agility = 1
    _intelligence = 2

    def __init__(self):
        self.stats = [10, 11, 12]
        # self._strength = 10
        # self._agility = 11
        # self._intelligence = 12

    @property
    def strength(self):
        return self.stats[Creature._strength]
        # return self._strength

    @strength.setter
    def strength(self, value):
        self.stats[Creature._strength] = value
        # self._strength = value

    @property
    def sum_of_stats(self):
        return sum(self.stats)
        # return sum(self.strength + self.agility + self.intelligence)

    @property
    def max_stat(self):
        return max(self.stats)
        # return max(self.strength, self.agility, self.intelligence)

    @property
    def average_of_stats(self):
        return float(self.sum_of_stats) / len(self.stats)
        # return self.sum_of_stats / 3.0

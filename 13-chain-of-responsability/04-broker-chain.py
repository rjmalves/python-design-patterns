# Vamos implementar a mesma tarefa de modificadores em
# um jogo de cartas, porém agora usando uma abstração
# de um broker de eventos para lidar com a cadeia de
# responsabilidade.

# Vamos usar alguns conceitos:
#   - Padrão Observer
#   - CQS
#   - Event Broker


# Primeiramente iremos definir a classe base de um evento,
# que é uma lista de funções a serem chamadas no momento
# que ele ocorre (callbacks).

from abc import ABC
from typing import Any
from enum import Enum


class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for item in self:
            item(*args, **kwds)

# Definimos a classe do broker de eventos, que no caso é
# a própria partida em questão.
class Game:
    def __init__(self):
        # Temos apenas um evento, que é o próprio jogo.
        # Este é o broker que recebe as queries.
        self.queries = Event()

    # Fazer a query é chamar o evento
    def perform_query(self, sender, query):
        self.queries(sender, query)


# Definimos agora a query. Primeiramente, os tipos de query:
class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, creature_name, what_to_query, default_value) -> None:
        self.creature_name = creature_name
        self.what_to_query = what_to_query
        # O nome interno é value, porque este será modificado
        self.value = default_value


# Definimos também a classe base para aplicar os modificadores
# (os que escutam os eventos).
class CreatureModifier(ABC):
    def __init__(self, game, creature) -> None:
        self.game = game
        self.creature = creature
        # No momento da criação do modificador, ele já
        # se inscreve para ouvir o evento, submetendo a sua
        # função de tratamento (modificação)
        self.game.queries.append(self.handle)

    # Na classe base, a modificação não é nada
    def handle(self):
        pass

    # Podemos sobrescrever também as funções de entrada e saída
    # em contextos, para poder funcionar corretamente dentro
    # dos blocos with
    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.game.queries.remove(self.handle)


# Definimos alguma modificação concreta
class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if (sender.name == self.creature.name and query.what_to_query == WhatToQuery.ATTACK):
            query.value *= 2


# Então definimos a classe base das criaturas
class Creature:
    def __init__(self, game, name, attack, defense) -> None:
        self.game = game
        self.name = name
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def attack(self):
        # A propriedade é a maneira de realizar queries.
        # O valor de attack é determinado no instante em que é
        # solicitado.
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        # A propriedade é a maneira de realizar queries.
        # O valor de defense é determinado no instante em que é
        # solicitado.
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"


if __name__ == "__main__":
    # Nesta abordagem, tudo gira em torno do broker
    game = Game()

    # Criamos a criatura sem modificadores
    goblin = Creature(game, "Strong Goblin", 2, 2)
    print(goblin)

    # Criamos um modificador dentro de um contexto
    with DoubleAttackModifier(game, goblin):
        print(goblin)

    # O goblin deixa de ser modificado quando sai do contexto
    print(goblin)

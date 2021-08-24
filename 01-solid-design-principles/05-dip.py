# DIP - Dependency Inversion Principle

# OBS: Não se relaciona com o conceito de dependency injection

# O conceito do princípio é o seguinte: módulos (classes) de alto nível
# no código não devem depender diretamente dos módulos (classes) de mais
# baixo nível, mas sim de abstrações.
# Por abstrações se quer dizer interfaces. Dessa maneira, é possível trocar
# uma implementação de mais baixo nível por outra, sem prejuízo.


# Por exemplo, supomos que estamos resolvendo um problema de genealogia.
# Vamos definir um enum para os possíveis relacionamentos.

from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name) -> None:
        self.name = name


# Para armazenar todas as interações entre as pessoas da árvore,
# precisamos de uma classe base para isso.

class Relationships:

    def __init__(self) -> None:
        self.relations = []

    # A função responsável por guardar os relacionamentos
    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))


# Vamos agora, para quebrar o princípio, vamos definir uma classe
# que faz buscas nos relacionamentos. Vamos fazer uma busca muito
# particular pelos filhos de John

class Research:

    def __init__(self, relationships) -> None:
        relations = relationships.relations
        for r in relations:
            if r[0].name == "John" and r[1] == Relationship.PARENT:
                print(f"John has a child called {r[2].name}")


# Vamos testar a implementação definindo os objetos de teste
parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)
research = Research(relationships)

# A implementação atual funciona. Porém, vemos que a classe Research faz
# acessos internos à Relationships. Ela assume que o retorno da propriedade
# "relations" retorna algo iterável (o que é razoável), e também assume
# que existem os objetos de índices 0, 1 e 2, e ainda assume os seus tipos.

# Se a implementação de Relationships mudar, trocar de list para dict, ou
# trocar os elementos individuais de tuplas para algo mais otimizado e
# específico, todo o código irá quebrar.

# Para corrigir este problema, vamos definir uma interface

from abc import abstractmethod


class RelationshipBrowser:

    @abstractmethod
    def find_all_children_of(self, name):
        pass


# Dessa forma, a busca agora é feita na própria classe que conhece a sua
# estrutura interna de armazenamento. Assim, a classe de alto nível não
# precisa saber detalhes internos da classe de mais baixo nível, só que
# ela atende uma certa interface.
# Podemos reimplementar a classe:

class BetterRelationships(RelationshipBrowser):

    def __init__(self) -> None:
        self.relations = []

    # A função responsável por guardar os relacionamentos
    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    # A implementação para atender à interface
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


# Dessa forma a classe Research se torna:

class BetterResearch:

    def __init__(self, browser) -> None:
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p}")


# Podemos testar a nova implementação
relationships = BetterRelationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)
research = BetterResearch(relationships)

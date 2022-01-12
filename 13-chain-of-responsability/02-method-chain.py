
# No caso de um jogo de cartas onde as cartas podem receber
# modificadores, temos uma classe base para as cartas de criaturas.
class Creature:
    def __init__(self, name, attack, defense) -> None:
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"


# Uma classe base para os modificadores de cartas de criaturas
class CreatureModifier:
    def __init__(self, creature) -> None:
        self.creature = creature
        self.next_modifier = None

    # Os modificadores são adicionados em uma forma de cadeia.
    # Se já existe um próximo, então tenta adicionar como próximo
    # deste. Senão, adiciona como próximo no atual.
    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    # O tratamento base é chamar o handle() no próximo
    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


# A implementação de um Modifier concreto é realizar a alteração
# na criatura e depois chamar o tratamento base, que pula para
# o próximo, na ordem em que foram adicionados.
class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Doubling {self.creature.name}'s attack")
        self.creature.attack *= 2
        super().handle()


class IncresaseDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            print(f"Increasing {self.creature.name}'s defense")
            self.creature.defense += 1
        super().handle()


# Podemos também criar um modificador que limpa todas as alterações,
# pois não chama o tratamento base
class NoBonusesModifier(CreatureModifier):
    def handle(self):
        print(f"No bonuses for {self.creature.name}")


if __name__ == "__main__":
    goblin = Creature("Goblin", 1, 1)
    print(goblin)

    root = CreatureModifier(goblin)

    # Se descomentar, o globin não é alterado
    # root.add_modifier(NoBonusesModifier(goblin))

    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncresaseDefenseModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncresaseDefenseModifier(goblin))

    root.handle()
    print(goblin)

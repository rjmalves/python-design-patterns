from enum import Enum, auto
from abc import ABC

# Quando se tem uma hierarquia de objetos para serem
# construídos, isso é refletido em uma hierarquia de
# Factories. Com isso, fazemos uma classe base abstrata.

# Os objetos a serem criados serão "bebidas quentes"
class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("This tea is delicious!")


class Coffee(HotDrink):
    def consume(self):
        print("This coffee is delicious!")


# Os Factories:
class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print("Put in tea bag, boil water,",
              f" pour {amount}ml, enjoy!")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print("Grind some beans, boil water,",
              f" pour {amount}ml, enjoy!")
        return Coffee()


# Poderíamos criar um método para fabricar bebidas quentes,
# responsável por construir cada uma das bebidas que estão
# disponíveis
def make_drink():
    type = input("Choose a drink: ")
    if type == "tea":
        return TeaFactory().prepare(200)
    elif type == "coffee":
        return CoffeeFactory().prepare(50)
    else:
        return None


# De fato esta abordagem funciona, mas tem alguns problemas.
# Por exemplo, sempre que uma nova bebida for adicionada,
# é necessário alterar o método make_drink, que está na raiz.
# Também, não existe relação entre a palavra-chave e a bebida,
# a priori. O usuário deve saber quais são as palavras-chave
# aceitas e escolher a bebida a partir disso.

# Podemos fazer de outra forma, eliminando o primeiro dos problemas.
# Apesar desta abordagem violar o OCP, vamos definir um enum
# que contém as bebidas quentes suportadas dentro da "máquina de bebidas":

class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self) -> None:
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                # Assumindo que os enums são as bebidas em caps
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + "Factory"
                # É extremamente inseguro usar isso,
                # somente usar em demonstrações
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print("Available drinks:")
        for f in self.factories:
            print(f[0])
        
        s = input(f"Please pink drink ({0}-{len(self.factories)-1}): ")
        idx = int(s)
        s = input(f"Specify amount: ")
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


if __name__ == "__main__":
    # Usando a primeira abordagem:
    make_drink()

    # Com a segunda abordagem:
    hdm = HotDrinkMachine()
    hdm.make_drink()

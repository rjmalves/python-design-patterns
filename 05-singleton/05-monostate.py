# Existe uma outra abordagem para definicao de um singleton,
# que consiste em instanciar todos os atributos como um
# dicionario estatico na classe, e fazer com que todas as
# novas instancias usem o mesmo conjunto de atributos.

class CEO:
    __shared_state = {
                      "name": "Steve",
                      "age": 55
                     }
    
    def __init__(self):
        self.__dict__ = CEO.__shared_state

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"


# Essa abordagem pode ser mais generica fazendo uma classe
# base que ja faz isso no metodo alocador.

class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    def __init__(self):
        self.name = ""
        self.money_managed = 0

    def __str__(self):
        return f"{self.name} manages {self.money_managed}"


# Testando
if __name__ == "__main__":
    ceo1 = CEO()
    print(ceo1)

    ceo2 = CEO()
    ceo2.age = 77
    print(ceo1)
    print(ceo2)

    cfo1 = CFO()
    cfo1.name = "Steve"
    cfo1.money_managed = 1
    print(cfo1)

    cfo2 = CFO()
    cfo2.name = "Ruth"
    cfo2.money_managed = 10
    print(cfo1)
    print(cfo2)

# Apesar do monostate funcionar bem, a melhor maneira de se implementar
# um singleton e atraves de decorators ou metaclasses.

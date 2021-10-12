# Para demonstrar o processo de inicializacao de um
# objeto em Python, vamos criar uma interface
# com um banco de dados.

from random import randint


class Database:

    # Criamos uma instancia como um atributo
    # estatico.
    _instance = None

    # Sobrescrevemos o alocador, que e chamado
    # antes do inicializador __init__
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls)\
                .__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        print(f"Criando um novo objeto, id = {randint(1, 101)}")


# Apesar de isso ser suficiente para algumas aplicacoes,
# da maneira que foi feito o metodo __init__ acaba sendo
# chamado 2 vezes.



if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print (d1 == d2)
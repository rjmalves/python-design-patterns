# Functional decorators existem em python por default.
# Não é a forma clássica do Design Pattern, mas é iteressante.

import time


# Supondo que temos uma função cuja execução é demorada e
# desejamos fazer uma medição de tempo. Podemos fazer isso
# definindo uma função que recebe uma função e retorna a
# medição de tempo da sua execução.

# Melhor ainda, podemos definir uma função que modifica
# uma função para que ela seja medida sempre que executada.


def time_it(func):

    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"{func.__name__} took {int((end-start) * 1000)}ms")
        return result

    return wrapper


# A sintaxe especial de Python para esse caso
@time_it
def some_op():
    print("Starting op")
    time.sleep(1)
    print("We are done")
    return 123


if __name__ == "__main__":
    some_op()

    # Podemos chamar assim
    # time_it(some_op)()

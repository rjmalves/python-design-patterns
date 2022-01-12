
# Iremos implementar a estratégia de economia de
# espaço para o caso de armazenamento de nomes
# de pessoas em um banco de dados.

import random
import string

# Esta implementação é intuitiva, porém gasta
# muito espaço, pois armazena o nome como uma string
# completa.
class User:
    def __init__(self, name) -> None:
        self.name = name

# Esta implementação, apesar de mais complexa, é muito
# mais eficiente em termos de espaço.
# Porém, há um tradeoff de processamento.
class UserFlyweight:
    strings = []

    def __init__(self, name) -> None:

        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        self.names = [get_or_add(s) for s in
                      name.split(" ")]

    def __str__(self):
        return " ".join([self.strings[i] for i in self.names])


# Para emular, vamos fazer um teste com nomes aleatórios
def random_string():
    chars = string.ascii_lowercase
    return "".join(
        random.choice(chars) for _ in range(8)
    )


if __name__ == "__main__":
    # Gera os usuários
    users = []
    first_names = [random_string() for _ in range(100)]
    last_names = [random_string() for _ in range(100)]
    for first in first_names:
        for last in last_names:
            users.append(UserFlyweight(f"{first} {last}"))
    # Ao final, podemos conferir o tamanho da lista
    # de nomes, que é armazenada apenas uma vez.
    print(users[0])
    n_chars_user = 17 * len(users)
    n_chars_fly = 8 * len(UserFlyweight.strings)
    print(f"Ao invés de armazenar (8 * 2 + 1) * {len(users)} = {n_chars_user} caracteres," +
          f" estão sendo armazenados 8 * {len(UserFlyweight.strings)} = {n_chars_fly}")

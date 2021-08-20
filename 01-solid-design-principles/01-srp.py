# SRP SOC

# Uma classe deve ter apenas uma responsabilidade.
# Não vale a pena criar uma classe só para lidar com tudo.
# Por isso o nome do princípio:

# Single Responsability Principle
# ou
# Separation of Concerns

# A implementação da classe Journal como uma classe
# responsável por gerenciar as entradas é saudável.

# Tentar lidar com coisas como "salvar no disco"
# e "carregar do disco" pode sobrecarregar a classe.

# Desta forma seriam adicionadas mais "preocupações"
# ou "responsabilidades" à classe e, portanto, não é
# recomendado.

class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        self.count -= 1
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # Estes métodos não são recomendados, pois sobrecarregam
    # as reponsabilidades de Journal.
    # Tratar com salvar e carregar o objeto leva a uma série
    # de problemas (persistência), além de poder ser feito
    # em vários domínios.
    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass


# Esta classe possui uma única responsabilidade, que é a manutenção
# da persistência de um objeto em disco, por exemplo.
# É uma maneira mais indicada de tratar o problema do que sobrecarregar
# a classe Journal.
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today")
j.add_entry("I ate a bug")
print(f"Journal entries:\n{j}")
file = "journal.txt"
PersistenceManager.save_to_file(j, file)
with open(file) as fh:
    print(fh.read())


# Tentar carregar tudo na classe Journal cria o que chamamos de
# "God Object", que é um anti-pattern (algo que se opôe a um padrão)

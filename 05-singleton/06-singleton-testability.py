# Um dos problemas apontados ao fazer uso do padrao
# singleton sao as dificuldades na hora de realizar testes.

# Supondo que temos uma classe Database, que e um singleton
# que no seu processo de inicializacao carrega dados de
# arquivos no disco.

# Para implementar o Singleton sera usada a metaclasse

import unittest

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls)\
                .__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.population = {}
        f = open("05-singleton/capitals.txt", "r")
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            self.population[lines[i].strip()] =\
                int(lines[i + 1].strip())
        f.close()


# Vamos definir classes que manipulam os dados fornecidos pela
# base de dados. Veremos que esta classe tem um problema
# com relacao a usar dados brutos diretamente. Ela depende de
# maneira inflexivel da Database.
class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for c in cities:
            result += Database().population[c]
        return result


# A clase abaixo nao tem os problemas da anterior, como sera visto
# mais a frente
class ConfigurableRecordFinder:
    def __init__(self, db) -> None:
        self.db = db
    def total_population(self, cities):
        result = 0
        for c in cities:
            result += self.db.population[c]
        return result


# Agora vamos escrever testes para essas classes.

class DummyDatabase:
    population = {
        "alpha": 1,
        "beta": 2,
        "gamma": 3
    }


class SingletonTests(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    # Este teste tem um problema serio: esta sendo feito
    # com base em dados reais, lidos de arquivos.
    def test_singleton_total_population(self):
        rf = SingletonRecordFinder()
        names = ["Tokyo", "Berlin"]
        tp = rf.total_population(names)
        self.assertEqual(tp, 17685000)

    # Variavel usada nos testes
    testdb = DummyDatabase()

    # Teste melhor que o anterior
    def test_singleton_total_population_better(self):
        rf = ConfigurableRecordFinder(SingletonTests.testdb)
        names = ["alpha", "beta"]
        tp = rf.total_population(names)
        self.assertEqual(tp, 3)

if __name__ == "__main__":
    unittest.main()

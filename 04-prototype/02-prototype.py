
# Vamos criar uma classe Person que tem um nome e um endereço, que é
# uma outra classe Address

class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.country}"

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives as {self.address}"


# Se tentarmos criar uma pessoa a partir de outra já existente,
# como por exemplo no caso abaixo com jane a partir de john,
# temos um problema, pois eles são uma referência ao mesmo objeto

john = Person("John", Address("123 London Road", "London", "UK"))
print(john)
jane = john
jane.name = "Jane"
print("----")
print(john)
print(jane)

# Uma possível solução seria criarmos os dois objetos a partir do
# construtor base, declarando os atributos que eles possuem por fora
# e aproveitando para ambos.

address = Address("123 London Road", "London", "UK")
john = Person("John", address)
jane = Person("Jane", address)
print("---")
print(john)
print(jane)

# Neste caso simples funciona, mas se as classes possuíssem vários atributos
# em comum, teríamos um problema de escalabilidade. Ainda, se quisermos
# alterar o endeço apenas de john, veremos que alteramos o de todos
# que foram criados com aquele mesmo objeto

john.address.street_address = "123B London Road"
print("---")
print(john)
print(jane)

# Por isso, teremos que usar o recurso de cópia. Um dos nossos objetos servirá
# de "protótipo" para o outro, sendo copiado e tendo os atributos de interesse
# alterados
from copy import deepcopy
john = Person("John", Address("123 London Road", "London", "UK"))
jane = deepcopy(john)
jane.name = "Jane"
jane.address.street_address = "124 London Road"
print("---")
print(john)
print(jane)

# Este é um exemplo de uso do Prototype.
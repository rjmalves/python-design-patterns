# Às vezes desejamos construir um objeto que é composto de
# muitos atributos, que podem ser categorizados em alguns
# grupos de atributos.

# Nestes casos, precisamos de mais de um Builder. Vamos ver como
# fazer para construir de maneira adequada um objeto destes.
# O nosso exemplo será de um pessoa (Person), que possuirá atributos
# relativos ao seu endereço e a algumas propriedades sobre o emprego.

class Person:
    def __init__(self) -> None:
        # Endereço
        self.street_address = None
        self.postcode = None
        self.city = None
        # Emprego
        self.company_name = None
        self.position = None
        self.annual_income = None

    # Um método de reprodução para debug
    def __str__(self):
        return (f"Address: {self.street_address}, {self.postcode}, {self.city} \n" +
                f"Employed at {self.company_name} as a {self.position} earning {self.annual_income}")


# Como vamos construir vários Builder, então vamos definir uma
# classe base para servir de referência para todos.

class PersonBuilder:

    def __init__(self, person=Person()) -> None:
        self.person = person

    # Para a classe base usar os outros Builder, podemos
    # definir propriedades
    @property
    def works(self):
        return PersonEmploymentBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


# Vamos também definir dois Builder, um para as informações de endereço
# e outro para as informações de emprego

class PersonEmploymentBuilder(PersonBuilder):

    def __init__(self, person) -> None:
        super().__init__(person=person)

    # Interface fluente para o nome da companhia
    def at(self, company_name):
        self.person.company_name = company_name
        return self

    # Interface fluente para a posição
    def as_a(self, position):
        self.person.position = position
        return self

    # Interface fluente para o salário
    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):

    def __init__(self, person) -> None:
        super().__init__(person=person)

    # Interface fluente para o endereço
    def at(self, street_address):
        self.person.street_address = street_address
        return self

    # Interface fluente para o código postal
    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    # Interface fluente para a cidade
    def in_city(self, city):
        self.person.city = city
        return self


# Agora, para usar o conjunto de Builder, fazemos:
pb = PersonBuilder()
person = pb\
    .lives\
        .at("123 London Road")\
        .in_city("London")\
        .with_postcode("SW12BC")\
    .works\
        .at("Fabrikam")\
        .as_a("Engineer")\
        .earning(123000)\
    .build()
print(person)


# Vamos criar uma classe Employee que tem um nome e um endereço, que é
# uma outra classe Address

class Address:
    def __init__(self, street_address, city, suite):
        self.street_address = street_address
        self.city = city
        self.suite = suite

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.suite}"

class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives as {self.address}"

# Ao invés do usuário precisar de fazer as cópias manualmente,
# vamos implementar uma Factory que faça isso.

class EmployeeFactory:
    main_office_employee = Employee("", Address("123 East Dr",
                                                "London",
                                                0))
    aux_office_employee = Employee("", Address("123B East Dr",
                                               "London",
                                               0))

    @staticmethod
    def __new_employee(employee, name, suite):
        pass

    @staticmethod
    def new_main_office_employee(name, suite):
        pass

    @staticmethod
    def new_aux_office_employee(name, suite):
        pass
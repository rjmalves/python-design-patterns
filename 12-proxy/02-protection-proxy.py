
# Supondo que temos uma relação simples entre duas entidade:
# Car e Driver. Inicialmente, a implementação pode ser a
# mais intuitiva:
class Car:
    def __init__(self, driver) -> None:
        self.driver = driver

    def drive(self):
        print(f"Car is being driven by {self.driver.name}")


# Porém, se desejarmos implementar uma verificação de idade
# para não permitir que um Car execute drive(), então podemos
# criar uma Proxy, que engloba um Car e é vista da mesma maneira
# do ponto de vista do usuário.
class CarProxy:
    def __init__(self, driver) -> None:
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print("Driver too young")


class Driver:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

# Uma Protection Proxy está relacionada com controle de acesso.
# Se engloba o objeto original, expondo alguns métodos que tenham
# restrições no seu uso.

if __name__ == "__main__":
    driver = Driver("John", 20)
    car = Car(driver)
    car.drive()

    driver = Driver("John", 15)
    car = CarProxy(driver)
    car.drive()

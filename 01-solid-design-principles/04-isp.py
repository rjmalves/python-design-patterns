# ISP - Interface Segregation Principle

# Vamos demonstrar outro princípio da orientação a objetos
# através de um exemplo.

# Suponha que desejamos criar uma classe base para representar
# de maneira genérica um conjunto de objetos que tem algumas
# características em comum entre si.


class Machine:

    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


# Esta classe representa bem, por exemplo, uma impressora
# multifuncional.


class MultiFunctionPrinter(Machine):

    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


# Mas se desejamos representar, por exemplo, uma impressora
# antiga, teremos um problema:


class MultiFunctionPrinter(Machine):

    # O método "print" faz sentido, porque até mesmo
    # impressoras antigas imprimem.
    def print(self, document):
        pass

    # Agora, impressoras antigas não fazem "fax". O que devemos colocar
    # na implementação do método? Devemos lançar uma exceção? Se fizermos
    # isso o programa será interrompido...
    def fax(self, document):
        pass

    # O mesmo valo para "scan". Também podemos retornar uma mensagem
    # dizendo que não está implementado, mas aí todos que usam a função
    # "scan" de alguma Machine precisam verificar as mensagens de retorno,
    # o que cria alguns compromissos inadequados... o ideal era que não
    # tivesse esse método
    def scan(self, document):
        pass


# Daí compreendemos o sentido do princípio ISP. Toda interface deve ser
# granular, para conseguir representar os tipos de entidades no grau que
# podemos vir a precisar na nossa modelagem. O ideal é que hajam três
# interfaces:

from abc import abstractmethod

class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Fax:
    @abstractmethod
    def fax(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


# Daí podemos instanciar adequadamente os nossos objetos, que só atendem
# as interfaces que precisam atender:


def MyPrinter(Printer):

    def print(self, document):
        print(document)


def Photocopier(Printer, Scanner):

    def print(self, document):
        pass

    def scan(self, document):
        pass


# Também podemos criar interfaces mais complexas para não precisar
# fazer heranças múltiplas o tempo inteiro

def MultiFunctionDevice(Printer, Scanner):

    def print(self, document):
        pass

    def scan(self, document):
        pass


# Assim podemos criar os objetos mais complexos mais facilmente

class MultiFunctionMachine(MultiFunctionDevice):

    def __init__(self, printer, scanner) -> None:
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)

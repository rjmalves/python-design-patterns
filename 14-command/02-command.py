
# Iremos ilustrar uma implementação de Command
# com um problema clássico de conta bancária.

from abc import ABC
from enum import Enum

# A classe básica BankAccount pode parecer suficiente
# para resolver o problema desejado
class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0) -> None:
        self.balance = 0

    # As ações com BankAccount retornam o sucesso ou não
    def deposit(self, amount):
        self.balance += amount
        print(f"Depositing ${amount}")
        return True

    def withdraw(self, amount):
        if self.balance - amount > BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrawing ${amount}")
            return True
        return False

    def __str__(self):
        return f"Balance = {self.balance}"


# Todavia, se quisermos implementar um registro das operações feitas
# ou até mesmo possibilitar desfazer uma operação, precisamos de
# implementar o conceito de operação como uma entidade.

# Para isso, listamos as possíveis operações
class Action(Enum):
    DEPOSIT = 0
    WITHDRAW = 1


# Definimos também um comando genérico
class Command(ABC):

    # A função invoke é reponsável por executar o comando em questão
    def invoke(self):
        pass

    # A função undo é responsável por desfazer o comando, se executado
    def undo(self):
        pass


class BankAccountCommand(Command):
    def __init__(self, account, action, amount) -> None:
        self.account = account
        self.action = action
        self.amount = amount
        self.success = None

    def invoke(self):
        if self.action == Action.DEPOSIT:
            self.success = self.account.deposit(self.amount)
        elif self.action == Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        # O sucesso ou não das ações é usado para saber se elas
        # devem ser desfeitas ou não
        if not self.success:
            return
        if self.action == Action.DEPOSIT:
            self.success = self.account.withdraw(self.amount)
        elif self.action == Action.WITHDRAW:
            self.success = self.account.deposit(self.amount)


if __name__ == "__main__":
    ba = BankAccount()
    cmd = BankAccountCommand(ba, Action.DEPOSIT, 100)
    cmd.invoke()
    print(f"After $100 deposit: {ba}")

    cmd.undo()
    print(f"After $100 deposit undo: {ba}")
    cmd2 = BankAccountCommand(ba, Action.WITHDRAW, 1000)
    cmd2.undo()
    print(f"After $1000 withdraw undo: {ba}")

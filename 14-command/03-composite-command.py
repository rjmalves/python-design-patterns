

from abc import ABC
from enum import Enum


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0) -> None:
        self.balance = balance

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


class Action(Enum):
    DEPOSIT = 0
    WITHDRAW = 1


# Para representar um Command que, na verdade, é uma composição de outros
# Command, precisamos ajustar a definição da classe base, adicionando
# um atributo para sucesso.
class Command(ABC):

    def __init__(self) -> None:
        self.success = None

    def invoke(self):
        pass

    def undo(self):
        pass


class BankAccountCommand(Command):
    def __init__(self, account, action, amount) -> None:
        super().__init__()
        self.account = account
        self.action = action
        self.amount = amount

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


# Agora definimos um comando composto, mas que não irá funcionar
# bem como desejado.
class CompositeBankAccountCommand(Command, list):
    def __init__(self, items=[]) -> None:
        super().__init__()
        for i in items:
            self.append(i)

    def invoke(self):
        for x in self:
            x.invoke()

    def undo(self):
        for x in reversed(self):
            x.undo()


# Definimos um comando composto que funciona como esperado
class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_acct, to_acct, amount) -> None:
        super().__init__([
            BankAccountCommand(from_acct,
                               Action.WITHDRAW,
                               amount),
            BankAccountCommand(to_acct,
                               Action.DEPOSIT,
                               amount),
        ])

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False
        # O invoke guarda o sucesso de todas as operações
        self.success = ok


if __name__ == "__main__":
    ba1 = BankAccount(100)
    ba2 = BankAccount()

    amount = 1000
    cmd = CompositeBankAccountCommand([
        BankAccountCommand(ba1, Action.WITHDRAW, amount),
        BankAccountCommand(ba2, Action.DEPOSIT, amount)
    ])
    cmd.invoke()
    print(f"ba1: {ba1}, ba2: {ba2}")
    cmd.undo()
    print(f"ba1: {ba1}, ba2: {ba2}")

    print("-------")

    amount = 100
    transfer = MoneyTransferCommand(ba1, ba2, amount)
    transfer.invoke()
    print(f"ba1: {ba1}, ba2: {ba2}")
    transfer.undo()
    print(f"ba1: {ba1}, ba2: {ba2}")
    print(transfer.success)

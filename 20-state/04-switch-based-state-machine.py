from enum import Enum, auto

# Podemos fazer a mesma lógica, porém
# com o uso de condicionais

# Neste caso, iremos fazer uma fechadura de cofre,
# que é baseada em uma senha de 4 dígitos

class State(Enum):
    LOCKED = auto()
    FAILED = auto()
    UNLOCKED = auto()


if __name__ == "__main__":
    print("Please type the digits of the password")
    code = "1234"
    state = State.LOCKED
    entry = ""
    while True:
        if state == State.LOCKED:
            # Trata o caso em que o cofre ainda está
            # fechado
            entry += input(entry)
            if entry == code:
                state = State.UNLOCKED
            if not code.startswith(entry):
                state = State.FAILED
        if state == State.FAILED:
            print("\nFAILED")
            entry = ""
            state = State.LOCKED
        if state == State.UNLOCKED:
            print("\nUNLOCKED")
            break

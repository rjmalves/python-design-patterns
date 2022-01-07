from abc import ABC


# Para ilustrar, vamos implementar um interruptor
# de luz, que pode estar ligado ou desligado

# A implementação pode parecer muito complicada para algo tão
# simples, mas iremos entender por que.

class Switch:
    # O switch é uma classe de apenas um atributo: o estado.
    def __init__(self) -> None:
        self.state = OffState()

    # Quando modificamos o estado, não o fazemos diretamente.
    # Acessamos o estado e forçamos uma transição.
    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


# Iremos implementar também classes para representar
# os estados em que o interruptor pode estar.


class State(ABC):
    def on(self, switch):
        print("Light is already on")

    def off(self, switch):
        print("Light is already off")


class OnState(State):
    def __init__(self) -> None:
        print("Light turned on")

    def off(self, switch):
        print("Turning light off...")
        switch.state = OffState()


class OffState(State):
    def __init__(self) -> None:
        print("Light turned off")

    def on(self, switch):
        print("Turning light on...")
        switch.state = OnState()


# A implementação tem alguns problemas.
# Para este caso, talvez não fosse necessário tornar cada estado
# uma classe. Poderiam simplesmente ser um Enum.
# Ainda, o próprio estado ser responsável pela transição
# do estado da classe principal é uma ideia interessante, porém
# não muito intuitiva.

if __name__ == "__main__":
    sw = Switch()

    sw.on()

    sw.off()

    sw.off()

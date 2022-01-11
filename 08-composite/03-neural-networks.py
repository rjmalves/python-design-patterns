from abc import ABC
from collections.abc import Iterable


# Podemos definir uma classe base para conter os
# métodos comuns
class Collectable(Iterable, ABC):
    def connect_to(self, other):
        if self == other:
            return

        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Collectable):
    def __init__(self, name) -> None:
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self):
        return (f"{self.name}, " +
                f"{len(self.inputs)} inputs,"
                f"{len(self.outputs)} outputs")

    # Habilitamos Neuron como iterável ao definir esse método.
    # Assim ele pode ser tratado como uma lista de 1 elemento
    # de maneira transparente.
    def __iter__(self):
        yield self


class NeuronLayer(list, Collectable):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        for x in range(0, count):
            self.append(Neuron(f"{name}-{x}"))

    def __str__(self):
        return f"{self.name} with {len(self)} neurons"


if __name__ == "__main__":
    neuron1 = Neuron("n1")
    neuron2 = Neuron("n2")
    layer1 = NeuronLayer("L1", 3)
    layer2 = NeuronLayer("L2", 4)

    neuron1.connect_to(neuron2)
    neuron1.connect_to(layer1)
    layer1.connect_to(neuron2)
    layer2.connect_to(layer2)

    print(neuron1)
    print(neuron2)
    print(layer1)
    print(layer2)

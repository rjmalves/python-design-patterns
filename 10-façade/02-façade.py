# Vamos ilustrar o uso de uma Façade para simplificar
# a API do desenvolvedor final, escondendo algumas
# complexidades do meio.

# Supondo que temos um buffer bidimensional que é capaz
# de armazenar alguns caracteres.

class Buffer:
    def __init__(self, width=30, height=20) -> None:
        self.width = width
        self.height = height
        self.buffer = [" "] * (width * height)

    # Podemos reimplementar esse magic method que facilita
    # o uso do buffer para instâncias superiores
    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text


# Definimos uma Viewport, que é um elemento que provê uma
# interface para utilização do Buffer
class Viewport:
    def __init__(self, buffer=Buffer()) -> None:
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[index + self.offset]

    def append(self, text):
        self.buffer.write(text)


# Para o usuário final, talvez a Viewport tenha muitos detalhes
# de implementação. Por isso, vamos definir a classe que provê
# a API externa, que pode ter vários Buffer e várias Viewport
# que compartilhar, ou não, Buffers (mas o usuário não sabe disso)
class Console:
    def __init__(self) -> None:
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    # Podemos ter APIs de alto nível, como escrever no Console,
    # que é traduzido em adicionar ao Viewport, que escreve no Buffer
    def write(self, text):
        self.current_viewport.buffer.write(text)

    # Podemos ter APIs de baixo nível específicas para algumas tarefas
    # do usuário do Console
    def get_char_at(self, index):
        self.current_viewport.get_char_at(index)


if __name__ == "__main__":
    # O usuário usa apenas a classe Console
    c = Console()
    # Que pode expor uma API de alto nível
    # (o usuário, ao escrever, nem faz ideia que existem os buffers..)
    c.write("hello")
    # Ou pode expor uma API de baixo nível
    ch = c.get_char_at(0)

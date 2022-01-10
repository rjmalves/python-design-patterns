# Supondo que temos uma tarefa que fornecerá uma lista como saída,
# mas desejamos escolher em qual formato irá acontecer:
# HTML ou Markdown


from abc import ABC
from enum import Enum, auto

# Define-se uma classe base para as estratégias.
# A estratégia não guarda nada do estado do sistema,
# por isso todos os seus métodos recebem os containeres
# de dados e atuam sobre eles. Estes ficam em outro lugar.
class ListStrategy(ABC):
    def start(self, buffer): pass
    def end(self, buffer): pass
    def add_list_item(self, buffer, item): pass


# Um enum para ter controle das variações que existem
class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


class MarkdownListStrategy(ListStrategy):
    def add_list_item(self, buffer, item):
        buffer.append(f" * {item}\n")


class HtmlListStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append("<ul>\n")

    def end(self, buffer):
        buffer.append("</ul>\n")

    def add_list_item(self, buffer, item):
        buffer.append(f"  <li>{item}</li>\n")


class TextProcessor:
    def __init__(self,
                 list_strategy=HtmlListStrategy()) -> None:
        self.list_strategy = list_strategy
        self.buffer = []

    def append_list(self, items):
        ls = self.list_strategy
        ls.start(self.buffer)
        for item in items:
            ls.add_list_item(self.buffer, item)
        ls.end(self.buffer)

    def set_output_format(self, format):
        if format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return "".join(self.buffer)

if __name__ == "__main__":
    items = ["foo", "bar", "baz"]

    tp = TextProcessor()
    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(items)
    print(tp)

    tp.set_output_format(OutputFormat.HTML)
    tp.clear()
    tp.append_list(items)
    print(tp)

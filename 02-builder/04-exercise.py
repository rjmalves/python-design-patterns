class Code:

    indent_size = 4

    def __init__(self, name) -> None:
        self.name = name
        self.fields = {}

    def __str(self, indent):
        lines = []
        i0 = ' ' * ((indent + 0) * Code.indent_size)
        i1 = ' ' * ((indent + 1) * Code.indent_size)
        i2 = ' ' * ((indent + 2) * Code.indent_size)
        lines.append(f'{i0}class {self.name}:')
        if len(self.fields.keys()) == 0:
            lines.append(f"{i1}pass")
        else:
            lines.append(f'{i1}def __init__(self):')
            for k, v in self.fields.items():
                lines.append(f'{i2}self.{k} = {v}')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

class CodeBuilder:

    def __init__(self, root_name) -> None:
        self.root_name = root_name
        self.code = Code(root_name)

    def add_field(self, name, value):
        self.code.fields[name] = value
        return self

    def __str__(self):
        return str(self.code)


cb = CodeBuilder("Person").add_field("name", '""')\
                          .add_field("age", "0")
print(cb)
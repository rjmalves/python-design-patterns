
# Vamos realizar uma implementação que permita
# utilizar os métodos específicos das classes
# decoradas.

from typing import Any

# Se temos uma classe que decora um arquivo com
# logging, então queremos usá-lo como um arquivo
# normal.
class FileWithLogging:
    def __init__(self, file) -> None:
        self.file = file

    def writelines(self, strings):
        self.file.writelines(strings)
        print(f"wrote {len(strings)} lines")

    # Para tornar o acesso ao arquivo transparente,
    # iremos fazer um overload de alguns magic methods
    def __getattr__(self, item: str) -> Any:
        return getattr(self.__dict__["file"], item)

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "file":
            self.__dict__[key] = value
        else:
            setattr(self.__dict__["file"], key, value)

    def __delattr__(self, item: str) -> None:
        delattr(self.__dict__["file"], item)

    # Neste caso específico, vale a pena também reescrever
    # os métodos de iteração.

    def __iter__(self):
        return self.file.__iter__()

    def __next__(self):
        return self.file.__next__()


if __name__ == "__main__":
    f = FileWithLogging(open("hello.log", "w"))
    f.writelines(["hello", "world"])
    # Podemos tratar f como um arquivo, chamando
    # métodos que não implementamos no decorator
    f.write("hey jude")
    f.close()

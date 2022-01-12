
# Supondo que estamos lidando com uma tarefa de carregar
# dados de imagens e exibi-los na tela.
# Na implementação inicial, o Bitmap carrega os dados
# na inicialização.
class Bitmap:
    def __init__(self, filename) -> None:
        self.filename = filename
        print(f"Loading image from {self.filename}")

    def draw(self):
        print(f"Drawing image {self.filename}")

# Podemos fazer uma implementação diferente, chamada "Lazy".
# Esta variação funciona como uma Proxy de economia de dados,
# uma vez que o processo de carregamento pode ser custoso.
# Não queremos ler os dados a menos que realmente precisemos
# exibir na tela.
class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()

# A função genérica para desenhar
def draw_image(image):
    print("About to draw image")
    image.draw()
    print("Finished drawing image")


# Ao usar o Bitmap e o LazyBitmap, temos uma diferença na
# ordem em que as tarefas são executadas.
if __name__ == "__main__":
    bmp = Bitmap("facepalm.jpg")
    draw_image(bmp)
    print("--")
    bmp2 = LazyBitmap("facepalm2.jpg")
    draw_image(bmp2)

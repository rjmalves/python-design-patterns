class Game(list):
    def __call__(self, *args, **kwds):
        return len(self)


class Rat:
    def __init__(self, game):
        self.game = game
        self.game.append(self)
        self._attack = 1

    @property
    def attack(self):
        return self.game()

    def __enter__(self):
        pass

    def __exit__(self, type, value, tb):
        self.game.remove(self)


game = Game()
rat = Rat(game)
rat1 = Rat(game)
rat2 = Rat(game)
rat3 = Rat(game)
rat4 = Rat(game)
with Rat(game) as rat5:
    print(rat.attack)

print(rat1.attack)
print(rat2.attack)
print(rat3.attack)
print(rat4.attack)

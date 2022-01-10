# Supondo que desejamos implementar um
# sistema para gerenciar partidas de jogos.

from abc import ABC


class Game(ABC):
    def __init__(self, number_of_players) -> None:
        self.number_of_players = number_of_players
        self.current_player = 0

    # O template method utiliza vários métodos que
    # não são definidos na classe base "Game"
    def run(self):
        self.start()
        while not self.have_winner:
            self.take_turn()
        print(f"Player {self.winning_player} wins!")

    def start(self): pass

    @property
    def have_winner(self): pass

    def take_turn(self): pass

    @property
    def winning_player(self): pass


# A classe Chess, sendo uma implementação concreta, tem
# que implementar todos os métodos chamados no template
# method.
class Chess(Game):
    def __init__(self) -> None:
        super().__init__(2)
        self.max_turns = 10
        self.turn = 1

    def start(self):
        print(f"Starting a game of chess with " +
              f"{self.number_of_players} players.")

    @property
    def have_winner(self):
        return self.turn == self.max_turns

    def take_turn(self):
        print(f"Turn {self.turn} taken by player " +
              f"{self.current_player}")
        self.turn += 1
        self.current_player = 1 - self.current_player

    @property
    def winning_player(self):
        return self.current_player


if __name__ == "__main__":
    chess = Chess()
    chess.run()

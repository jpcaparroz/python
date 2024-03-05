from .player import Player
from .round import Round

class Match(Round):
    
    def __init__(self, player1:Player, player2:Player, round:int) -> None:
        self.player1 = player1
        self.player2 = player2
        self.round = round
        
    def __str__(self) -> str:
        return f'Player 1: {self.player1.name} | Player 2: {self.player2.name}'
    
    def play(self) -> list:
        matches = []

        for _ in range(self.round):
            self.player1.random_move()
            self.player2.random_move()
            matches.append(self.game())
            
        return matches
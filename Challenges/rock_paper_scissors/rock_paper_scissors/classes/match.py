from .player import Player
from .round import Round

class Match(Round):
    
    player1: Player
    player2: Player
    round: int
    
    def __init__(self, player1:Player, player2:Player, round:int) -> None:
        self.player1 = player1
        self.player2 = player2
        self.round = round
        
    def __str__(self) -> str:
        return f'Player 1: {self.player1.name} | Player 2: {self.player2.name}'
    
    def play(self) -> list:
        matches = []
        
        round = Round(self.player1, self.player2)

        for _ in range(self.round):
            matches.append(round.automatic_game())
            
        return matches
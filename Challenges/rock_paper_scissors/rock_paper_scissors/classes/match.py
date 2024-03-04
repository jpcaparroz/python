from . import Player

class Match:
    
    def __init__(self, p1:Player, p2:Player) -> None:
        self.p1 = p1
        self.p2 = p2
        
    def __str__(self) -> str:
        return f'Player 1: {self.p1.name} | Player 2: {self.p2.name}'
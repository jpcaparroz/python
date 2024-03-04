from .player import Player
from .moveset import Moveset

class Round:
    
    def __init__(self, player1:Player, player2:Player) -> None:
        self.player1 = player1
        self.player2 = player2
    
    def rule(self, move1:Moveset, move2:Moveset) -> int:
        
        result = 0

        if move1 == move2:
            pass
        
        if move1 == 'S' and move2 == 'P':
            result = 1
        
        if move1 == 'P' and move2 == 'S':
            result = 2
        
        if move1 == 'R' and move2 == 'S':
            result = 1
        
        if move1 == 'S' and move2 == 'R':
            result = 2
        
        if move1 == 'P' and move2 == 'R':
            result = 1
        
        if move1 == 'R' and move2 == 'P':
            result = 2
            
        return result
    
    def game(self) -> int:
        
        return self.rule(self.player1.move, self.player2.move)

from .moveset import Moveset
class Player:
    
    move: Moveset

    def __init__(self, name:str) -> None:
        self.name = name
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    def random_move(self) -> None:
        self.move = Moveset.random_move()
        
    def move(self, move:Moveset) -> None:
        self.move = move
    
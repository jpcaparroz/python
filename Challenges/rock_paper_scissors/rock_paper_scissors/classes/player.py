from .moveset import Moveset
class Player(Moveset):
    
    def __init__(self, name:str, move:str = None) -> None:
        self.name = name
        self.move = self.movement(move) if move else self.random_move()
        
    def __str__(self) -> str:
        return f'Name: {self.name} | Move: {self.move}'

    
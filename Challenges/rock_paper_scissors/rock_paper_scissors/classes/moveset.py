import random

VALID_MOVES = ['R', 'P', 'S']

class Moveset:
    
    def __init__(self, move:str) -> None:
        
        if move.capitalize() not in VALID_MOVES:
            raise ValueError(f'This move ({move}) are not valid. Try one of these: {VALID_MOVES}')
        
        self.move = move
    
    def random_move() -> str:
        return random.choice(VALID_MOVES)
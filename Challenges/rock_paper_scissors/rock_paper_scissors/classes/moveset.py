import random

VALID_MOVES = ['R', 'P', 'S']

class Moveset:

    def movement(self, move:str) -> None:
        if move.capitalize() not in VALID_MOVES:
            raise ValueError(f'Move ({move}) are not valid. Try one of these: {VALID_MOVES}')
        
        return move
            
    def random_move(self) -> None:
        return random.choice(VALID_MOVES)
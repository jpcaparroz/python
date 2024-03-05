
class Round:
    
    result: int

    def rule(self) -> None:
        result = 0

        if self.player1.move == self.player2.move:
            pass

        elif (self.player1.move, self.player2.move) in [('S', 'P'), ('R', 'S'), ('P', 'R')]:
            result = 1
            
        else:
            result = 2
            
        self.result = result


    def winner(self) -> str:
        match self.result:
            case 0:
                return 'DRAW'
            
            case 1:
                return self.player1.name
            
            case 2:
                return self.player2.name


    def game(self) -> int:
        self.rule()
        return self.winner()


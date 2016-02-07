class Board:
    def __init__(self):
        self.boardState = [" " for x in range(0,9)]
        self.won = " "
    def displayBoard(self):
        for x in range(0,3):
            print " " + self.boardState[3*x] + " | " + self.boardState[3*x + 1] + " | " + self.boardState[3*x + 2]
            if x != 2:
                print "-----------"
                
    def placePiece(self, player, place):
        if ord(self.boardState[place]) == 32:
            self.boardState[place] = player
            self.isWon(player)
            return True
        return False

    def isWon(self,player):
        for place in range(0,3):
            if self.boardState[place] == self.boardState[place + 3] == self.boardState[place + 6] != " ":          #####down
                self.won = player
                return
            if self.boardState[3*place] == self.boardState[3*place + 1] == self.boardState[3*place + 2] != " ":        ##### across
                self.won = player
                return
        if self.boardState[0] == self.boardState[4] == self.boardState[8] != " " or self.boardState[2] == self.boardState[4] == self.boardState[6] != " ":        ##### diagonals
            self.won = player
            return
        filled = 0
        while filled < 9 and ord(self.boardState[filled]) != 32:
            filled +=1
        if filled == 9:
            self.won = "tie!"
            return
        self.won = " "
            
class Player:
    def __init__(self, player):
        self.player = player
        
    def placePiece(self, board, place):
        hoppened = board.placePiece(self.player, place)
        if hoppened:
            return True
        else:
            return False
        

        

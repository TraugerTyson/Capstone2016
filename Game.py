import Tic_Tac_Toe
import NET
import copy

def start():
    board = Tic_Tac_Toe.Board()
    board.displayBoard()
    ex = Tic_Tac_Toe.Player("x")
    oh = Tic_Tac_Toe.Player("o")
    turn = 0
    piece = 0
    
    while ord(board.won[0]) == 32:
        if turn%2 == 0:
            piece = raw_input("Please place your piece! (0-8)\n")
            piece = ord(piece) - 48
            if not ex.placePiece(board, piece):
                print "This place has been taken! Please do again!"
                turn -=1
        else:
            piece = NET.getBest().getAnswer(board.boardState)
            if not oh.placePiece(board, piece):
                print "This place has been taken! Please do again!"
                turn -=1
        board.displayBoard()
        turn += 1
    print board.won + " has won!"
start()

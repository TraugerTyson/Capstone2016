import Tic_Tac_Toe
import NET
import copy
import random
import Create_Net
import math

def PlayWithHuman():
    """This function allows a human player to play
    against a neural network"""
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
            piece = Create_Net.getBest().getAnswer(board.boardState)
            if not oh.placePiece(board, piece):
                print "This place has been taken! Please do again!"
                turn -=1
        board.displayBoard()
        turn += 1
    print board.won + " has won!"
    return board.won

def playWithRandom(net):
    """This function pits a neural network (a parameter)
    against a random guesser and returns the winner"""
    board = Tic_Tac_Toe.Board()
    ex = Tic_Tac_Toe.Player("x")
    oh = Tic_Tac_Toe.Player("o")
    turn = 0
    piece = 0
    while ord(board.won[0]) == 32:
        if turn%2 == 0:
            piece = -1
            while (board.boardState[piece]== "x" and board.boardState[piece] == "o") or piece ==-1:
                piece = int(random.random()*9)
            ex.placePiece(board,piece)
        else:
            piece = net.getAnswer(board.boardState)
            if not oh.placePiece(board, piece):
                print "This place has been taken! Please do again!"
                turn -=1
        turn += 1
    #print board.won + " has won!"
    return board.won

def run(times, howMany, gamesPer):
    """This plays a neural network against a random guesser 'gamesPer' amount of times,
    with 'howMany' repetition per trial. There are 'times' trials."""
    total = 0
    wins = []
    variences = []
    averages = []
    for x in range(0,times):
        net = Create_Net.start(100,100)
        total = 0
        varience = 0
        average = 0
        wins = []
        for x in range(0,howMany):
            win = 0
            for counter in range(0,gamesPer):
                outcome = playWithRandom(net)
                if outcome == "o" or outcome == "tie!":
                    win+=1
            wins.append(win)
            total +=win
        average = float(total)/float(howMany)
        varience = 0
        for x in wins:
            varience+=(x-average)**2
        varience = varience/99
        std_dev = math.sqrt(varience)
        print "Average: ",average
        print "Variance: ",varience
        print "Standard Deviation: ", std_dev
        averages.append(average)
        variences.append(varience)
        
run(1,10,10)    ### This line starts everything; it is the line that runs the program
    

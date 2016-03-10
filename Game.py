import Tic_Tac_Toe
import NET
import copy
import random
import Create_Net
import math
import numpy as np
import pickle
def importNet(size):
    fileWeights = open("bestw","r")
    fileBiases = open("bestb","r")
    net = NET.Network(size)
    w = pickle.load(fileWeights)
    b = pickle.load(fileBiases)
    net.biases = b
    net.weights = w
    fileWeights.close()
    fileBiases.close()
    return net
    
def playWithHuman(net):
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
            piece = net.getAnswer(board.boardState)
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
            piece = int(random.random()*9)
            if not ex.placePiece(board,piece):
                turn-=1
            
        else:
            piece = net.getAnswer(board.boardState)
            if not oh.placePiece(board, piece):
                print "This place has been taken! Please do again!"
                turn -=1
        turn += 1
    #print board.won + " has won!"
    return board.won
def playAgainstOther(testNet, goodNet):
    """This function pits a neural network (a parameter)
    against another neural network (2nd parameter) to teach it better"""
    board = Tic_Tac_Toe.Board()
    ex = Tic_Tac_Toe.Player("x")
    oh = Tic_Tac_Toe.Player("o")
    turn = 0
    piece = 0
    while ord(board.won[0]) == 32:
        if turn%2 == 0:
            piece = goodNet.getAnswer(board.boardState)
            if not oh.placePiece(board, piece):
                print "This place has been taken! Please do again!"
                turn -=1
            
        else:
            piece = testNet.getAnswer(board.boardState)
            if not oh.placePiece(board, piece):
                print "This place has been taken! Please do again!"
                turn -=1
        turn += 1
    #print board.won + " has won!"
    return board.won
def run(times, howMany, gamesPer, net, testNet = False, goodNet = 0, xoro = 0, printout = False):
    """This plays a neural network against a random guesser 'gamesPer' amount of times,
    with 'howMany' repetition per trial. There are 'times' trials."""
    total = 0
    wins = []
    variences = []
    averages = []
    ties = []
    for x in range(0,times):
        varience = 0
        average = 0
        wins = []
        ties = []
        total_wins = 0
        total_ties = 0
        for x in range(0,howMany):
            win = 0
            tie = 0
            if testNet:
                for counter in range(0,gamesPer):
                    outcome = playWithOther(net,goodNet)
                if outcome == xoro:
                    win+=1
                elif outcome == "tie!":
                    tie+=1
            else:
                for counter in range(0,gamesPer):
                    outcome = playWithRandom(net)
                    if outcome == "o":
                        win+=1
                    elif outcome == "tie!":
                        tie+=1
            wins.append(win)
            ties.append(tie)
        total_wins = sum(wins)
        total_ties = sum(ties)
        average = (float(total_wins)/float(howMany),float(total_ties)/float(howMany))
        varience = 0
        for x in wins:
            varience+=(x-average[0])**2
        varience = varience/99
        std_dev = math.sqrt(varience)
        if printout:
            print "Average: ",average
            print "Variance: ",varience
            print "Standard Deviation: ", std_dev
        averages.append(average)
        variences.append(varience)
        return averages
        
#run(1,10,10,True)    ### This line starts everything; it is the line that runs the program


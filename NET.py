import numpy as np
import matplotlib.pyplot as plt
import random
import Game
class Network:
    def __init__(self,size):
        """Constructor for the neural network"""
        self.layers = len(size)
        self.size = size
        self.weights = [np.random.randn(y,x) for x,y in zip(size[:-1], size[1:])]   #instead of having each neuron created itself, I 'combine' them so that each layer is an array of weights and biases
        self.biases = [np.random.randn(y,1) for y in size[1:]]                      


    def feedforward(self, a):
        """Returns the output neurons values in an array"""
        for x in range(0,self.layers-1):
            a = sigmoid(np.dot(self.weights[x],a)+np.hstack(self.biases[x]))
        return a
    
    def evaluate(self, trials, games, xoro, testNet = False, goodNet = 0):
        """Tests the network and returns the results"""
        if testNet:         ###If there is another network to test with
            answers = Game.run(1,trials, games, self, xoro, True, goodNet)
        else:               ###If running against a random guesser
            answers = Game.run(1,trials,games,self, xoro)
        return answers
    
    def getAnswer(self, boardState):
        """Returns the place the network will place their piece in Tic-Tac-Toe"""
        boardState = convert(boardState)
        answer = self.feedforward(boardState)
        pick = np.argmax(answer)
        while boardState[pick]!=0:      ###If there is already a piece there, pick another
            np.put(answer,pick,-1)          ###replace maximum with a -1 (so it is no longer maximum) 
            pick = np.argmax(answer)
        return pick


def sigmoid(z):
    """The value a neuron outputs given an input"""
    return 1/(1+ np.exp(-z))

def convert(array):
    """Converts a Tic-Tac-Toe board into an integer array that the network can use"""
    new = []
    for x in array:
        if x == 'o':
            new.append(100)
        elif x == 'x':
            new.append(10)
        elif x == ' ':
            new.append(0)
        else:
            new.append(x)
    npnew = np.array(new)
    return npnew


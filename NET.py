import numpy as np
import matplotlib.pyplot as plt
import random
import Game
class Network:
    def __init__(self,size):
        """Constructor for creating a neural network"""
        self.layers = len(size)
        self.size = size
        self.weights = [np.random.randn(y,x) for x,y in zip(size[:-1], size[1:])]   #instead of having each neuron created itself, I 'combine' them so that each layer is an array of weights and biases
        self.biases = [np.random.randn(y,1) for y in size[1:]]                      


    def feedforward(self, a):
        """Returns the output neurons values in an array"""
        for x in range(0,self.layers-1):
            a = sigmoid(np.dot(self.weights[x],a)+np.hstack(self.biases[x]))
        return a
    
    def evaluate(self, test_data, answers1):
        """Tests the network and returns the results"""
        #answers = [self.feedforward(x) for x in test_data]      ###Array of the output neurons' values
        #maximums = [np.argmax(x) for x in answers]              ###Gets the highest activated neuron's index, which is the network's guess
        #cost = costs(answers1,maximums)                         
        #return sum(int(x == y) for (x, y) in zip(maximums,answers1)), cost
        answers = Game.run(1,100,50,self)
        return answers
    
    def getAnswer(self, boardState):
        """Returns the place the network will place their piece in Tic-Tac-Toe"""
        boardState = convert(boardState)
        answer = self.feedforward(boardState)
        pick = np.argmax(answer)
        while boardState[pick]!=0:      ###If there is already a piece there, pick another
            np.put(answer,pick,-1)
            pick = np.argmax(answer)
        return pick


def newCosts(answers, results):
    actLevel = 0.0
    for x in range(0,len(answers)):
        actLevel+=answers[x][results[x]-1]
    return actLevel

def costs(answers, results):
    """Creates the network's cost. Cost is defined as a difference of squares."""
    cost = 0.0
    for x in xrange(0,len(answers)):
            cost += float((float(answers[x]) - float(results[x]))**2) ### Sum of ((networks guess minus the actual answer)^2)
    return cost
    
def sigmoid(z):
    """The value a neuron outputs given an input"""
    return 1/(1+ np.exp(-z))

def pickbest(net, against):
    minimum_cost = 10000
    amount_right = 0
    best = 0
    for x in net:
        test, cost = x.evaluate(against)


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

def convertAll(array):
    """Converts all the testing data into readable arrays for the network"""
    new = []
    for x in array:
        new.append(convert(x))
    return new



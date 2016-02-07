import numpy as np
import matplotlib.pyplot as plt
import random
import copy
import time
class Network:
    def __init__(self,size):
        self.layers = len(size)
        self.size = size
        self.weights = [np.random.randn(y,x) for x,y in zip(size[:-1], size[1:])]
        self.biases = [np.random.randn(y,1) for y in size[1:]]
       # print self.weights[1]
      #  print self.biases
      #  print"\n\n\n"
    def feedforward(self, a):
        counter = 0
        for x in range(0,self.layers-1):
         #   print a,"\n\n"
            a = sigmoid(np.dot(self.weights[x],a)+np.hstack(self.biases[x]))
        """Return the output of the network if ``a`` is input."""
     #   print a
        return a
    def evaluate(self, test_data, answers1):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""
        answers = [self.feedforward(x) for x in test_data]
        maximums = [np.argmax(x) for x in answers]
      #  print "start"
       # print answers[-1]
       # print 'end'
       # print maximums
        cost = costs(answers1,maximums) 
        return sum(int(x == y) for (x, y) in zip(maximums,answers1)), cost
    def getAnswer(self, boardState):
        boardState = convert(boardState)
        answer = self.feedforward(boardState)
        pick = np.argmax(answer)
        while boardState[pick]!=0:
            np.put(answer,pick,-1)
            pick = np.argmax(answer)
        return pick


def newCosts(answers, results):
    actLevel = 0.0
    for x in range(0,len(answers)):
        actLevel+=answers[x][results[x]-1]
    return actLevel
def costs(answers, results):
    cost = 0.0
    for x in xrange(0,len(answers)):
            cost += float((float(answers[x]) - float(results[x]))**2)
    return cost
    
def sigmoid(z):
    return 1/(1+ np.exp(-z))
def pickbest(net, against):
    minimum_cost = 10000
    amount_right = 0
    best = 0
    for x in net:
        test, cost = x.evaluate(against)


def convert(array):
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
    new = []
    for x in array:
        new.append(convert(x))
    return new

def procreate(dup):
    bbest = copy.deepcopy(dup)
    for b in range(0,len(bbest.weights)):
        for c in range(0,len(bbest.weights[b])):
            for a in range(0,len(bbest.weights[b][c])):  
                if random.random() > PERCENTAGE:
                    bbest.weights[b][c][a] = random.random()#a + random.gauss(MEAN,SIGMA)
    for b in range(0,len(bbest.biases)):
        for c in range(0,len(bbest.biases[b])):
            for a in range(0,len(bbest.biases[b][c])):  
                if random.random() > PERCENTAGE:
                    bbest.biases[b][c][a] = random.random()#random.gauss(MEAN,SIGMA)#a + random.gauss(MEAN,SIGMA)
    return bbest







lists =[
    ['o','x','o','o','x','x',' ',' ','x'],  ['x','o','o','o','x','x','x',' ',' '],  ['o','x','o',' ',' ','x','x','x','o'],  ['x','x',' ','o',' ','x','o','x','o'],
    ['o',' ','o','x','x',' ','x','o','x'],  ['x','o','x','o',' ','o','x','x',' '],  ['x',' ',' ','o','o','x','x','o','x'],  ['x',' ','x','x','o','o',' ','x','o'],
    [' ','x','x',' ','o','o','x','x','o'],  [' ','o','x','o','x',' ','x','o','x'],  [' ',' ',' ',' ',' ',' ',' ',' ',' '],  ['o','x',' ',' ','x',' ',' ',' ',' '],
    ['x','x',' ',' ','o',' ',' ',' ',' '],  ['x',' ','o',' ','x','x',' ',' ','o']
    ]
answers = [6,8,4,2,1,4,1,6,3,0,4,7,2,3]
#['o','x','','','x','','','','',7]
#['x','x','','','o','','','','',2]['x','','o','','x','x','','','o',3]['','','','','','','','','',]['','','','','','','','','',]
#['','','','','','','','','',]['','','','','','','','','',]['','','','','','','','','',]['','','','','','','','','',]



PERCENTAGE = .95
nets = [Network([9,30,9]) for x in range(0,10000)]
lists= convertAll(lists)
old_maximum = 0
maximum = 0
maximum_cost = 100000
cost = 0
best = 0
start_time = time.time()


for b in range(0,10000):
    for x in nets:
        y,cost = x.evaluate(lists, answers)
        if cost < maximum_cost:
            maximum_cost = cost
            maximum = y
            best = copy.deepcopy(x)
    if old_maximum != maximum:
        print maximum, float(maximum)/float(len(lists)), maximum_cost, round((time.time() - start_time),5), b
        old_maximum = maximum
    nets = [] 
    for amount in range (0,99):
        nets.append(procreate(best))
    if b%1000==0:
        print maximum, float(maximum)/float(len(lists)), maximum_cost, round((time.time() - start_time),5), b

def getBest():
    return best
targetw = open("bestw.txt",'w')
targetb = open("bestb.txt",'w')
np.save(targetw,best.weights)
np.save(targetb,best.biases)
targetw.close()
targetb.close()

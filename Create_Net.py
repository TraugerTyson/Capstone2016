import NET
import copy
import time
import numpy as np
import random

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
SUBJECTS = 10000
GENERATIONS = 10000
nets = [NET.Network([9,30,9]) for x in range(0,SUBJECTS)]
lists= NET.convertAll(lists)
old_maximum = 0
maximum = 0
maximum_cost = 100000
cost = 0
best = 0
start_time = time.time()


for b in range(0,GENERATIONS):
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

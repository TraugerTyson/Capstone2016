import NET
import copy
import time
import numpy as np
import random
import pickle
def procreate(dup, PERCENTAGE):
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






#['o','x','','','x','','','','',7]
#['x','x','','','o','','','','',2]['x','','o','','x','x','','','o',3]['','','','','','','','','',]['','','','','','','','','',]
#['','','','','','','','','',]['','','','','','','','','',]['','','','','','','','','',]['','','','','','','','','',]
def getBest():
    return best

def start(subjects, generations):
    lists =[
    ['o','x','o','o','x','x',' ',' ','x'],  ['x','o','o','o','x','x','x',' ',' '],  ['o','x','o',' ',' ','x','x','x','o'],  ['x','x',' ','o',' ','x','o','x','o'],
    ['o',' ','o','x','x',' ','x','o','x'],  ['x','o','x','o',' ','o','x','x',' '],  ['x',' ',' ','o','o','x','x','o','x'],  ['x',' ','x','x','o','o',' ','x','o'],
    [' ','x','x',' ','o','o','x','x','o'],  [' ','o','x','o','x',' ','x','o','x'],  [' ',' ',' ',' ',' ',' ',' ',' ',' '],  ['o','x',' ',' ','x',' ',' ',' ',' '],
    ['x','x',' ',' ','o',' ',' ',' ',' '],  ['x',' ','o',' ','x','x',' ',' ','o']
    ]
    answers = [6,8,4,2,1,4,1,6,3,0,4,7,2,3]
    PERCENTAGE = .95
   # SUBJECTS = 1000
   # GENERATIONS = 1000
    nets = [NET.Network([9,30,9]) for x in range(0,subjects)]
    lists= NET.convertAll(lists) 
    old_maximum = -1
    maximum = 0
    maximum_wins = -1
    cost = 0
    best = 0
    start_time = time.time()


    for b in range(0,generations):
        print b
        maximum_wins = -1
        for x in nets:
            wins = x.evaluate(lists, answers)
            if wins[0][0] > maximum_wins:
                maximum_wins = wins[0][0]
                best = copy.deepcopy(x)
        print maximum_wins, float(maximum_wins)/float(50), round((time.time() - start_time),5), b
        nets = [best]
        for amount in range (0,subjects):
            nets.append(procreate(best, PERCENTAGE))



    targetw = open("bestw",'w')
    targetb = open("bestb",'w')
   # np.savetxt(targetw,best.weights)
    pickle.dump(best.biases,targetb)
    pickle.dump(best.weights,targetw)
    targetw.close()
    targetb.close()
    return best

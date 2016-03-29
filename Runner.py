import Game
import NET
import Create_Net
subjects = 100
generations = 25
trialsPer = 1
gamesPerTrial = 100
amount = 50
netsx = []
netso = []
for x in range(amount):
    netsx.append(Create_Net.start(subjects,generations, trialsPer, gamesPerTrial, "x"))
for o in range(amount):
    netso.append(Create_Net.start(subjects,generations, trialsPer, gamesPerTrial, "o"))
for i in range(0,amount):
    print Game.run(1,1,1,netsx[i], "x",True,netso[i])
#while True:
 #   Game.playWithHuman(net,"x")
#Game.playWithHuman(net)
#a = Game.run(1,10,1000,net)
bestx
besto
netsx = []
netso = []
for x in range(0,amount):
    netsx.append(Create_Net.procreate(bestx,.95))
    netso.append(Create_Net.procreate(besto,.95))
xVersusO(netsx,netso)

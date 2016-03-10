import Game

net = Game.importNet([9,30,9])
#Game.playWithHuman(net)
a = Game.run(1,10,1000,net)
print a

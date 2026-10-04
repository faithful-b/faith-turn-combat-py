import random

#this class creates a fighter
class Fighter:
    idNum = 0
    def __init__(self, name = '????', hpMax = 1, hp = 0, mpMax= 0, mp = 0, pp = 0, blk = 75, speed = 1, atk = 1, luck = 100, luckyNum = 60, type1 = "Human", concentration = 5):
        self.idNum += 1
        self.id = "fighter" + str(self.idNum)
        self.name = name
        self.hpMax = hpMax
        self.hp = hp
        self.mpMax = mpMax
        self.mp = mp
        self.type1 = type1
        self.atkMax = atk
        self.speed = speed
        self.luck = luck
        self.blkAmnt = blk
        self.blk = blk/100
        self.recover = hpMax // 4
        self.pp = pp
        

    def randomizeAtk(self):
        atkMax = self.atkMax
        self.atk = random.randint(0, self.atkMax + 1)

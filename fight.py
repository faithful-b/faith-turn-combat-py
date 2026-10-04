from fighter import Fighter
import random


# This starts a fight
class Fight(Fighter):
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def oneTwo(self):
        fighter1 = self.fighter1
        fighter2 = self.fighter2

        randFight1Hp = random.randint(0, fighter1.luck)
        randFight2Blk = random.randint(0, fighter2.luck)

        if randFight1Hp == fighter1.luck // 3:
            fighter1.hp += fighter1.recover
            if fighter1.hp > fighter1.hpMax:
                fighter1.hp = fighter1.hpMax
            print(f"{fighter1.name} recovered {fighter1.recover} hp")

        if randFight2Blk == fighter2.luck // 2:
            fighter2.hp -= fighter1.atkMax * fighter2.blk
            print(
                f"{fighter1.name} attacks {fighter2.name}, "
                f"{fighter2.name} blocks {fighter2.blkAmnt}% of the damage, "
                f"taking only {fighter1.atkMax * fighter2.blk} damage\n"
                f"{fighter2.name}'s hp is down to {fighter2.hp}"
            )
        else:
            fighter2.hp -= fighter1.atkMax
            print(
                f"{fighter1.name} attacks {fighter2.name}, "
                f"dealing {fighter1.atkMax} damage\n"
                f"{fighter2.name}'s hp is down to {fighter2.hp}"
            )

        if fighter2.hp <= 0:
            print(f"Game OVER {fighter1.name} wins")
            return True

        return False

    def twoOne(self):
        fighter1 = self.fighter1
        fighter2 = self.fighter2

        randFight2Hp = random.randint(0, fighter2.luck)
        randFight1Blk = random.randint(0, fighter1.luck)

        if randFight2Hp == fighter2.luck // 3:
            fighter2.hp += fighter2.recover
            if fighter2.hp > fighter2.hpMax:
                fighter2.hp = fighter2.hpMax
            print(f"{fighter2.name} recovered {fighter2.recover} hp")

        if randFight1Blk == fighter1.luck // 2:
            fighter1.hp -= fighter2.atkMax * fighter1.blk
            print(
                f"{fighter2.name} attacks {fighter1.name}, "
                f"{fighter1.name} blocks {fighter1.blkAmnt}% of the damage, "
                f"taking only {fighter2.atkMax * fighter1.blk} damage\n"
                f"{fighter1.name}'s hp is down to {fighter1.hp}"
            )
        else:
            fighter1.hp -= fighter2.atkMax
            print(
                f"{fighter2.name} attacks {fighter1.name}, "
                f"dealing {fighter2.atkMax} damage\n"
                f"{fighter1.name}'s hp is down to {fighter1.hp}"
            )

        if fighter1.hp <= 0:
            print(f"Game OVER {fighter2.name} wins")
            return True

        return False

    def startFight(self):
        fighter1 = self.fighter1
        fighter2 = self.fighter2

        print("The fight BEGINS!!")

        while True:
            randFight1Blk = random.randint(0, fighter1.luck)
            randFight2Blk = random.randint(0, fighter2.luck)
            randFight1Hp = random.randint(0, fighter1.luck)
            randFight2Hp = random.randint(0, fighter2.luck)

            if fighter1.speed >= fighter2.speed:
                if self.oneTwo():
                    break
                if self.twoOne():
                    break
            else:
                if self.twoOne():
                    break
                if self.oneTwo():
                    break

    def specs(self):
        fighter1 = self.fighter1
        fighter2 = self.fighter2
        print(f"{fighter1.name}: HP {fighter1.hp}/{fighter1.hpMax}")
        print(f"{fighter2.name}: HP {fighter2.hp}/{fighter2.hpMax}")

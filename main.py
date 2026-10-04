from fighter import Fighter
from fight import Fight

luke = Fighter(
    name = "Luke",
    hpMax = 100,
    hp = 75,
    atk = 20,
    blk = 75,
    speed = 51,
    luck = 5
)
adam = Fighter(
    name = "Adam",
    hpMax = 100,
    hp = 80,
    atk = 25,
    blk = 80,
    speed = 50,
    luck = 5
)

#fighter1 = Fighter("one")
fighter2 = Fighter("two", speed = 2)

fight = Fight(luke, adam)
#fight2 = Fight(fighter1, fighter2)

fight.startFight()
#fight2.startFight()

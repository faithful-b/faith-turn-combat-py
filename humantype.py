from fighter import Fighter

class Human(Fighter):
    
    def __init__(self, age = "18", weight = 60, height = 40, concentration = 10):
        self.age = age
        self.weight = weight
        self.height = height

    def dodge(self):
        

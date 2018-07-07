class Medic(Character):
    #recuperates 2 hp after attack 20% of the time
    def __init__(self, health, power):
        self.name = 'Medic'
        self.health = health
        self.power = power
    
    def attack(self, hero):
        pass
        
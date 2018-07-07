from characters import Character

class Shadow(Character):
    #Starting health is 1, takes times 10% of the time.
    def __init__(self, health, power):
        self.name = 'Shadow'
        self.health = 1
        self.power = power
        
    def attack(self, hero):
        hero.health -= self.power
        print("The shadow does {} damage to you".format(self.power))
        if(hero.health <= 0):
            print("You are dead")

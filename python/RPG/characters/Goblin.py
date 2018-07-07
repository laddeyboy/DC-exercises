from characters import Character

class Goblin(Character):
    def __init__(self, health, power):
        self.name = 'Goblin'
        self.health = health
        self.power = power
        
    def attack(self, hero):
        hero.health -= self.power
        print("The goblin does {} damage to you".format(self.power))
        if(hero.health <= 0):
            print("You are dead")
from characters import Character

class Zombie(Character):
    #doesn't die even if health below zero
    def __init__(self, health, power):
        self.name = 'Zombie'
        self.health = health
        self.power = power
        
    def attack(self, hero):
        hero.health -= self.power
        print("The zombie does {} damage to you". format(self.power))
        if(hero.health <= 0):
            print("You are dead.")
            
    def alive(self):
        return True
        
    def print_status(self):
        if(self.health < 0):
            print('The zombie is already dead and cannot be killed')
        else:
            super().print_status()
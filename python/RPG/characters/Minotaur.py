from characters import Character
import random

class Minotaur(Character):
    #has a 15 probablity for a charge attach that does 40% damage
    def __init__(self, health, power):
        self.name = 'Minotaur'
        self.health = health
        self.power = power
        
    def attack(self, hero):
        attack_odds = random.randint(1,100)
        if(attack_odds <= 15):
            hero.health -= (self.power * 3)
            print("The minotaur uses his CHARGE ATTACK and does 3 times damage.")
        else:
            hero.health -= self.power
            print("The minotaur does {} damage to you".format(self.power))
        if(hero.health <= 0):
            print("You are dead.")
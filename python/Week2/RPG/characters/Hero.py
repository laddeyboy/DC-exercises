from characters import Character
import random

class Hero(Character): 
    def __init__(self, health, power):
        self.name = 'Hero'
        self.health = health
        self.power = power
        self.gold = 0
        
        
    def _opponent_reaction(self, enemy):
        if(enemy.name == 'Zombie'):
            enemy.health -= self.power
            if(enemy.health > 0):
                print("You do {} damage to the {}.".format(self.power, enemy.name))
            elif(enemy.health <= 0):
                print("\nThe zombie is already dead you cannot kill it!  RUN!!\n")
        elif(enemy.name == 'Shadow'):
            attack_odds = (random.randint(1,100))
            if(attack_odds <= 10):
                enemy.health -= self.power
                print("You do {} damage to the {}.".format(self.power, enemy.name))
            else:
                print("The shadow avoided your attack and takes no damage.")
            if(enemy.health <= 0):
                #defeated the Shadow
                self.gold += 1
                print("You have vanquished the {}".format(enemy.name))
        elif(enemy.name == 'Goblin'):
            enemy.health -= self.power
            print("You do {} damage to the {}.".format(self.power, enemy.name))
            if(enemy.health <= 0):
                #defeated the Goblin
                self.gold += 3
                print("You have vanquished the {}".format(enemy.name))
        elif(enemy.name == "Minotaur"):
            enemy.health -= self.power
            print("You do {} damage to the {}.".format(self.power, enemy.name))
            if(enemy.health <= 0):
                self.gold += 5
                print("You have vanquished the {}".format(enemy.name))
        
    def attack(self, enemy):
        chance = (random.randint(1,100))
        if (chance <= 20):
            enemy.health -= (self.power * 2)
            print("You do {} DAMAGE to the {}.".format((self.power*2), enemy.name))
        else:
            self._opponent_reaction(enemy)
#!/usr/bin/env python
from characters import Hero, Goblin, Zombie, Shadow, Minotaur

import random
# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

def print_title():
    print("**********************************************")
    print('* Welcome to DC-Flex Role Playing Quest 2018 *')
    print("**********************************************")
    print("Let's Play!!\n")

def print_menu(a_monster):
    print("###  What do you want to do?  ###")
    print("1. Fight the {}".format(a_monster.name))
    print("2. Do nothing")
    print("3. Flee in Fear")
    print("> ", end=' ')
    
def game_setup():
    goblin = Goblin(random.randint(1,50), random.randint(1,15))
    shadow = Shadow( 1, random.randint(1,15))
    zombie = Zombie(random.randint(1,25), random.randint(1,15))
    minotaur = Minotaur(random.randint(1,75), random.randint(1,15))
    my_monsters = [goblin, shadow, zombie, minotaur]
    starting_monster = random.randint(0, len(my_monsters)-1)
    fight_list = my_monsters[starting_monster:] + my_monsters[:starting_monster]
    return fight_list
    
def create_hero():
    print('A quest has emerged and a new hero must answer the call.  Who will answer the challenge and will they rise to glory or end in defeat.')
    return Hero(100, 5)
    
def main():
    print_title()
    enemy_monsters = game_setup()
    hero = create_hero()
    
    hero.print_status()
    break_loop = False
    keep_going = True
    
    for monster in enemy_monsters:
        if(keep_going and hero.alive()):
            print("\nYou have entered a new area.....")
            print("Our Hero comes across a {}\n".format(monster.name))
            
            while monster.alive() and hero.alive():
                hero.print_status()
                monster.print_status()
            
                print_menu(monster)
                raw_input = input()
                print('----------------------------')
                if raw_input == "1":
                    # Hero attacks goblin
                    hero.attack(monster)
                elif raw_input == "2":
                    pass
                elif raw_input == "3":
                    if(monster.name == 'Zombie'):
                        print("RUN FOR YOUR LIFE.")
                        break
                    else:
                        print("Goodbye.....coward")
                        keep_going = False
                        break
                else:
                    print("Invalid input {}".format(raw_input))
        
                if monster.alive():
                    # Goblin attacks hero
                    monster.attack(hero)
                print('----------------------------')
    
        #print("YOU HAVE DEFEATED ALL YOUR FOES...GRAND CHAMPION")

main()
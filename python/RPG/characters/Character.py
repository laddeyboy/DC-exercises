
class Character:
    def __init__(self, health, power):
        self.name = None
        self.health = health
        self.power = power
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
            
    def print_status(self):
        if (self.name == 'Hero'):
            print('You have {} health and {} power.'.format(self.health, self.power))
        else:
            print('The {} has {} health and {} power.'.format(self.name, self.health, self.power))
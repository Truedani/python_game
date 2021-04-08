import random

class Character:
   

    def __init__(self, name, hp=100, ability_power=10, dodge=0.15):
        self._name          = name
        self._hp            = hp
        self._ability_power = ability_power
        self._dodge         = dodge
   

    def get_name(self):
        return self._name
   

    def check_life(self):
        print(f'{self._name} is dead!')
    
    
    def heal(self):
        print(f'{self._name} healed')
        

    def attack(self, target):
        print(f'{self._name} attacked with damage!')


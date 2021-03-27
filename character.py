class Character:


    def __init__(self, name, hp=100, ability_power=10, dodge=0.15):
        self._name          = name
        self._hp            = hp
        self._ability_power = ability_power
        self._dodge         = dodge
    

    def check_life(self):
        print(f'{self._name} is alive!')
        return True
    
    
    def heal(self):
        print(f'{self._name} is healing')
        

    def attack(self, target):
        print(f'{self._name} attacked!')

    
    def take_damage(self, damage):
        print(f'{self._name} took damage!')

from character import Character 
import random

def main():
    name = input('Enter your name: ')
    difficulty = input('Enter difficulty (easy/normal/hard)')
    ability_power = 1
    if difficulty is 'easy':
        ability_power = 30
        print('You entered a beginner\'s dungeon!')
    elif difficulty is 'normal':
        ability_power = 20
        print('You dived into an advanced dungeon!')
    elif difficulty is 'hard':
        ability_power = 10
        print('You adventured into an S class dungeon!')
    else:
        print('You entered into an unknown dungeon! Difficulty set to insane!')

    boss = Character(name='Boss', hp=100, ability_power=10, dodge=0.15)
    protagonist = Character(name=name, hp=100, ability_power=ability_power, dodge=0.15)
    print(f'{protagonist.get_name()} entered a dungeon and encounters the first Boss')

    while True:
        action = input('Choose action (attack/heal)')
        if action is 'attack':
            protagonist.attack(boss)
        elif action is 'heal':
            protagonist.heal()
        else:
            print(f'{protagonist.get_name()} didn\'t choose heal or attack, he passes the turn')
        boss.attack(protagonist)
        
        boss_status = boss.check_life()
        protagonist_status = protagonist.check_life()
        if not boss_status:
            print(f'{boss.get_name()} defeated!')
            break
        elif not protagonist_status:
            print(f'{protagonist.get_name()} defeated!')
            break
    print('Game over!')


if __name__ == '__main__':
    main()

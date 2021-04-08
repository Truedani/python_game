from character import Character 
import random

def main():
    name = input('Enter your name: ')
    boss = Character(name='Boss', hp=100, ability_power=10, dodge=0.15)
    protagonist = Character(name=name, hp=100, ability_power=10, dodge=0.15)
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
            print(f'{boss.get_name()} defeated! {
            break
        elif not protagonist_status:
            break
    print('Game over!')


if __name__ == '__main__':
    main()

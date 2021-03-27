from character import Character 
import random

def main():
    name = input("Choose your name: ")
    difficulty = input("Choose difficulty (easy/normal/hard)")
    boss = Character(name='Boss', hp=100, ability_power=10, dodge=0.15)
    protagonist = Character(name='You', hp=100, ability_power=10, dodge=0.15)
    while True:
        ability = random.uniform(0, 1)
        if ability > 0.5:
            protagonist.attack(boss)
        else:
            protagonist.heal()
        boss.attack(protagonist)
        
        boss_status = boss.check_life()
        protagonist_status = protagonist.check_life()
        if not boss_status or not protagonist_status:
            break
    print('Game over!')


if __name__ == '__main__':
    main()

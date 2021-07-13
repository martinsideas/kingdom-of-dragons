# Kingdom of Dragons
import random
import time

#Functions
def showIntro():
    print('\nYou are in a land full of dragons. In front of you,\nthere are two caves. In one of them, the dragon is kind and\nfriendly and will share its treasure with you. The other dragon\nis greedy and hungry, and will devour you immediately.\n')

def chooseCave():
    cave = ''
    
    while cave != '1' and cave != '2':
        cave = input('Which cave do you want to enter? (1 or 2)\n')
    
    return cave

def exploreCave(choosenCave):
    print()
    print('You approach the cave...')
    time.sleep(2)
    print("It's dark and creepy...")
    time.sleep(2)
    print('A large dragon suddenly appears in front of you! It opens its jaws and...')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if choosenCave == str(friendlyCave):
        print('It gives you its treasure!')
    else:
        print('It gobbles you up in one bite!')
    
    print()

#Functions

playAgain = 'y' #yes
while playAgain.lower().startswith('y'):
    
    showIntro()
    
    caveNumber = chooseCave()

    exploreCave(caveNumber)

    playAgain = input("Do you want to play again?\n")
import random
import time

def dice_roll():
    counter=0
    list=[
                                           '''
                                                -----
                                                |   |
                                                | o |    = 1
                                                |   |
                                                -----''',

                                           '''
                                                -----
                                                |o  |
                                                |   |     = 2
                                                |  o|
                                                -----''',

                                           '''
                                                -----
                                                |o  |
                                                | o |     = 3
                                                |  o|
                                                -----''',

                                           '''
                                                -----
                                                |o o|
                                                |   |     = 4
                                                |o o|
                                                -----''',

                                           '''
                                                -----
                                                |o o|
                                                | o |     = 5
                                                |o o|
                                                -----''',

                                           '''
                                                -----
                                                |o o|
                                                |o o|     = 6
                                                |o o|
                                                ----- ''',
                                                 ]
    while  counter !=6:
           counter =counter + 1
           time.sleep(0.49)
           print("\n"*50)
           print(random.choice(list))

dice_roll()

num = 3
print("input  'quit' to stop  ")
print("Press any key to roll the dice ")
while num!='quit':
    num=input(">>> ")
    if num == 'quit':
        break
    else:
        dice_roll()
        print(":)")

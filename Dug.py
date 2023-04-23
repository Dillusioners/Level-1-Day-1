import os # Used to clear screen
import time # use to get pauses
import random # used to generate the random lava spawn
import platform

def starting(clr): # JUST THE UI TO START NICELY
    print(""" | D I G G I N G - S I M U L A T O R ️|""")
    print(""" | - - - - - - -   - - - - - - - - - | \n \n""")
    
    time.sleep(2)
    
    print(
                """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣄⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠿⠟⠛⠻⣿⠆⠀
    ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣆⣀⣀⠀⣿⠂⠀
    ⠀⠀⠀⠀⠀⠀⠀⢸⠻⣿⣿⣿⠅⠛⠋⠈⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠘⢼⣿⣿⣿⣃⠠⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣟⡿⠃⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⣛⣫⡄⠀⢸⣦⣀⠀
    ⠀⠀⠀⢀⣠⣴⣾⡆⠸⣿⣿⣿⡷⠂⠨⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⣤⣾⣿⣿⣿⣿⡇⢀⣿⡿⠋⠁⢀⡶⠪⣉⢸⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢀⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣷⣿⣿⣷⣦⡙⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢹⣿⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡁

    """)

    time.sleep(2)

    print("\n \n Tate:- Hi! Its me and I am stuck in a planet, help me dig down and fall to my planet.")

    time.sleep(2)

    print("\n MONSTER:- I WILL NOT LET YOU GO!")

    time.sleep(2)

    print("\n Tate:- Help me dig!")

    time.sleep(5)

    os.system(clr)


def rules(clr): #RULES TO PLAY THE GAME
    print(""" | RULES |""")
    print(""" | ----- | \n \n""")

    time.sleep(1)

    print("1. There will be 5 blocks and under it 1 will be lava.")
    time.sleep(1)
    print("\n 2. You have to avoid the lava and dig the safe blocks.")
    time.sleep(1)
    print("\n 3. Even if you don't like the game, you have to say its cool.")
    time.sleep(3)
    print("\n \n SO STARTING THE GAME!!")
    time.sleep(3)
    os.system(clr)

def get_user(): # VERIFYING INPUT WITH RECURSION
    user_number = 0
    try: 
        user_number = int(input("\n Enter the block number you want to dig:- "))
        if(user_number <= 5 and user_number >= 0):
            return user_number
        else:
            print("\n Enter a number less than 5 and greater than 0!")
            get_user()
    except:
        print("\n Enter a number!")
        get_user()

def game(clr): # THE MAIN GAME
    print(""" | GAME |""")
    print(""" | ----- | \n \n""")

    lost = False #TO CHECK IF THE PLAYER HAS LOST
    score = -1 # SCORE

    while(not lost): # LOOPING
        score = score + 1
        lava_number = random.randrange(5)
        user = get_user()

        if(lava_number == user):
            print("YOU FELL IN LAVA!!")
            lost = True
            time.sleep(3)
        else:
            print("You Survived and mined the correct block!")

    if(lost):
        os.system(clr)
        print(""" | YOU LOST |""")
        print(""" | --- ---- | \n \n""")

clr = ''
if(platform.system() == 'Windows'): clr = 'cls'
else: clr = 'clear'

starting(clr)
rules(clr)
game(clr)
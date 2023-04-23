import time
import random

#Function to print the story line "slowly"
def slow_print(text, speed=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()

#Getting input from user
def get_input():
    user_number = 0
    #try-except for loggers
    try:
        slow_print("\nEnter the speed of this car you saw.")
        user_number = int(input(">> "))
    except:
        slow_print("\nEnter a number!")
        get_input()
    return user_number

#Giving context to user
def play_game():
    slow_print("Welcome to the Slow Speed Game! \n")
    slow_print("You are standing in front of a fork in the road.")
    slow_print("Watching the cars go at a speed but you see a driver rushing and you remember 'SAFE DRIVE SAVE LIFE BY MAMATA BANERJEE'. So now you try to guess the speed of different cars but if you tell the speed more than the actual speed, you lose. So GET SLOW!!! \n")
#Working out game logic
    lose = False
    score = -1
    while not lose:
        score = score + 1
        number = random.randrange(100)
        user = get_input()
    #NEVER VIOLATE OUR BELOVED MAMATA
        if number < user:
            slow_print("YOU ARE TELLING THAT THE Car IS FAST???? YOU LOST IDIOT!! LOVE MAMATA BANERJEE!!")
            lose = True
        else:
            slow_print("GOOD GUESS!!")
    #BYE BYE
    slow_print("\n \n Thanks for playing the Slow Speed Game!")


play_game()
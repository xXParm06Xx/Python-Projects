# The Perfect Guess Game

import random
import time

# generating a random no. by computer
number = random.randint(0,100)

def game():
    guesses = 1

    print("Choosing a Number...\n")
    time.sleep(0.5)
    print("A Number has been Chosen !!\n")
    time.sleep(0.5)
    
    while True:

        # Taking User Input
        user_input = int(input("Guess a Number : "))
        print("")

        time.sleep(0.5)
        print("Checking Number ....")
        time.sleep(0.5)
        
        # main logic
        if (user_input not in range(0,101)):
            print("Invalid Choice !! Try Again...\n")

        else:
            if (user_input > number):
                print("Lower Number Please...\n")
                guesses += 1
            
            elif (user_input < number):
                print("Higher Number Please...\n")
                guesses += 1
            
            elif (user_input == number):
                print("You Guessed Right !! You WON !!")
                print(f"You Took {guesses} Guesses !\n")
                break

print("Number Guessing Game ")
time.sleep(0.5)
print("Ready to PLAY?..")


while True:
    play = input("Y/N --> ").lower()

    if(play not in ["y","n"]):
        print("Invalid Choice !! Try Again...\n")
    
    elif(play == "n"):
        print("OK, Next Time..\n") # \n instead of print("")
        
        break
    
    else:
        game()
        break
        

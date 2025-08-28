# Rock Paper Scissor game

import random
import time

# Title
for char in "Rock Paper Scissor Game \n "" \n R for Rock \n P for Paper \n S for Scissor \n ":
   print(char,end="",flush=True)
   time.sleep(random.uniform(0.05,0.1))


n = [1, 0, -1]

gameDict = {"r":1, "p":0, "s":-1}
ruleDict = {1:"Rock", 0:"Paper", -1:"Scissor"}

user_score = 0
computer_score = 0  # initial values
round_no = 1

while (user_score < 5 and computer_score < 5): # loop to play again and again
    print(f"---- Round {round_no} ----")

    user_input = input("Enter your Choice R/P/S : ").lower()

    if (user_input not in gameDict):
        print("Invalid Choice !! Try Again...")
        print("")
        continue

    else:
      game = gameDict[user_input]
      computer = random.choice(n)  # random choice

      # using time messeges
      print(" Rock...")
      time.sleep(0.5)
      print(" Paper...")
      time.sleep(0.5)
      print(" Scissor...")
      time.sleep(0.5)
      print(" Shoot...\n")
      
      # Main Logic of The game
      if(computer == 1 and game == 0 or computer == 0 and game == -1 or computer == -1 and game == 1):
         print(f" You chose {ruleDict[game]}\nComputer Chose {ruleDict[computer]}")
         print("You WON !!")
         user_score +=1
        

      elif(computer == 0 and game == 1 or computer == -1 and game == 0 or computer == 1 and game == -1):
         print(f" You chose {ruleDict[game]}\nComputer Chose {ruleDict[computer]}")
         print("You Lose !!")
         computer_score +=1
        
    
      elif(computer == game): # when value is same
         print(f" You chose {ruleDict[game]}\nComputer Chose {ruleDict[computer]}")
         print("Its a Tie !!")
        
      print(f"Score: You {user_score} - {computer_score} Computer")
      round_no += 1
      time.sleep(1)
      print("")

# Final scores..
for char in "GAME OVER !!\n":
   print(char,end="",flush=True)
   time.sleep(0.2)

if(user_score > computer_score):
   for char in "Congrats, You WON the game !!":
    print(char,end="",flush=True)
    time.sleep(random.uniform(0.05,0.1))

elif(computer_score > user_score):
   for char in "Sadly, You LOST the game !!":
    print(char,end="",flush=True)
    time.sleep(random.uniform(0.05,0.1))

else:
   for char in "Its a TIE !!":
    print(char,end="",flush=True)
    time.sleep(random.uniform(0.05,0.1))

# END
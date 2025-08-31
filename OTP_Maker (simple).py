# a simple OTP Generator with user input

import random
import time


used_otps = set()

def otp():

    while True:
        myotp = random.randint(100000,999999)

        # creating unique OTP
        if myotp not in used_otps:
            used_otps.add(myotp)
            break 
    
    print("")
    time.sleep(0.5)
    print("Generating...\n")
    time.sleep(0.5)
    print(f"OTP is {myotp}")

print("--- OTP Generator ---\n")

# user input
print("Do You Want to generate OTP?")
while True:
    user_input = input(" Y/N --> ")

    try:
        if user_input.lower() == "y":
            otp()
            while True:
                print("")
                
                input2 = input("Do you want to generate again? Y/N : ")
                if input2.lower() == "y":
                    otp()
                elif input2.lower() == "n":
                    print("Ok, Next Time...")
                    break
                else:
                    print("Invalid input !!")
            break

        elif user_input.lower() == "n":
            print("Ok, Next Time...")
            break
        else:
            print("Invalid input !! Please try again...")

    except Exception as e:
        print("Invalid input !!")
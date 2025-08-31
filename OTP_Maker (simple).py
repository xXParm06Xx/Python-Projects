# a simple OTP Generator with user input

import random
import time


def otp():
    myotp = "".join([random.choice("0123456789")for _ in range(5)])
    
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
            break
        elif user_input.lower() == "n":
            print("Ok, Next Time...")
            break
        else:
            print("Invalid input !! Please try again...")

    except Exception as e:
        print("Invalid input !!")
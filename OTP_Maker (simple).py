# a simple OTP Generator

import random
import time

def otp():
    myotp = "".join([random.choice("0123456789")for _ in range(5)])
    
    print("")
    time.sleep(0.5)
    print("Generating...\n")
    time.sleep(0.5)
    print(f"OTP is {myotp}")


otp()
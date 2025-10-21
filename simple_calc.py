# Simple calculator

print("A Simple calculator")
print("  1. To Add")
print("  2. To Subtract")
print("  3. To Multiply")
print("  4. To Divide")

choice = int(input("Enter Your Choice (1/2/3/4) : "))

if choice in [1,2,3,4]:
 n1 = float(input("Enter First no. : "))
 n2 = float(input("Enter Second no. : #"))

 if(choice == 1):
  print(f"{n1} + {n2} = { n1 + n2}")

 elif(choice == 2):
  print(f"{n1} - {n2} = {n1 - n2}")

 elif(choice == 3):
  print(f"{n1} x {n2} = {n1*n2}")

 elif(choice == 4):
  if(n2 == 0 or n1 == 0):
   print("cannot divide by 0")
  else:
   print(f"{n1} / {n2} = {n1/n2}")

else:
 print("Choose from (1/2/3/4) only")

print("Thanks for trying")

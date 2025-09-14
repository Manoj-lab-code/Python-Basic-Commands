#Using nested conditions write a program for the given scenario.
#Generate a random number between 1 and 10. Then, Ask the user to guess the number and print a #message based on whether they get it right or not.


import random
x=random.randint(1,10)
user_input = int(input("guess a number between 1 and 10"))
if user_input>0:
  if x==user_input:
    print("you have won!!")
  else:
    print("you lose")
else:
  print("Enter only valid number")
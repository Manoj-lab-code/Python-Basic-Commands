#Write a program to sequence the age range using nested if- to check if the user age is within 50.

age = int(input("enter your age"))
if age<=50:
  print("your ages within 50")
  if age<5:
    print("toddler")
  elif age<13:
    print("child")
  elif age<20:
    print("teenagers")
  elif age<30:
    print("adult")
  elif age<40:
    print("middle aged")
  elif age<50:
    print("old")
  else:
    print("your exactly 50")
else:
  print("you are above 50")
    
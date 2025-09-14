#Write a program to check the snacks combo available for the amount in a theater
#- When you have 10 dollars --> popcorn available
#- When you have 15 dollars-> popcorn and nuggets available
#- When you have 5 dollars–> you get water bottle

money = int(input("enter amount of money"))
if money==10:
  print("popcorn available")
elif money==15:
  print("popcorn and nuggets available")
elif money==5:
  print("you get a waterbottle")
else:
  print("we dont have a menu for your money")
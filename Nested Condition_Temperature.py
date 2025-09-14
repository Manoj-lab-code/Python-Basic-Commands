#Write a python program using if…elif statements for the given scenario.
#Ask the user to enter a temperature in Celsius. The program should print a message based on the #temperature:
#If the temperature is less than -273.15,
#print that the
#temperature is invalid [because it is below absolute zero.]
#If it is exactly -273.15,
#print that the temperature is absolute 0
#If the temperature is between -273.15 and 0,
#print that the temperature is below freezing.
#If it is 0,
#print that the temperature is at the freezing point.
#If it is between 0 and 100,
#print that the
#temperature is in the normal range.
#If it is 100,
#print that the
#temperature is at the boiling point.
#If it is above 100,
#print that the
#temperature is above the boiling point.


tempurature = int(input("enter tempurature"))
if tempurature < -273.15:
  print("tempurature is invalid")
elif tempurature == -273.15:
  print("tempurature is absolute 0")
elif tempurature > -273.15 and tempurature <=0:
  print("tempurature is below freezing")
elif tempurature == 0:
  print("tempurature is at the freezing point")
elif tempurature > 0 and tempurature <=100:
  print(" tempurature is at the boiling point")
elif tempurature > 100:
  print("tempurature is above boiling point")
else:
  print("tempurature")
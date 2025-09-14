#Write the python program using conditional statements for the given scenario.
#Write a program to read an angle from the user and then displays its quadrant.

angle = float(input("Enter an angle(in degrees)"))
if angle>0 and angle<90:
  print("this is the first quadrant")
elif angle>90 and angle<180:
  print("this is the second quadrant")
elif angle>180 and angle<270:
  print("this is the third quadrant")
elif angle>270 and angle<360:
  print("this is the fourth quadrant")
elif angle==0:
  print("Its Zero angle")
elif angle==90:
  print("its a right angle")
elif angle==180:
  print("its a straight angle")
elif angle==270:
  print("its a reflex angle")
elif angle==360:
  print("full angle")
else:
  print("invalid number")
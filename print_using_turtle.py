#Using turtle, write the below statement:
#Computer is an Electronic Device.
#Computer has Hardware and Software components.
#It also has Input and Output devices



import turtle
pen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('red')
pen.penup()
pen.goto(-150,0)
pen.pendown()
pen.write("Computor is an Electronic Device\n")
pen.penup()
pen.goto(-150,-10)
pen.pendown()
pen.write("Computor has Hardware and Software components\n")
pen.penup()
pen.goto(-150,-20)
pen.pendown()
pen.write("It also has input and output devices\n")
turtle.done()


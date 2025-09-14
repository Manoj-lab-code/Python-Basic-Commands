#Question:Creating a python program using turtle module and write your name,Required details as #below,
#Title : “My First Turtle Graphics”
#Font style: Arial
#Font Size: 8
#Font type: Normal
#Align : Center
#Using the functions as,
#setposition()- to set the position of the turtle.
#screen.title()- To set the title for the screen and
#write() - To write the text.

Answer
import turtle
screen = turtle.Screen()
screen.title("My First Turtle Graphics")

# create turtle object
pen = turtle.Turtle()
pen.penup()
pen.setposition(0,0)
pen.pendown()

pen.write("i have so much aura", font=("calibre", 10))

turtle.done()

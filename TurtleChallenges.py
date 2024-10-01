import turtle
import random

def DrawCircle():
    for i in range (0,350):
        turtle.forward(1)
        turtle.right(1)
def DrawTriangle():
    for i in range (0,3):
        turtle.forward(50)
        turtle.right(240)
def DrawSquare():
    turtle.pendown()
    for i in range (0,4):
        turtle.forward(50)
        turtle.right(90)
def ThreeSquares(colour):
    turtle.color(colour,colour)
    turtle.begin_fill()
    DrawSquare()
    turtle.end_fill()
    turtle.penup()
    turtle.forward(75)
def DrawStar():
    for i in range (0,5):
        turtle.right(60)
        turtle.forward(50)
        turtle.right(155)
        turtle.forward(50)
def RandomTurtle():
    colour_tuple = ("yellow", "red", "blue", "green", "orange", "purple")
    NumOfLines = random.randint(10,20)
    turtle.pensize(5)
    for i in range(0, NumOfLines):
        Angle = random.randint(0, 360)
        Length = random.randint(10,70)
        turtle.color(random.choice(colour_tuple))
        turtle.right(Angle)
        turtle.forward(Length)

def TurtleGraphics():
    scr = turtle.Screen()
    turtle.shape("turtle")
    RandomTurtle()
    turtle.exitonclick()
def main():
    TurtleGraphics()

main()
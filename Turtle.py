import turtle
import math
from math import sin
from math import radians
from tkinter import *

root = Tk()
turtle.shape('turtle')


def turtleCircle():
    for x in range(0, 120):
        turtle.forward(8)
        turtle.left(3)


def turtleSquare10():
    a = 10
    b = -5
    for y in range(0,10):
        for x in range(0, 4):
            turtle.pendown()
            turtle.forward(a)
            turtle.left(90)
            turtle.penup()
        turtle.goto(b, b)
        a += 10
        b -= 5


def turtleFlover():
    for y in range(0, 4):
        for x in range(0, 180):
            turtle.forward(1)
            turtle.left(2)
        for x in range(0, 180):
            turtle.forward(1)
            turtle.right(2)
        turtle.left(45)


def turtleButterFly():
    turtle.right(90)
    n = 1
    for y in range(0, 4):
        for x in range(0, 120):
            turtle.forward(n)
            turtle.left(3)
        for x in range(0, 120):
            turtle.forward(n)
            turtle.right(3)
        n += 1


def turtleSpider():
    for x in range(0, 12):
        turtle.pendown()
        turtle.forward(100)
        turtle.stamp()
        turtle.right(180)
        turtle.penup()
        turtle.forward(100)
        turtle.right(210)


def turtleTwister():
    for x in range(180):
        turtle.forward(2 * x / 3.14)
        turtle.left(16)


def turtleSquareTwister():
    n = 20
    for y in range(0,20):
        for x in range(0, 2):
            turtle.forward(n)
            turtle.left(90)
        turtle.forward(10)
        n += 10


def turtleSmile():
    turtle.color("yellow")
    turtle.begin_fill()
    turtleCircle()
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-80, 180)
    turtle.pendown()
    turtle.color("blue")
    turtle.begin_fill()
    for x in range(0, 72):
        turtle.forward(2)
        turtle.left(5)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(80, 180)
    turtle.pendown()
    turtle.begin_fill()
    for x in range(0, 72):
        turtle.forward(2)
        turtle.left(5)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0, 180)
    turtle.pendown()
    turtle.color("red")
    turtle.width(10)
    turtle.right(90)
    turtle.forward(90)
    turtle.penup()
    turtle.goto(50, 80)
    turtle.pendown()
    for x in range(0, 40):
        turtle.forward(3)
        turtle.right(4)


def turtleDick():
    turtle.right(90)
    for x in range(0, 120):
        turtle.forward(2)
        turtle.left(3)
    for x in range(0, 120):
        turtle.forward(2)
        turtle.right(3)
    turtle.penup()
    turtle.left(180)
    for x in range(0, 30):
        turtle.forward(2)
        turtle.left(3)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(200)
    for x in range(0, 60):
        turtle.forward(2)
        turtle.right(3)
    turtle.right(90)
    turtle.forward(76)
    turtle.right(180)
    turtle.penup()
    turtle.forward(38)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(38)
    turtle.penup()
    turtle.right(180)
    turtle.forward(38)
    turtle.left(90)
    turtle.forward(38)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(200)


# r = z / (2 * (sin(360 / (2 * n))))
# z = 2 * r * sin(radians(360) / (2 * n))

def turtle_nCorners():
    r = 30
    n = 3
    for y in range(0, 10):
        degr = 90 + ((360 / n) / 2)
        z = 2 * r * sin(radians(180) / n)
        # z = r / 2
        turtle.left(degr)
        for x in range(0, n):
            turtle.forward(z)
            turtle.left(360 / n)
        turtle.penup()
        turtle.right(degr)
        turtle.forward(15)
        turtle.pendown()
        r += 15
        n += 1

def turtle_el_pruzhino():
    turtle.left(90)
    for y in range(0, 4):
        for x in range(0, 39):
            turtle.forward(5)
            turtle.right(5)
        for x in range(0, 20):
            turtle.forward(1)
            turtle.right(8)


def turtle_star5(n):
    turtle.left(180)
    for x in range(n):
        turtle.forward(200)
        turtle.left((360 / (n / 2)))

def turtle_star11(n):
    for x in range(n):
        turtle.forward(200)
        turtle.left((360 / (n / 6)))


turtle_nCorners()

root.mainloop()

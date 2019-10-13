import turtle

turtle.shape('turtle')

def turtleCircle():
    for x in range(0, 120):
        turtle.forward(8)
        turtle.left(3)

def turtleSquare10():
    for x in range(0, 4):
        turtle.pendown()
        turtle.forward(10)
        turtle.left(90)
        turtle.penup()
    turtle.goto(-5,-5)

    for x in range(0, 4):
        turtle.pendown()
        turtle.forward(20)
        turtle.left(90)
        turtle.penup()
    turtle.goto(-10, -10)

    for x in range(0, 4):
        turtle.pendown()
        turtle.forward(30)
        turtle.left(90)
        turtle.penup()
    turtle.goto(-15, -15)

    for x in range(0, 4):
        turtle.pendown()
        turtle.forward(40)
        turtle.left(90)
        turtle.penup()
    turtle.goto(-20, -20)

    for x in range(0, 4):
        turtle.pendown()
        turtle.forward(50)
        turtle.left(90)
        turtle.penup()
    turtle.goto(-25, -25)

    for x in range(0, 4):
        turtle.pendown()
        turtle.forward(60)
        turtle.left(90)
        turtle.penup()
    turtle.goto(-30, -30)

    for x in range(0, 4):
        turtle.pendown()
        turtle.forward(70)
        turtle.left(90)
        turtle.penup()
    turtle.goto(-35, -35)

    for x in range(0, 4):
        turtle.pendown()
        turtle.forward(80)
        turtle.left(90)
        turtle.penup()
    turtle.goto(-40, -40)

    for x in range(0, 4):
        turtle.pendown()
        turtle.forward(90)
        turtle.left(90)
        turtle.penup()
    turtle.goto(-45, -45)

    for x in range(0, 4):
        turtle.pendown()
        turtle.forward(100)
        turtle.left(90)
        turtle.penup()
    turtle.goto(-50, -50)


def turtleFlover():
    for x in range(0, 180):
        turtle.forward(1)
        turtle.left(2)
    for x in range(0, 180):
        turtle.forward(1)
        turtle.right(2)
    turtle.left(46)
    for x in range(0, 180):
        turtle.forward(1)
        turtle.left(2)
    for x in range(0, 180):
        turtle.forward(1)
        turtle.right(2)
    turtle.left(46)
    for x in range(0, 180):
        turtle.forward(1)
        turtle.left(2)
    for x in range(0, 180):
        turtle.forward(1)
        turtle.right(2)
    turtle.left(46)
    for x in range(0, 180):
        turtle.forward(1)
        turtle.left(2)
    for x in range(0, 180):
        turtle.forward(1)
        turtle.right(2)



def turtleButterFly():
    turtle.right(90)
    for x in range(0, 120):
        turtle.forward(1)
        turtle.left(3)
    for x in range(0, 120):
        turtle.forward(1)
        turtle.right(3)

    for x in range(0, 120):
        turtle.forward(2)
        turtle.left(3)
    for x in range(0, 120):
        turtle.forward(2)
        turtle.right(3)

    for x in range(0, 120):
        turtle.forward(3)
        turtle.left(3)
    for x in range(0, 120):
        turtle.forward(3)
        turtle.right(3)

    for x in range(0, 120):
        turtle.forward(4)
        turtle.left(3)
    for x in range(0, 120):
        turtle.forward(4)
        turtle.right(3)


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
    for x in range(0, 30):
        turtle.forward(1)
        turtle.left(6)
    for x in range(0, 36):
        turtle.forward(1)
        turtle.left(5)
    for x in range(0, 45):
        turtle.forward(1)
        turtle.left(4)
    for x in range(0, 60):
        turtle.forward(1)
        turtle.left(3)
    for x in range(0, 90):
        turtle.forward(1)
        turtle.left(2)
    for x in range(0, 180):
        turtle.forward(1)
        turtle.left(1)


def turtleSquareTwister():
    for x in range(0,2):
        turtle.forward(20)
        turtle.left(90)
    turtle.forward(10)
    for x in range(0,2):
        turtle.forward(30)
        turtle.left(90)
    turtle.forward(10)
    for x in range(0,2):
        turtle.forward(40)
        turtle.left(90)
    turtle.forward(10)
    for x in range(0,2):
        turtle.forward(50)
        turtle.left(90)
    turtle.forward(10)
    for x in range(0,2):
        turtle.forward(60)
        turtle.left(90)
    turtle.forward(10)
    for x in range(0, 2):
        turtle.forward(70)
        turtle.left(90)
    turtle.forward(10)
    for x in range(0, 2):
        turtle.forward(80)
        turtle.left(90)
    turtle.forward(10)
    for x in range(0, 2):
        turtle.forward(90)
        turtle.left(90)
    turtle.forward(10)
    for x in range(0, 2):
        turtle.forward(100)
        turtle.left(90)
    turtle.forward(10)
    for x in range(0, 2):
        turtle.forward(110)
        turtle.left(90)
    turtle.forward(10)
    for x in range(0, 2):
        turtle.forward(120)
        turtle.left(90)


def turtleSmile():
    turtle.color("yellow")
    turtle.begin_fill()
    turtleCircle()
    turtle.end_fill()
    turtle.penup()
    turtle.goto (-80, 180)
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





turtleSmile()




















import turtle
from turtle import *

# t = turtle()

bgcolor("black")
colorS = ["yellow", "red", "purple", "green"]
pensize(5)


def H():
    color("yellow")

    left(90)
    forward(150)
    back(75)
    right(90)
    forward(50)
    left(90)
    forward(75)
    back(150)
def A():
    color("green")
    right(10)
    forward(155)
    back(100)
    right(80)
    forward(35)
    left(100)
    forward(100)
    back(155)
    right(10)

def P():
    color("red")
    forward(155)
    back(100)
    right(90)
    circle(50,180)
    right(90)
    back(155)

def Y():
    color('violet')
    forward(50)
    left(15)
    forward(110)
    back(110)
    right(30)
    forward(110)
    back(110)
    left(15)
    back(50)

def N():
    color("pink")
    forward(155)
    right(165)
    forward(160)
    left(165)
    forward(155)
    back(155)

def E():
    color("brown")
    right(90)
    forward(55)
    back(55)
    left(90)
    forward(85)
    right(90)
    forward(35)
    back(35)
    left(90)
    forward(70)
    right(90)
    forward(55)
    back(55)
    left(90)
    back(155)

def W():
    color("light yellow")
    left(15)
    forward(160)
    back(160)
    right(30)
    forward(75)
    right(150)
    forward(75)
    left(180)
    right(30)
    forward(160)
    back(160)
    left(15)



penup()
goto(-300, 100)
pendown()
H()
penup()
goto(-240,100)
pendown()
A()
penup()
goto(-175,100)
pendown()
P()
penup()
goto(-120,100)
pendown()
P()
penup()
goto(-50,100)
pendown()
Y()
penup()
goto(-130,-80)
pendown()
N()
penup()
goto(-80,-80)
pendown()
E()
penup()
goto(10,-80)
pendown()
W()
done()
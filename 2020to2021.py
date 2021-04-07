import turtle
from turtle import *
import random
import time
from pygame import mixer

t = turtle.Turtle()
mixer.init()
mixer.music.load("C:/Users/Manav/Downloads/avengers_infinitywar.mp3")
mixer.music.play(2)
colours = ["cyan", "red", "green", "violet", "yellow", "orange"]
col = random.choice(colours)
bgcolor("black")
speed(10 ^ 100)
pensize(5)


def a():
    color("violet")
    penup()
    goto(-180, 60)
    pendown()
    back(100)
    left(90)
    forward(100)
    right(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)


def b():
    color("yellow")
    penup()
    goto(-130, 60)
    pendown()
    right(90)
    forward(200)
    right(90)
    forward(100)
    right(90)
    forward(200)
    right(90)
    forward(100)


def c():
    color("green")
    penup()
    goto(110, 60)
    pendown()
    right(180)
    back(100)
    left(90)
    forward(100)
    right(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)


def d():
    color("orange")
    penup()
    goto(150, 60)
    pendown()
    right(90)
    forward(200)
    right(90)
    forward(100)
    right(90)
    forward(200)
    right(90)
    forward(100)


def e():
    color("orange")
    penup()
    goto(180, 60)
    pendown()
    right(90)
    forward(200)
    left(120)
    forward(30)


time.sleep(7)
a()
b()
c()
d()
penup()
goto(150, -25)

hideturtle()
color("yellow")
turtle.write(arg='Was a mess.....', move=True, align="center", font=("arial", 24, "bold"))
time.sleep(2)
goto(0, -50)
turtle.write(arg="Don't worry someone is coming to save you!!!!", move=True, align="center",
             font=("verdana", 20, "normal"))
time.sleep(3)
reset()
pensize(8)
a()
b()
c()
e()
penup()
goto(2, -5)
turtle.write(arg="coming soon....", move=True, align='center', font=("verdana", 30, "bold"))
hideturtle()

time.sleep(2)

done()

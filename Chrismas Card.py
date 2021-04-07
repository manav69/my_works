from turtle import *
import random

colors=["cyan","yellow","light yellow","red","green"]
n=45
speed(0)
pensize(2)
bgcolor(0,0,0)

penup()
goto(0,-130)
pendown()
left(90)
forward(3*n)
color("yellow","yellow")
begin_fill()
left(126)
for i in range(5) :   #this draws star
    forward(n/5)
    right(144)
    forward(n/5)
    left(72)
end_fill()
right(126)
color("white")
backward(n*4.8)
def tree(d,s):
    pensize(4)
    if d<=0:
        return
    forward(s)
    tree(d-1,s*.8)
    right(120)
    tree(d-3,s*.6)
    right(120)
    tree(d - 3, s * .6)
    right(120)
    backward(s)


def lenght_select():
    return random.randint(5, 8)


def stars(x,y):
    hideturtle()
    col=random.choice(colors)
    l=lenght_select()
    color(col)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(5):
        forward(l)
        right(144)
    end_fill()


tree(12,n)#branches,45
backward(n/2)#trunk
color("light yellow")
begin_fill()
penup()
goto(-180,240)
circle(25)
end_fill()


pensize(2)
onscreenclick(stars,1)#1 means left click
# stars will take two parameters i.e x and y
done()


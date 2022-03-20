from turtle import *
import turtle
wm = turtle.Screen()

def draw(x,y):
    t.goto(x,y)
def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def moveup():
    t.goto(t.xcor(),t.ycor() + 5)
def movedown():
    t.goto(t.xcor(),t.ycor() - 5)
def moveleft():
    t.goto(t.xcor() - 5,t.ycor())
def moveright():
    t.goto(t.xcor() + 5,t.ycor())
def color_r():
    t.color("red")
def color_g():
    t.color("green")
def color_b():
    t.color("blue")
def plus_pensize():
    t.psize += 1
    t.pensize(t.psize)
def minus_pensize():
    t.psize -= 1
    t.pensize(t.psize)
def startfill():
    t.begin_fill()
def finishfill():
    t.end_fill()
def bgcolor_w():
    wm.bgcolor("white")
def bgcolor_b():
    wm.bgcolor("black")
def bgcolor_a():
    wm.bgcolor("aquamarine")
def changehidden():
    if t.showen == True:
        t.showen = False
        t.hideturtle()
    else:
        t.showen = True
        t.showturtle()
def eraser():
    t.clear()
def changeshape():
    if t.form == 0:
        t.form += 1
        t.shape("triangle")
    elif t.form == 1:
        t.form += 1
        t.shape("arrow")
    elif t.form == 2:
        t.form += 1
        t.shape("turtle")
    elif t.form == 3:
        t.form += 1
        t.shape("circle")
    elif t.form == 4:
        t.form += 1
        t.shape("square")
    else:
        t.form = 0
        t.shape("classic")


t = Turtle()
t.shape("circle")
t.color("blue")
t.ondrag(draw)
t.speed(100)
t.psize = 1
t.showen = True
t.form = 0

scr = t.getscreen()
scr.onscreenclick(move)
scr.listen()
scr.onkey(moveup, "w")
scr.onkey(movedown, "s")
scr.onkey(moveleft, "a")
scr.onkey(moveright, "d")
scr.onkey(color_r, "r")
scr.onkey(color_g, "g")
scr.onkey(color_b, "b")
scr.onkey(plus_pensize, "Up")
scr.onkey(minus_pensize, "Down")
scr.onkey(startfill, "Left")
scr.onkey(finishfill, "Right")
scr.onkey(bgcolor_w, "z")
scr.onkey(bgcolor_b, "x")
scr.onkey(bgcolor_a, "c")
scr.onkey(changehidden, "space")
scr.onkey(eraser, "e")
scr.onkey(changeshape, "f")

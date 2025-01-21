import turtle
sm = turtle.Screen()
sm.bgcolor("white")
sm.title("House Drawing")
h = turtle.Turtle()
h.speed(5) 
def square(colour, side):
    h.fillcolor(colour)
    h.begin_fill()
    for i in range(4):
        h.fd(side)
        h.left(90)
    h.end_fill()
def triangle(colour, side):
    h.fillcolor(colour)
    h.begin_fill()
    for i in range(3):
        h.fd(side)
        h.left(120)
    h.end_fill()
def rectangle(colour, w, h_height):
    h.fillcolor(colour)
    h.begin_fill()
    for i in range(2):
        h.fd(w)
        h.left(90)
        h.fd(h_height)
        h.left(90)
    h.end_fill()
h.penup()
h.goto(-50, -50)
h.pendown()
triangle("red", 100)
h.penup()
h.goto(-50, -150)
h.pendown()
square("blue", 100)
h.penup()
h.goto(-20, -150)
h.pendown()
rectangle("brown", 40, 60)
h.hideturtle()
turtle.done()


import turtle
import random
sm=turtle.Screen()
sm.title("night")
sm.bgcolor("dark blue")
s=turtle.Turtle()
s.speed(0)
s.hideturtle()
def star(tur,si):
    s.begin_fill()
    for i in range(5):
        s.fd(si)
        s.right(144)
    s.end_fill()
s.color("yellow")
for i in range(20):
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    si=random.randint(10,30)
    s.penup()
    s.goto(x,y)
    s.pendown()
    star(s,si)
turtle.done()


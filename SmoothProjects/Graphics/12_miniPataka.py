import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")

t.speed(0)

colors = ["red","yellow","blue","green","orange","violet"]

for i in range(20):
    t.penup()
    t.goto(random.randint(-200,200), random.randint(-200,200))
    t.pendown()
    t.color(random.choice(colors))

    for j in  range(10):
        t.forward(30)
        t.backward(30)
        t.right(36)

turtle.done()
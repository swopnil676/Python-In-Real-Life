import turtle
from turtle import done
import colorsys

p=turtle.Turtle()
s=turtle.Screen()
s.title("StudyMuch")
s.bgcolor("black")
p.pensize(2.0)
p.speed(0)
n=36
h=0.5

for i in range(72):
    h+=1/n
    p.color(colorsys.hsv_to_rgb(h,1,1))
    p.right(5)
    for j in range(5):
        p.backward(250)
        p.right(144)

done()
from turtle import *
from colorsys import *
from colorsys import hsv_to_rgb

tracer(50)
bgcolor('black')
hideturtle()
pensize(2)

for _ in range(15):
    for i in range(200):
        color(hsv_to_rgb(i / 200, 1, 1))
        forward(i * 1.2)
        backward(i * 1.2)
        left(89)
    left(24)
done()
from turtle import *
import colorsys as cs

bgcolor('darkblue')
pensize(2)
tracer(3)    # Controls screen refresh rate

h = 0.3
r = 70

penup()
goto(-50,-200)
pendown()

for i in range(700):
    color(cs.hsv_to_rgb(h,1,1))
    h += 0.03
    forward(r-i * 0.1)
    lt(300)
    forward(r-i * 0.1)
    lt(150)
    forward(r-i * 0.1)
    lt(300)

done()
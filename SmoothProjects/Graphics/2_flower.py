from turtle import *
import colorsys

tracer(10)
bgcolor("black")
h = 0
for i in range(16):
    for j in range(10):
        color(colorsys.hsv_to_rgb(h,1,1))
        h += 0.005
        rt(90)
        circle(150 - j*6 ,90)
        lt(90)
        circle(150 - j*6 ,90)
        rt(180)
    circle(40, 24)

done()
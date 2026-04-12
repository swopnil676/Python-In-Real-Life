from turtle import * 
import colorsys

speed(0)
bgcolor("black")
width(1)
colormode(1.0)

h=0

for i in range(500):
    c = colorsys.hsv_to_rgb(h,1,1)
    pencolor(c)

    circle(i*0.5)
    left(59)

    h += 0.003

done()
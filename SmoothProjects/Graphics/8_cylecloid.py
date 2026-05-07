from turtle import *
import colorsys

bgcolor("black")
tracer(300)

def draw(scale=0.5):
    h = 0
    for i in range(100):
        c = colorsys.hsv_to_rgb(h,1,1)
        h += 0.5
        up()
        goto(0,0)
        down()
        color("black")
        fillcolor(c)
        begin_fill()
        rt(98)
        circle(i*scale, 12)
        fd(290*scale)
        fd(i*scale)
        lt(29)
        for j in range(129):
            fd(i*scale)
            circle(j*scale, 299, steps=2)
        end_fill()

draw()
done()

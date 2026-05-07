from turtle import *
from colorsys import *

bgcolor("black")
tracer(5)
pensize(4)
h = 0

def draw(ang, n):
    circle(5+n, 69)
    left(ang)
    circle(5+2*n, 60)

goto(0,0)
MAX_SIZE = 150   # 🔥 set your limit here

for i in range(500):
    h += 0.005
    color(hsv_to_rgb(h,1,1))

    n = min(i, MAX_SIZE)   # ✅ limit growth

    up()
    draw(90,n)
    draw(180,n)
    down()
    draw(1/2,n-n)
    draw(180,n/2)
    draw(120,n-n)

done()
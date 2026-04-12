import turtle
import colorsys

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")

# screen.tracer(0)   # 🚀 Turn off animation

t.speed(0)
t.width(2)

h = 0

for i in range(400):
    t.pencolor(colorsys.hsv_to_rgb(h,1,1))
    h += 0.005

    t.forward(i*2)
    t.left(121)

# screen.update()   # ✅ Show drawing instantly
turtle.done()
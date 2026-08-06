    # Noob version

# import turtle

# screen = turtle.Screen()
# screen.setup(700, 700)

# t = turtle.Turtle()
# t.speed(0)

# # Outer circle
# t.penup()
# t.goto(0, -200)
# t.pendown()
# t.circle(200)

# # Three spokes
# for angle in [90, 210, 330]:
#     t.penup()
#     t.goto(0, 0)
#     t.setheading(angle)
#     t.pendown()
#     t.forward(180)

# turtle.done()


    # Legend version

import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("white")
screen.title("Mercedes-Benz Logo")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(4)

OUTER_RADIUS = 220
INNER_RADIUS = 190

# Draw outer ring
t.penup()
t.goto(0, -OUTER_RADIUS)
t.pendown()
t.circle(OUTER_RADIUS)

t.penup()
t.goto(0, -INNER_RADIUS)
t.pendown()
t.circle(INNER_RADIUS)

# Draw 3-pointed star
for angle in [90, 210, 330]:
    x = INNER_RADIUS * math.cos(math.radians(angle))
    y = INNER_RADIUS * math.sin(math.radians(angle))

    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.goto(x, y)

# Small center circle
t.penup()
t.goto(0, -12)
t.pendown()
t.circle(12)

turtle.done()
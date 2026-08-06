import turtle
import colorsys
import math

def setup():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=800)
    screen.tracer(5)
    return screen

def draw_phyllotaxis_neon():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    phi = 137.508 * (math.pi / 180)
    c = 4
    
    for n in range(600):
        r = c * math.sqrt(n)
        theta = n * phi
        
        # Calculate coordinates
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        
        # Color transition strategy
        h = n / 600
        color = colorsys.hsv_to_rgb(h, 1, 1)
        
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color(color)
        t.dot(7)

setup()
draw_phyllotaxis_neon()
turtle.done()
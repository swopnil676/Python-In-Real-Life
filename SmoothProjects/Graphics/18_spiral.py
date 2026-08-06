import turtle

def draw_dynamic_spiral():
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Colorful Animated Spiral")

    t = turtle.Turtle()
    t.speed(0)
    t.width(2)

    colors = ["red", "purple", "blue", "green", "yellow", "orange"]

    for x in range(500):
        t.pencolor(colors[x % 6])
        t.forward(x)
        t.left(59)

    window.exitonclick()

draw_dynamic_spiral()
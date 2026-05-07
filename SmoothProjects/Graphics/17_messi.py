        # <--- Method 1 --->
# from sketchpy import canvas

# Turtle = canvas.sketch(x_offset=290, y_offset=320)

# Turtle.draw_fn("face_out",     co=(233, 183, 151), mode=0)
# Turtle.draw_fn("beard_out",    co=(30, 25, 31),    mode=0)
# Turtle.draw_fn("chin1",        co=(204, 139, 124), mode=0)
# Turtle.draw_fn("chin2",        co=(204, 139, 124), mode=0)
# Turtle.draw_fn("lip_lower",    co=(214, 125, 100), mode=0)
# Turtle.draw_fn("lip_upper",    co=(186, 30, 21),   mode=0)
# Turtle.draw_fn("nostril",      co=(8, 15, 29),     mode=0)
# Turtle.draw_fn("nose_curve",   co=(128, 69, 56),   mode=0)
# Turtle.draw_fn("right_eyebrow",co=(12, 16, 22),    mode=0)
# Turtle.draw_fn("left_eyebrow", co=(12, 16, 22),    mode=0)
# More code lines below...


        # <--- Method 1 --->
import turtle
import math

# Setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Messi Portrait")
screen.setup(800, 700)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_filled_shape(points, color):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0])
    t.end_fill()

def draw_circle_filled(x, y, r, color):
    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def draw_ellipse(x, y, rx, ry, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    for angle in range(361):
        rad = math.radians(angle)
        px = x + rx * math.cos(rad)
        py = y + ry * math.sin(rad)
        t.goto(px, py)
    t.end_fill()

# ── SKIN COLOR ──
SKIN       = "#E9B78E"
SKIN_DARK  = "#CC9B6D"
SKIN_SHAD  = "#C8875A"
BEARD      = "#1E1812"
HAIR       = "#1A1008"
LIP_LOW    = "#D67D64"
LIP_UP     = "#BA1E15"
EYE_WHITE  = "white"
EYE_COLOR  = "#3A3020"
BROW       = "#0C1016"

# ── FACE BASE ──
face = [
    (-60, 200), (-90, 150), (-110, 80), (-115, 0),
    (-100, -80), (-80, -150), (-50, -200),
    (0, -220), (50, -200), (80, -150),
    (100, -80), (110, 0), (100, 80),
    (80, 150), (50, 200), (0, 210)
]
draw_filled_shape(face, SKIN)

# ── HAIR (top) ──
hair_top = [
    (-60, 200), (-80, 220), (-60, 260), (-20, 280),
    (30, 275), (70, 260), (90, 230), (80, 200),
    (50, 210), (0, 215), (-30, 210)
]
draw_filled_shape(hair_top, HAIR)

# ── HAIR SIDE / BACK ──
hair_side = [
    (80, 150), (100, 180), (110, 230), (105, 270),
    (90, 230), (80, 200), (100, 80)
]
draw_filled_shape(hair_side, HAIR)

# ── BEARD (main dark mass) ──
beard = [
    (-80, -80), (-90, -120), (-70, -180), (-40, -215),
    (0, -225), (40, -215), (70, -180),
    (85, -120), (75, -80), (60, -60),
    (20, -50), (-20, -50), (-60, -60)
]
draw_filled_shape(beard, BEARD)

# ── MUSTACHE ──
mustache = [
    (-45, -60), (-20, -75), (0, -72), (20, -75),
    (45, -60), (30, -55), (0, -65), (-30, -55)
]
draw_filled_shape(mustache, BEARD)

# ── CHIN HIGHLIGHT ──
chin = [
    (-15, -195), (0, -210), (15, -195),
    (10, -180), (0, -185), (-10, -180)
]
draw_filled_shape(chin, SKIN_DARK)

# ── LIPS lower ──
lip_lower = [
    (-25, -85), (0, -95), (25, -85),
    (20, -75), (0, -80), (-20, -75)
]
draw_filled_shape(lip_lower, LIP_LOW)

# ── LIPS upper ──
lip_upper = [
    (-25, -75), (-10, -65), (0, -68),
    (10, -65), (25, -75), (15, -78),
    (0, -73), (-15, -78)
]
draw_filled_shape(lip_upper, LIP_UP)

# ── NOSE ──
nose = [
    (-5, 20), (-15, -10), (-20, -35),
    (-10, -50), (0, -52), (10, -50),
    (18, -35), (12, -10), (5, 20)
]
draw_filled_shape(nose, SKIN_SHAD)

# Nostril left
nostril_l = [(-18, -42), (-25, -50), (-15, -55), (-8, -48)]
draw_filled_shape(nostril_l, BEARD)

# Nostril right
nostril_r = [(18, -42), (25, -50), (15, -55), (8, -48)]
draw_filled_shape(nostril_r, BEARD)

# ── RIGHT EYE ──
# Eye white
eye_r = [(-70, 80), (-50, 90), (-30, 88), (-25, 80),
         (-35, 72), (-55, 70), (-75, 74)]
draw_filled_shape(eye_r, EYE_WHITE)
# Iris
draw_circle_filled(-48, 72, 10, EYE_COLOR)
# Pupil
draw_circle_filled(-48, 72, 5, "black")

# ── LEFT EYE (slightly hidden in 3/4 view) ──
eye_l = [(20, 82), (35, 90), (55, 88), (58, 80),
         (50, 72), (30, 72), (18, 76)]
draw_filled_shape(eye_l, EYE_WHITE)
draw_circle_filled(38, 74, 9, EYE_COLOR)
draw_circle_filled(38, 74, 4, "black")

# ── RIGHT EYEBROW ──
brow_r = [(-80, 108), (-60, 118), (-30, 115), (-22, 108),
          (-32, 104), (-62, 106), (-78, 100)]
draw_filled_shape(brow_r, BROW)

# ── LEFT EYEBROW ──
brow_l = [(15, 110), (35, 120), (60, 116), (68, 108),
          (58, 103), (32, 106), (13, 104)]
draw_filled_shape(brow_l, BROW)

# ── EAR (right side, partially visible) ──
ear = [(95, 60), (115, 40), (120, 10), (118, -20),
       (108, -40), (95, -30), (100, 0), (98, 30)]
draw_filled_shape(ear, SKIN_DARK)

# ── NECK ──
neck = [(-30, -215), (30, -215), (40, -280), (-40, -280)]
draw_filled_shape(neck, SKIN)

# ── SHADOW under jaw ──
jaw_shadow = [
    (-60, -160), (-80, -130), (-85, -90),
    (-70, -80), (-60, -120), (-40, -155)
]
draw_filled_shape(jaw_shadow, SKIN_SHAD)

turtle.done()
import cairo
import math

WIDTH, HEIGHT = 600, 600

# Create image surface
surface = cairo.ImageSurface(
    cairo.FORMAT_ARGB32,
    WIDTH,
    HEIGHT
)

# Create drawing context
ctx = cairo.Context(surface)

# Black background
ctx.set_source_rgb(0, 0, 0)
ctx.paint()

# Draw spiral dots
for i in range(200):

    angle = i * 0.1

    x = 300 + math.cos(angle) * angle * 10
    y = 300 + math.sin(angle) * angle * 10

    ctx.set_source_rgba(1, 1, 1, 0.5)

    ctx.arc(x, y, 5, 0, 2 * math.pi)

    ctx.fill()

# Save image
surface.write_to_png("spiral.png")
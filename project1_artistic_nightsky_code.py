import turtle # Import turtle module
import random # Import random module

# Create a screen object
screen = turtle.Screen()
screen.bgcolor("midnightblue")
screen.tracer(0)  # speed up drawing

# Create a Turtle for drawing
pen_turtle = turtle.Turtle()
pen_turtle.speed(0)  # Set the drawing speed to maximum
pen_turtle.shape("blank")

# determine screen borders
width = screen.window_width()
height = screen.window_height()
ground = -height // 2  # bottom edge of the screen

def draw_star(starlength):
    pen_turtle.color("white")
    pen_turtle.setheading(0) # always position to the same direction
    pen_turtle.forward(starlength/2)
    pen_turtle.backward(starlength/4)
    pen_turtle.left(90)
    pen_turtle.forward(starlength/2)
    pen_turtle.backward(starlength)

def draw_triangle(p1, p2, p3, color):
    pen_turtle.penup()
    pen_turtle.goto(p1)
    pen_turtle.color(color)
    pen_turtle.pendown()
    pen_turtle.begin_fill()
    pen_turtle.goto(p2)
    pen_turtle.goto(p3)
    pen_turtle.goto(p1)
    pen_turtle.end_fill()

def draw_mountain(x, mountain_width, mountain_height, color):
    peak = (x, ground + mountain_height)
    left = (x - mountain_width / 2, ground)
    right = (x + mountain_width / 2, ground)
    draw_triangle(left, peak, right, color)
    # snow cap: top part of the mountain
    share = 0.3
    snow_y = peak[1] - share * mountain_height
    snow_left = (x - share * mountain_width / 2, snow_y)
    snow_right = (x + share * mountain_width / 2, snow_y)
    draw_triangle(snow_left, peak, snow_right, "white")

def draw_circle(x, y, radius, color):
    pen_turtle.penup()
    pen_turtle.goto(x, y - radius) # circle() starts at the bottom of the circle
    pen_turtle.setheading(0)
    pen_turtle.color(color)
    pen_turtle.pendown()
    pen_turtle.begin_fill()
    pen_turtle.circle(radius)
    pen_turtle.end_fill()

def draw_moon(x, y, radius):
    draw_circle(x, y, radius, "lightyellow")
    # crater spots
    draw_circle(x - radius * 0.3, y + radius * 0.3, radius * 0.2, "khaki")
    draw_circle(x + radius * 0.4, y - radius * 0.2, radius * 0.15, "khaki")
    draw_circle(x - radius * 0.1, y - radius * 0.5, radius * 0.12, "khaki")

def draw_tree(x, tree_height):
    trunk_width = tree_height * 0.15
    trunk_height = tree_height * 0.25
    # trunk (brown rectangle made of two triangles)
    draw_triangle((x - trunk_width / 2, ground),
                  (x - trunk_width / 2, ground + trunk_height),
                  (x + trunk_width / 2, ground + trunk_height), "saddlebrown")
    draw_triangle((x - trunk_width / 2, ground),
                  (x + trunk_width / 2, ground),
                  (x + trunk_width / 2, ground + trunk_height), "saddlebrown")
    # three stacked green triangles as treetop
    for i in range(3):
        base_y = ground + trunk_height + i * tree_height * 0.22
        half_width = tree_height * (0.3 - i * 0.07)
        draw_triangle((x - half_width, base_y),
                      (x, base_y + tree_height * 0.35),
                      (x + half_width, base_y), "darkgreen")

# draw stars:
for _ in range(100): # number of stars
    x = random.randint(-width // 2, width // 2)
    y = random.randint(-height // 2, height // 2)
    
    pen_turtle.penup()
    pen_turtle.goto(x, y)
    pen_turtle.pendown()
    
    draw_star(random.randint(6, 20))

# draw moon:
draw_moon(width // 3, height // 3, 50)

# draw mountains:
draw_mountain(-200, 400, 250, "slategray")
draw_mountain(200, 450, 300, "slategray")
draw_mountain(0, 350, 180, "dimgray")
draw_mountain(-330, 300, 150, "dimgray")

# draw trees (in front of the mountains):
for _ in range(8):
    draw_tree(random.randint(-width // 2, width // 2), random.randint(60, 120))

screen.exitonclick()
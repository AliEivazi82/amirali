import turtle
import random
colors = ["red", "blue", "lime", "pink"]

pen = turtle.Turtle()

x = 0
for color in colors:
    pen.pendown()
    pen.pencolor(random.choice(colors))
    pen.pensize(10)
    # pen.fillcolor(color)
    # pen.begin_fill()
    pen.circle(50)
    # pen.end_fill()
    pen.penup()
    x -= 45
    pen.goto(x,0)

turtle.done()

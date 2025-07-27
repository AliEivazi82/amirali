import turtle

pen = turtle.Turtle()

pen.fillcolor("skyblue")
pen.begin_fill()
for i in range(4):
    pen.fd(100)
    pen.right(90)
pen.end_fill()

pen.penup()

pen.goto(0,10)

pen.pendown()
pen.begin_fill()
for i in range(4):
    pen.fd(100)
    pen.left(90)
pen.end_fill()

pen.penup()

pen.goto(-110,10)

pen.pendown()
pen.begin_fill()
for i in range(4):
    pen.fd(100)
    pen.left(90)
pen.end_fill()

turtle.done()
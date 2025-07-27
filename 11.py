import turtle

pen = turtle.Turtle()

pen.color("red")
pen.pensize(15)

pen.fillcolor("black")
pen.begin_fill()
for i in range(8):
    pen.forward(100)
    pen.right(45)
pen.end_fill()

pen.fillcolor("gold")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

turtle.done()

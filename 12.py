import turtle

pen = turtle.Turtle()

pen.fillcolor("blue")
pen.begin_fill()
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.end_fill()

pen.left(45)

pen.fillcolor("red")
pen.begin_fill()
pen.forward(75)
pen.right(90)
pen.fd(75)
pen.end_fill()


turtle.done()
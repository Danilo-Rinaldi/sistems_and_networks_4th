import turtle
for _ in range(4):
    for _ in range(4):
        for _ in range(4):
            turtle.forward(10)
            turtle.left(90)
        turtle.forward(10)
    turtle.backward(40)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)

turtle.done()

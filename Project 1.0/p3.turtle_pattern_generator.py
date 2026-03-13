import turtle

sides = int(input("Enter number of sides: "))
repetitions = int(input("Enter number of shapes: "))

angle = 360 / sides

for i in range(repetitions):
    for j in range(sides):
        turtle.forward(100)
        turtle.left(angle)

    turtle.left(10)

turtle.done()
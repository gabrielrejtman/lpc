# library that allows us to use shapes through commands
import turtle
import math


def build_fibonacci(fibo):

    a = 0
    b = 1
    square_a = a
    square_b = b

    # defining the color of the pen that draws squares
    x.pencolor("blue")

    # functions to draw squares
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)

    # 'temp' variable equals to the B square(himself + the previous)
    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    # drawing the rest of the squares
    for i in range(1, fibo):

        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)

        # 'temp' variable equals to the B square(himself + the previous)
        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    # down below, the pen goes back to the spiral's starting point (1st square)
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    # defining the color of the pen that draws squares
    x.pencolor("red")
    x.left(90)

    for i in range(fibo):

        print(b)
        calculation = math.pi * b * factor / 2
        calculation /= 90

        for j in range(90):

            x.forward(calculation)
            x.left(1)
        temp = a
        a = b
        b = temp + b


factor = 1  # representing the multiplicative factor of the function


# input for the number of elements in the Fibonacci's Sequence
n = int(input("How many elements will the sequence have? "))

# defining the conditions that satisfy the input
# in case the number of elements is >1, the function that creates the sequence is called
# otherwise, the program informs that input mush be >=1

if n > 0:
    print("Fibonacci's Sequence to", n, "elements:")
    x = turtle.Turtle()
    x.speed(100)
    build_fibonacci(n)
    turtle.done()
else:
    print("The number of elements must be more than 1")

# library that allows us to use shapes through commands
import turtle

# open up the visualization screen
TurtleVisualization = turtle.Screen()

# creating tess object
drawing = turtle.Turtle()


def build_triangle(x, y):
    # draws the pen
    drawing.penup()

    # moves the mouse cursor to an established position
    drawing.goto(x, y)

    # it is used to draw in the pen
    drawing.pendown()

    for i in range(3):

        # moves the pen 100 unities forward from the click
        drawing.forward(100)

        # moves the pen 120 degrees left
        drawing.left(120)

        # moves another 100 unities forward
        drawing.forward(100)


# informs the current cursor position to the function

turtle.onscreenclick(build_triangle, 1)  # number 1 represents left click
turtle.onscreenclick(build_triangle, 3)  # number 2 represents right click


# keeps the screen up and running
turtle.done()

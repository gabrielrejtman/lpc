# library that allows us to use shapes through commands
from turtle import *

# defines the speed of the turtle
speed('fastest')

# rotating the turtle in 90 degrees
rt(-90)

# definition of the angle between the 'Y' base and its branches
angle = 30


# draws an 'Y' shape
def draw_y_shape(sz, level):

    if level > 0:

        colormode(255)

        # changes color mode to rgb and defines the green tone in intervals proportional to the level
        pencolor(0, 255 // level, 0)

        # drawing the base
        fd(sz)

        # another rotation with predetermined angle
        rt(angle)

        # call out to draw the left part
        draw_y_shape(0.8 * sz, level - 1)

        pencolor(0, 255 // level, 0)

        # another direction rotation, this time to the left and with a larger angle
        lt(2 * angle)

        # call out to draw the right part
        draw_y_shape(0.8 * sz, level - 1)

        pencolor(0, 255 // level, 0)

        rt(angle)
        fd(-sz)


# definition of size and level of the tree
draw_y_shape(80, 7)

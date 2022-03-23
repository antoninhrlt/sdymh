# This file is part of "sdymh"
# Under the MIT License
# Copyright (c) 2021 Antonin Hérault

from turtle import clear as tclear
from turtle import *

# Init a window for all functions
shape("turtle")
screensize(1000, 1000)


# Print a square on the turtle window
def square(width, height):
    for i in range(0, 2):
        forward(width)
        right(90)
        forward(height)
        right(90)


# Simple turtle screen clearer
def clear():
    tclear()


# Simple turtle runner
def display():
    mainloop()

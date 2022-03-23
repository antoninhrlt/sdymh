# This file is part of "sdymh"
# Under the MIT License
# Copyright (c) 2021 Antonin Hérault

import math

# Importations to use with directly a class name : "sdymh.ClassName()"
import sdymh.functions
from sdymh.plane_geom import Point
import sdymh.turtle 
from sdymh.vectors import Vector


# Just a simple function to say thank you for this project
# Link to "buy my coffee" in the response
def thank_you():
    print("""
    You have executed : sdymh.thank_you()\n
    You're welcome !!
    If you can, buy my coffee by accessing to this link :
    https://www.buymeacoffee.com/antoninhrlt
    Good luck in your studies, thank to you for using my tool collection :)
    """)


# Pythagore theorem application
# Where "c" is the hypotenuse
#    |\
# a  |  \  c
# or |    \
# b  |x_____\
#     a or b
# "x" it's the "right angle"
def pythagore(a, b):
    return math.sqrt((a ** 2) + (b ** 2)) # return c

# Reciprocal for Pythagore theorem
# Where "c" is the hypotenuse
#    |\
# a  |  \  c
# or |    \
# b  |x_____\
#     a or b
# "x" it's the "right angle"
def reciprocal_pythagore(a, b, c):
    return (a ** 2) + (b ** 2) == (c ** 2)


# Return a list of all numbers of the table `n` from 0 to parameter `to`
def mul_table(n, to=10, printing=True):
    numbers = []
    for i in range(1, to + 1):
        if printing:
            print(f"{n} x {i} = {i * n}")
        else:
            numbers += i * n
    return numbers

# Calculate the IMC of a person with their weight and height
# If your height is "1m80" in real life, please give "1.80" as parameter
def imc(weight: float, height: float):
    return weight / (height**2)


# Check if number `y` is a multiple of `x` 
def is_multiple(x, y):
    if x % y == 0:
        return True
    return False

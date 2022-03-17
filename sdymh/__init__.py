# This file is part of "sdymh"
# Under the MIT License
# Copyright (c) 2021 Antonin Hérault

# Just a simple function to say thank you for this project
# Link to "buy my coffee" in the response
def thank_you():
    print("""
    You have executed : sdymh.thank_you()\n
    You're welcome !!
    If you could, buy my coffee by accessing to this link :
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

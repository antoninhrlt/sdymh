# This file is part of "sdymh"
# Under the MIT License
# Copyright (c) 2021 Antonin Hérault

import sdymh

# Simple class to create a mathemetical vector with a name and its position
# in the plan
# NOTE : Can be called as `sdymh.Vector()`
#
# Example : 
# ```py
# u = Vector("vec u", 5, 3)
#
# # Mathemetical way to write it :
# # u = (
# #   5
# #   3
# # )
# ```
class Vector:
    def __init__(self, name: str, x: int, y: int):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return f"vector {self.name}({self.x}, {self.y})"


# Get the determinant between two vectors
# https://math.stackexchange.com/questions/3141770/what-is-the-determinant-of-two-vectors
def det(vec1: Vector, vec2: Vector, print_properties=False):
    if print_properties:
        if det(vec1, vec2) == 0: 
            print(f"{vec1} and {vec2} are parallels, they are collinears")
        else:
            print(f"{vec1} and {vec2} are not parallels, not collinears")
    
    return vec1.x * vec2.y - vec1.y * vec2.x


# Print a table with the determinants of a list of vectors
# The table uses colors for the vector names, if this raises some display bugs
# in your terminal, you should call this function with parameter `colored` set
# as `False` : `print_table(foo, colored=False)`
# 
# TODO : same but as GUI 
def print_table(vectors, colored=True):
    print("\t\t|", end="")
    for vector in vectors:
        if colored:
            print(f"\t\x1b[31m{vector.name}\x1b[0m\t| ", end="")
        else:
            print(f"\t{vector.name}\t| ", end="")

    print()

    for vector in vectors:
        if colored:
            print(f"\t\x1b[31m{vector.name}\x1b[0m\t| ", end="")
        else:
            print(f"\t{vector.name}\t| ", end="")

        for vector2 in vectors:
            result = det(vector, vector2)
            print(f"\t{result}\t| ", end="")
        
        print()

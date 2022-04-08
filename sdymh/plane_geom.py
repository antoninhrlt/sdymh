# This file is part of "sdymh"
# Under the MIT License
# Copyright (c) 2021 Antonin Hérault

import math

# Simple class for a 2D point in a plan
# NOTE : Can be called as `sdymh.Point()`
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


# Return the coordinates of segment middle thanks to two starting point 
# Formula :
# xm = (xa + xb) / 2
# ym = (ya + yb) / 2
def segment_middle(a: Point, b: Point): 
    middle_x = (a.x + b.x) / 2
    middle_y = (a.y + b.y) / 2

    return Point(middle_x, middle_y)


# Work only in orthonormal reference frame 
# Get the distance between two points
# Formula :
# sqrt((xb - xa)^2 + (yb - ya)^2)
def distance(a: Point, b: Point):
    return math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)


# Perimeter of a triangle of size (l x L)
def perimeter(l, L):
    return (l + L) * 2

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE

    matches = 0
    sides = (a, b, c)
    i1 = 0
    while i1 < len(sides):
      i2 = 0
      while i2 < len(sides):
        if ((sides[i1] <= 0) or (sides[i2] <= 0)):
          raise TriangleError()
        if i1 != i2:
          total_lengths = 0
          for length in sides:
            total_lengths += length
          other = total_lengths - sides[i1] - sides[i2]
          if other >= (sides[i1] + sides[i2]):
            raise TriangleError()
          if sides[i1] == sides[i2]:
            matches += 1
        i2 += 1
      i1 += 1

    if matches >= 3:
      return 'equilateral'
    elif matches == 2:
      return 'isosceles'
    else:
      return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass

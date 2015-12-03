"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import sys
from math import sqrt

# Trivial upper bound of 500 on a and b
UPPER = 500
for a in range(3, UPPER):
  for b in range(a+1, UPPER):
    c = sqrt(a*a + b*b)
    if c.is_integer():
      # found a valid Pythagorean triple
      if (a+b+c)==1000:
        print int(a*b*c)
        sys.exit()

"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

def sum_of_squares(n):
  return sum(i*i for i in range(1,n+1))

def square_of_sum(n):
  s = n*(n+1)/2
  return s*s

N = 100
print square_of_sum(N) - sum_of_squares(N)

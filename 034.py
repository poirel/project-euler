"""
Project Euler Problem 34
========================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial

result = 0
for i in range(10, 100000):
  fact_sum = sum(factorial(int(d)) for d in str(i))
  if i==fact_sum:
    result += i
print result
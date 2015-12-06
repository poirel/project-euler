"""
Project Euler Problem 23
========================

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is called
abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""

from utils import proper_factors

UPPER = 28123

abundant = []
for i in range(2, UPPER+1):
  if sum(proper_factors(i))>i:
    abundant.append(i)


# get all number that CAN be written as the sum of two abundant numbers
pair_abundant = set()
for i, a in enumerate(abundant[:UPPER]):
  for b in abundant[:i+1]:
    if a+b<=UPPER:
      pair_abundant.add(a+b)

# the sum of all numbers that CANNOT be written as the sum of two abundant numbers
# is just th sum of all numbers [1, UPPER] minus the sum of the abundant pairs
print UPPER*(UPPER+1)/2 - sum(pair_abundant)

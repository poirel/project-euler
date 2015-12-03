"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

from collections import Counter
from utils import prime_factors

UPPER = 20

all_factors = Counter()
for i in range(1,UPPER+1):
  for prime, count in Counter(prime_factors(i)).items():
    if count>all_factors[prime]:
      all_factors[prime] = count

product = 1
for prime, count in all_factors.items():
  product = product*(prime**count)

print product

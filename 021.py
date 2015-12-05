"""
Project Euler Problem 21
========================

Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from utils import proper_factors
from collections import defaultdict

UPPER = 10000

d = {}
inv_d = defaultdict(set)
for i in range(1, UPPER):
  d[i] = sum(proper_factors(i))
  inv_d[d[i]].add(i)
  # need to keep track of amicable siblings that may lie above the upper bound
  if d[i] > UPPER:
    d[d[i]] = sum(proper_factors(d[i]))
    inv_d[d[d[i]]].add(d[d[i]])

amicable = set()
for a in range(1, UPPER):
  for b in inv_d[a]:
    if a!=b and d[a]==b and d[b]==a:
      amicable.add(a)
      if b<UPPER:
        amicable.add(b)

print sum(amicable)
"""
Project Euler Problem 33
========================

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""

from utils import prime_factors
from collections import Counter

def is_curious(n1, n2, d1, d2):
  n = 10*n1 + n2
  d = 10*d1 + d2
  if n>=d:
    return False
  
  ratio = float(n)/d
  if n1==d1 and float(n2)/d2==ratio:
    return True
  if n1==d2 and float(n2)/d1==ratio:
    return True
  if n2==d1 and float(n1)/d2==ratio:
    return True
  if n2==d2 and float(n1)/d1==ratio:
    return True
  return False

curious = list()
for n in range(11, 100):
  if n%10==0:
    continue
  n1, n2 = [int(x) for x in str(n)]

    # let n1=d1
  for d2 in range(1,10):
    if is_curious(n1, n2, n1, d2):
      d = (10*n1+d2)
      curious.append((n,d))

  # let n1=d2
  for d1 in range(1,10):
    if is_curious(n1, n2, d1, n1):
      d = (10*d1+n1)
      curious.append((n,d))

  # let n2=d1
  for d2 in range(1,10):
    if is_curious(n1, n2, n2, d2):
      d = (10*n2+d2)
      curious.append((n, d))

  # let n2=d2
  for d1 in range(1,10):
    if is_curious(n1, n2, d1, n2):
      d = (10*d1+n2)
      curious.append((n,d))

# get the prime factors of the numerator and denominator
n_factors = Counter()
d_factors = Counter()
for n,d in curious:
  n_factors.update(prime_factors(n))
  d_factors.update(prime_factors(d))

# get the reduced form of n/d
for f in n_factors.keys():
  common = min(n_factors[f], d_factors[f])
  n_factors[f] -= common
  d_factors[f] -= common

result = 1
for f, count in d_factors.items():
  result *= f**count
print result
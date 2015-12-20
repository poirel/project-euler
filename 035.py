"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from utils import gen_primes


primes = gen_primes(1000000)
# Trivial filter any any even digits, which will always result in a non-prime rotation
even = set(str(24680))
primes = [2] + [p for p in primes if len(even.intersection(set(str(p))))==0]

def rotations(s):
  result = []
  for i in range(len(s)):
    result.append(s[i:] + s[:i])
  return set(result)

def is_circular(n):
  rots = [int(x) for x in rotations(str(n))]
  for x in rots:
    if x not in primes:
      return False
  return True

circular = []
for p in primes:
  if is_circular(p):
    circular.append(p)
print len(circular)

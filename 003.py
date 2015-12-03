"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from math import sqrt, floor
from utils import gen_primes

N = 600851475143

max_prime = N
candidates = gen_primes(sqrt(N))
candidates.reverse()
for p in candidates:
  if N%p==0:
    max_prime = p
    break

print max_prime

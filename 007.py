"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

from utils import gen_primes

# Listing primes less than 200,000 yields more than enough.
print gen_primes(200000)[10000]

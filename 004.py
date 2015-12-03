"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from utils import is_palindrome

UPPER_BOUND = 1000

max_palindrome = 1
for a in range(2, UPPER_BOUND):
  for b in range(2, UPPER_BOUND):
    prod = a*b
    if prod>max_palindrome and is_palindrome(str(prod)):
      max_palindrome = prod

print max_palindrome


"""
Project Euler Problem 36
========================

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

from utils import str_reverse, is_palindrome

result = 0

# single-digit palindromes
for i in range(10):
  if is_palindrome(bin(i)[2:]):
    result += i
# ... and beyond
for i in range(1,1000):
  s = str(i)
  rev_s = str_reverse(s)

  num = int(s + str_reverse(s))
  if num<1000000 and is_palindrome(bin(num)[2:]):
    result += num
  for d in range(10):
    num = int(s + str(d) + rev_s)
    if num<1000000 and is_palindrome(bin(num)[2:]):
      result += num

print result
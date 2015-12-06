"""
Project Euler Problem 26
========================

A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

   1/2  =  0.5
   1/3  =  0.(3)
   1/4  =  0.25
   1/5  =  0.2
   1/6  =  0.1(6)
   1/7  =  0.(142857)
   1/8  =  0.125
   1/9  =  0.(1)
  1/10  =  0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
be seen that ^1/[7] has a 6-digit recurring cycle.

Find the value of d < 1000 for which ^1/[d] contains the longest recurring
cycle in its decimal fraction part.
"""

def recurring_mantissa_cycle(n):
  # list of (mantissa_digit, remainder)
  mantissa = [(10/n, 10%n)]
  while True:
    next_pair = (mantissa[-1][1]*10/n, (mantissa[-1][1]*10)%n)
    if next_pair in mantissa:
      return [d for d,r in mantissa[mantissa.index(next_pair):]]
    mantissa.append(next_pair)
  print mantissa

idx_longest = None
longest = []
for i in range(2,1001):
  cycle = recurring_mantissa_cycle(i)
  if len(cycle) > len(longest):
    longest = cycle
    idx_longest = i

print idx_longest
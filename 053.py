"""
Project Euler Problem 53
========================

There are exactly ten ways of selecting three from five, 12345:

           123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, nCr(5,3) = 10.

In general,

nCr(n,r) = n!/(r!(n-r)!), where r =< n, n! = n * (n1) * ... * 3 * 2 * 1,
and 0! = 1.

It is not until n = 23, that a value exceeds one-million: nCr(23,10) =
1144066.

How many values of nCr(n,r), for 1 =< n =< 100, are greater than one-million?
"""

from math import factorial, ceil

def choose(n, r):
  return factorial(n)/(factorial(r)*factorial(n-r))


total = 0
for n in range(2,101):
  n_count = 0
  for r in range(int(ceil(n/2.0)), n+1):
    if choose(n,r)>1000000:
      n_count += 1
    else:
      break

  if n_count==0:
    pass
  elif n%2==0: # even
    n_count = n_count*2-1
  else: #odd
    n_count = n_count*2
  total += n_count
print total
"""
Project Euler Problem 37
========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from utils import gen_primes
from collections import defaultdict


primes = gen_primes(1000000)
even = set(str(24680))

primes_by_length = defaultdict(list)
trunc_by_length = defaultdict(list)
for p in primes:
  primes_by_length[len(str(p))].append(p)

  # truncatable prime can never contain 1,4,6,8,9
  if str(p)[0] in (1,4,6,8,9):
    continue

  if len(str(p))==1:
    trunc_by_length[1].append(p)
  else:
    len_p = len(str(p))
    if int(str(p)[1:]) in trunc_by_length[len_p-1]:
      trunc_by_length[len_p].append(p)


def is_trunc_from_right(p):
  if len(str(p))<=1:
    return False

  for i in range(1, len(str(p))+1):
    prefix = int(str(p)[:i])
    if prefix not in primes_by_length[i]:
      return False
  return True


truncs = []
for length, ts in trunc_by_length.items():
  for p in ts:
    if is_trunc_from_right(p):
      truncs.append(p)

print sum(truncs)
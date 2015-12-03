"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def sequence_generator(n):
  current = n
  while current!=1:
    yield current
    if current%2==0:
      current /= 2
    else:
      current = 3*current + 1
  yield 1


cached_lengths = {1:1}

max_chain_num = None
max_chain_length = 0
for i in range(2, 1000000):
  seq_i = sequence_generator(i)
  next_val = next(seq_i)
  length = 0
  while next_val not in cached_lengths:
    length += 1
    next_val = next(seq_i)

  length += cached_lengths[next_val]
  cached_lengths[i] = length

  if length>max_chain_length:
    max_chain_num = i
    max_chain_length = length

print max_chain_num
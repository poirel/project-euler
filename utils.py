from math import sqrt, ceil, floor

def gen_primes(n):
  """
  Returns a list of all primes in the inclusive range [1,n].
  """
  n_normalized = int(floor(n))
  primes = []
  for i in range(2,n_normalized+1):
    is_prime = True
    root = sqrt(i)
    for p in primes:
      if p>root: break
      if i%p==0:
        is_prime = False
        break
    if is_prime: primes.append(i)
  return primes

def prime_factors(n):
  """
  Returns a list of all prime factors of n.
  """
  n_normalized = int(floor(n))
  factors = []
  current = n_normalized
  for p in gen_primes(n):
    while current%p==0:
      factors.append(p)
      current = current/p
  if len(factors)==0:  factors = [n_normalized]
  return factors

def fib(n):
  """
  Returns list of numbers in the Fibonacci sequence in the inclusive range [1, n].
  """
  seq = [1, 2]
  while seq[-1]<n:
    seq.append(seq[-2]+seq[-1])
  return seq

def str_reverse(s):
  """
  Reverse the given string.
  """
  l = list(s)
  l.reverse()
  return ''.join(l)

def is_palindrome(s):
  """
  Return True if the given string is a palindrome; False, otherwise.
  """
  return s==str_reverse(s)

def product(numbers):
  return reduce(lambda x,y: x*y, numbers, 1)

def transpose(matrix):
  return zip(*matrix)

def vertical_flip(matrix):
  return matrix[::-1]

def horizontal_flip(matrix):
  return [row[::-1] for row in matrix]

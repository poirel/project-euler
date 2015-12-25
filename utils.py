from math import sqrt, floor


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

DAYS = ['mon', 'tues', 'wed', 'thu','fri','sat', 'sun']
MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

def days_in_month(month, year):
  num_days = {
    'jan': 31,
    'feb': 28 if (year%100!=0 or year%400==0) else 29,
    'mar': 31,
    'apr': 30,
    'may': 31,
    'jun': 30,
    'jul': 31,
    'aug': 31,
    'sep': 30,
    'oct': 31,
    'nov': 30,
    'dec': 31
  }
  return num_days[month.lower()[:3]]

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

def factors(n):
  f = set()
  for i in range(1, int(sqrt(n))+1):
    if n%i==0:
      f.update([i, n/i])
  f = list(f)
  f.sort()
  return f

def proper_factors(n):
  return factors(n)[:-1]

def fib(n):
  """
  Returns list of numbers in the Fibonacci sequence in the inclusive range [1, n].
  """
  seq = [1, 2]
  while seq[-1]<n:
    seq.append(seq[-2]+seq[-1])
  return seq

def fib_generator():
  """
  A generator for the Fibonnaci sequence
  """
  a, b = 1, 2
  while True:
    yield a
    a, b = b, a+b

def triangle_number_generator():
  curr_sum = 1
  curr_num = 1
  while True:
    yield curr_sum
    curr_num += 1
    curr_sum += curr_num

def str_reverse(s):
  """
  Reverse the given string.
  """
  l = list(s)
  l.reverse()
  return ''.join(l)

def num_reverse(n):
  return int(str_reverse(str(n)))

def is_palindrome(s):
  """
  Return True if the given string is a palindrome; False, otherwise.
  """
  return str(s)==str_reverse(str(s))

def product(numbers):
  return reduce(lambda x,y: x*y, numbers, 1)

def transpose(matrix):
  return zip(*matrix)

def vertical_flip(matrix):
  return matrix[::-1]

def horizontal_flip(matrix):
  return [row[::-1] for row in matrix]

def permutations(s):
  if len(s) <= 1:
    yield s
  else:
    for i in range(len(s)):
      for p in permutations(s[:i] + s[i+1:]):
        yield s[i] + p
"""
Project Euler Problem 42
========================

The n-th term of the sequence of triangle numbers is given by, t[n] =
1/2n(n+1); so the first ten triangle numbers are:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""

from utils import triangle_number_generator, ALPHABET

tri = triangle_number_generator()

tri_numbers = [tri.next()]
while tri_numbers[-1]<1000:
  tri_numbers.append(tri.next())

with open('resources/words.txt') as infile:
  words = infile.readline().replace('"', '').strip().lower().split(',')

tri_count = 0
for w in words:
  val = sum(ALPHABET.find(x)+1 for x in w)
  if val in tri_numbers:
    tri_count += 1

print tri_count

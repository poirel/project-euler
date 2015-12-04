"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

def wordify_under_10(n):
  words = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
  }
  return words[n]

def wordify_under_20(n):
  words = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
  }
  if n<10:
    return wordify_under_10(n)
  else:
    return words[n]

def wordify_under_100(n):
  words = {
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
  }
  if n<20:
    return wordify_under_20(n)
  else:
    return words[int(str(n)[-2])*10] + wordify_under_10(n%10)

def wordify_under_1000(n):
  hundreds_str = ''
  if n>=100:
    hundreds_str = wordify_under_10(int(str(n)[-3])) + "hundred"
  under_hundred_str = wordify_under_100(n%100)

  if len(hundreds_str)>0 and len(under_hundred_str)>0:
    return hundreds_str + 'and' + under_hundred_str
  else:
    return hundreds_str + under_hundred_str

num_words = [len(wordify_under_1000(i)) for i in range(1, 1000)]

print sum(num_words) + len('onethousand')



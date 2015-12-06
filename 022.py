"""
Project Euler Problem 22
========================

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""
from utils import ALPHABET

with open('./resources/names.txt') as infile:
  names = [n.strip('"') for n in infile.read().replace('\n', '').strip().split(',')]
names.sort()

def alphabetical_value(name):
  return sum(ALPHABET.index(x)+1 for x in name.lower())

total = 0
for i,name in enumerate(names, 1):
  total += alphabetical_value(name)*i
print total
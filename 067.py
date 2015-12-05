"""
Project Euler Problem 67
========================

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                    3
                                   7 4
                                  2 4 6
                                 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not
possible to try every route to solve this problem, as there are 2^99
altogether! If you could check one trillion (10^12) routes every second it
would take over twenty billion years to check them all. There is an
efficient algorithm to solve it. ;o)
"""

# this solution copied from original solution in 018.py

with open('./resources/triangle.txt') as infile:
  rows = [[int(x) for x in line.strip().split()] for line in infile]

max_paths = [rows[0]]
for i, r in enumerate(rows[1:], 1):
  max_paths.append([r[0] + max_paths[i-1][0]] +
                   [r[j] + max(max_paths[i-1][j-1], max_paths[i-1][j]) for j in range(1, len(r)-1)] +
                   [r[-1] + max_paths[i-1][-1]])
print max(max_paths[-1])


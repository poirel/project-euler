"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""

GRID = 20

dim = GRID+1

# initialize DP solution
result = [[0 for _ in range(dim)] for _ in range(dim)]
for x in range(dim):
  result[x][dim-1] = 1
  result[dim-1][x] = 1

# fill DP grig from bottom-right to top-left of matrix
for i in range(dim-2, -1, -1):
  for j in range(dim-2, -1, -1):
    result[i][j] = result[i][j+1] + result[i+1][j]

print result[0][0]
"""
Project Euler Problem 19
========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""

from utils import MONTHS
from utils import  days_in_month

total_days = 1 # the first day, Jan 1, 1900 is a monday.
lonely_mondays = 0
for y in range(1900, 2001):
  for m in MONTHS:
    total_days += days_in_month(m, y)
    if y>1900 and total_days%7==1:
        lonely_mondays += 1

print lonely_mondays
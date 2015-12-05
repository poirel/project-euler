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

total_days = 1 # the first day, Jan 1, 1900 is a monday.
lonely_mondays = 0
for y in range(1900, 2001):
  for m in MONTHS:
    total_days += days_in_month(m, y)
    if y>1900 and total_days%7==1:
        lonely_mondays += 1

print lonely_mondays
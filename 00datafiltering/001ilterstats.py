#!/usr/bin/python

# Run this first.
for l in open('statistics.txt'):
    x = l.split()
    if int(x[6]) > 500:
        continue

    if int(x[4]) > 0:
        continue

    if float(x[7]) < 0.01:
        continue

    print l.strip()

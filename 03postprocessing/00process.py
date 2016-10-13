#!/usr/bin/env python

import sys, subprocess, os
from numpy import mean, std

seen = set()
count = 0
l1 = sys.argv[1]

sys.stderr.write('.')
sys.stderr.flush()
mapping = {}
try:
    f = open(l1 + '/maela.mapping')
    for ll in f:
        x = ll.split()
        a = x[0]
        b = x[1]
        mapping[str(int(a)+1)] = int(b)
except:
    sys.exit(0)

sys.stderr.write('\n' + l1 + '\n')
sys.stderr.flush()
l = l1 + '/maela.plmdca'
scores = []
sumv = 0.
lenv = 0.
try:
    for ll in open(l):
        x = ll.split(',')
        try:
            a = mapping[x[0]] - mapping[x[1]] 
        except:
            continue
        sumv += float(x[2])
        lenv += 1
        if mapping[x[1]] -  mapping[x[0]] < 10000:
            continue
        scores.append( (float(x[2]), mapping[x[0]], mapping[x[1]]) ) 
except:
    sys.stderr.write('plmDCA file missing!')
    sys.stderr.flush()
    continue
sys.stderr.flush()

f = open(l1 + '/plmdca.data', 'w')
f.write('Seen:')
for i in sorted(mapping.values()):
    f.write(' {:d}'.format(i))
s = 0.

f.write('\nMean: {:6.6f}\n'.format(sumv/lenv))
scores.sort(reverse=True)
for s in scores[:3000]:
    f.write('{:d} {:d} {:7.6}\n'.format(s[1], s[2], s[0]))
f.close()

# Uncomment line below for compressing the resultant files
# subprocess.call('xz -9 ' + l1 + '/maela*', shell=True)

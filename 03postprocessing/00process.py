#!/usr/bin/env python

import sys, subprocess, os
from numpy import mean, std

# Sequence separation threshold below which couplings are not reported
excludeThreshold = 10000

# If you want to enable compression of predictions (highly recommended to save disk space), change below to True
compressResults = False

def processdirectory(l1):
    mapping = {}
    try:
        f = open(l1 + '/input.mapping')
        for ll in f:
            x = ll.split()
            a = x[0]
            b = x[1]
            mapping[str(int(a)+1)] = int(b)
    except:
        return 1

    l = l1 + '/input.genomedca'
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
            if mapping[x[1]] -  mapping[x[0]] < excludeThreshold:
                continue
            scores.append( (float(x[2]), mapping[x[0]], mapping[x[1]]) ) 
    except:
        return 2

    f = open(l1 + '/genomedca.data', 'w')
    f.write('Seen:')
    for i in sorted(mapping.values()):
        f.write(' {:d}'.format(i))
    s = 0.

    f.write('\nMean: {:6.6f}\n'.format(sumv/lenv))
    scores.sort(reverse=True)
    for s in scores[:3000]:
        f.write('{:d} {:d} {:7.6}\n'.format(s[1], s[2], s[0]))
    f.close()
    if compressResults:
        subprocess.call('xz -9 ' + l1 + '/input*', shell=True)
    return 0

if __name__ == "__main__":
    try:
        for indir in sys.argv[1:]:
            p = processdirectory(indir)
            if p == 0:
                sys.stderr.write('+ {:s} processed\n'.format(indir))
            elif p == 1:
                sys.stderr.write('- {:s} misses the mappings (step 01sampling)\n'.format(indir))
            elif p == 2:
                sys.stderr.write('- {:s} misses the couplings (step 02inference)\n'.format(indir))
            else:
                sys.stderr.write('? {:s} returns unknown errors. Emergency Temporal Shift!\n'.format(indir))
        if len(sys.argv) == 1:
            raise
    except Exception as e:
        sys.stderr.write('Syntax: {:s} resultDirectory [resultDirectory2...]\n'.format(sys.argv[0]))
        sys.stderr.write('Each of result directories should containt input.mapping and input.genomedca files.\n')
        sys.exit(2)

#!/usr/bin/env python

import os, sys, random
from numpy import mean, std

def makesummaries(directories, outfile):
    scores = {}
    seen = {} 
    means = []
    count = 0
    files = 0
    for l1 in directories:
        if not os.path.exists(l1 + '/genomedca.data'):
            continue
        count += 1
        sys.stderr.write(l1 + ' {0:d}\n'.format(count))
        l = l1 + '/genomedca.data'
        try:
            inf = open(l).readlines()
            meanv = float(inf[1].split()[1])
            means.append(meanv)
            seenlist = inf[0].split()[1:]
        except:
            continue
        v = len(seenlist)*(len(seenlist)-1) * 0.5
        for i in seenlist:
            try:
                seen[i].add(l1)
            except:
                seen[i] = set()
                seen[i].add(l1)
        files += 1
        for ll in inf[2:]:
            x = ll.split()
            try:
                scores[(x[0], x[1])].append( float(x[2]) ) 
                
            except:
                scores[(x[0], x[1])] = []
                scores[(x[0], x[1])].append( float(x[2]) ) 
        sys.stderr.flush()

    meanmean = mean(means)
    meanstd = std(means)
    mcount = len(scores.keys())
    count = 0.
    f = open(outfile, 'w')
    for sites in sorted(scores.keys()):
        count += 1
        if len(scores[sites]) < 1:
            continue
        if count % 500 == 0:
            sys.stderr.write('{0:7.0f} {1:5.3f}%\n'.format(count, 100*count/mcount))
            sys.stderr.flush()
            f.flush()
        f.write('{0:7s} {1:7s} '.format(sites[0], sites[1]))
        qscores = scores[sites]
        combinations = len(seen[sites[0]] & seen[sites[1]])
        f.write('{0:8.5f} {1:8.5f} {2:8.5f} {3:8.5f} {4:d} {5:d}\n'.format(mean(qscores), std(qscores), min(qscores), max(qscores), len(scores[sites]), combinations))
    f.close()

if __name__ == "__main__":
    try:
        indirs = sys.argv[2:]
        outfile = sys.argv[1]
    except:
        sys.stderr.write('Syntax: {:s} outputFile dataDirectories\n'.format(sys.argv[0]))
        sys.exit(2)
    makesummaries(indirs, outfile)

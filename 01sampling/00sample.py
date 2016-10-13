#!/usr/bin/env python

import sys, os
import numpy as np
import random
import joblib


accepted = []

# Uses processed.dat from previous step (not included here)

print 'Read data for sampling'
#data = joblib.load('processed.dat')
data = joblib.load('/hd0/skwarkmj/maela/processed.dat')

accepted = sorted(data[data.keys()[0]].keys())

step = 1500

chunks = []
start = 0
chunk = []

# Produce the bins from which to sample
for i in accepted:
    if i > start + step:
        start += step
        if len(chunk) > 0:
            chunks.append(chunk)
            print start, len(chunk), min(chunk), max(chunk)
    chunk.append(i)
    
for xxv in range(5000):
    accepted2 = []

    # Pick the entries from the bins
    for i in range(0, len(chunks)):
        accepted2.append(random.choice(chunks[i]))

    # Save the alignment of sampled bins and mapping of positions to
    # original loci
    i = 0
    while os.path.exists('sampled/samplingU{0:04d}'.format(i)):
        i+=1
    os.makedirs('sampled/samplingU{0:04d}'.format(i))

    f = open('sampled/samplingU{0:04d}/maela.seq'.format(i), 'w')
    print i, len(accepted2)
    for sequence in data.keys():
        S = data[sequence]
        f.write('>{:s}\n'.format(sequence))
        for ii in accepted2:
            f.write(data[sequence][ii])
        f.write('\n')
    f.close()

    s = 0
    f = open('sampled/samplingU{:04d}/maela.mapping'.format(i), 'w')
    for i in accepted2:
        f.write('{0:d} {1:d}\n'.format(s, i))
        s+=1
    f.close()

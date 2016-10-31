#!/usr/bin/env python

import sys, os
import numpy as np
import random
import joblib

## Adjustable parameters
stepSize = 1500
samples = 5000

def generateSamples(datafile, stepSize=1500, samples=5000):
    accepted = []
    print 'Read data for sampling'
    data = joblib.load(datafile)

    accepted = sorted(data[data.keys()[0]].keys())
    chunks = []
    start = 0
    chunk = []

    # Produce the bins from which to sample
    for i in accepted:
        if i > start + stepSize:
            start += stepSize
            if len(chunk) > 0:
                chunks.append(chunk)
        chunk.append(i)
        
    for xxv in range(samples):
        accepted2 = []

        # Pick the entries from the bins
        for i in range(0, len(chunks)):
            accepted2.append(random.choice(chunks[i]))

        # Save the alignment of sampled bins and mapping of positions to
        # original loci
        i = 0
        while os.path.exists('sampled/sampling{0:04d}'.format(i)):
            i+=1
        os.makedirs('sampled/sampling{0:04d}'.format(i))

        f = open('sampled/sampling{0:04d}/input.seq'.format(i), 'w')
        print i, len(accepted2)
        for sequence in data.keys():
            S = data[sequence]
            f.write('>{:s}\n'.format(sequence))
            for ii in accepted2:
                f.write(data[sequence][ii])
            f.write('\n')
        f.close()

        s = 0
        f = open('sampled/sampling{0:04d}/input.mapping'.format(i), 'w')
        for i in accepted2:
            f.write('{0:d} {1:d}\n'.format(s, i))
            s+=1
        f.close()


if __name__ == "__main__":
    try:
        infile = sys.argv[1]
        if not os.path.exists(infile):
            sys.stderr.write('The input file ({:s}) does not exist!\n'.format(infile))
            sys.exit(2)
        if len(sys.argv) == 2:
            generateSamples(infile)
        elif len(sys.argv) == 4:
            generateSamples(infile, stepSize=float(sys.argv[2]), samples=int(sys.argv[3]))
        else:
            raise 
    except Exception as e:
        sys.stderr.write('Syntax: {:s} inputFile\n'.format(sys.argv[0]))
        sys.stderr.write('        {:s} inputFile stepSize samplesNumer\n'.format(sys.argv[0]))
        sys.stderr.write(' If step size and number of samples are not provided, they will be given default values of 1,500 bp and 5000 samples.\n'.format(sys.argv[0]))
        sys.exit(2)

#!/usr/bin/env python2.7

import sys, os, joblib

# Modify these two to suit your preferences
minimalMAF = 0.01
gapFraction = 0.15
### 

def parsefile(infile):
    frequencies = {}
    length = -1
    seq = ''
    for l in open(infile):
        l = l.upper()
        if l.find('>') == 0:
            sys.stderr.write(l)
            if len(seq) < 1:
                continue
            if len(seq) != length and length > 0:
                sys.stderr.write('Length mismatch {:d} =/= {:d}\n'.format(len(seq), length))
                sys.exit(1)
            for i in range(len(seq)):
                if length < 0:
                    frequencies[i] = {} 
                try:
                    frequencies[i][seq[i]] += 1
                except:
                    frequencies[i][seq[i]] = 1
            length = len(seq)
            seq = ''
        else:
            seq += l.strip()

    lookup = {}
    for i in range(length):
        data = frequencies[i].items()
        data = sorted(data, key=lambda x: -x[1])
        q = []
        others = 0
        for d in data:
            if d[0] == '-' or d[0] == 'N':
                continue
            if len(q) < 6:
                q.append(d[1])
            else:
                others += d[1]
        gaps = 0
        for c in ['-', 'N']:
            try:
                gaps += frequencies[i][c]
            except:
                pass
        q.append(gaps)
        sequences = sum(q)
        maf = float(q[1])/float(q[1] + q[0])
        if maf < minimalMAF:
            # Skip the position, as it has to low minor allelle frequency
            continue
        if gaps > gapFraction * sequences:
            # Skip the position, due to too many gaps
            continue 
        if float(q[2]) > 0:
            # Skip the position, as it is not biallellic
            continue
        lookup[i] = {}
        lookup[i][data[0][0]] = 'E'
        lookup[i][data[1][0]] = 'F'
        lookup[i]['n'] = '-'
    
    data = {}
    count = 0
    seq = ''
    key = ''
    for l in open(infile):
        l = l.upper()
        if l.find('>') == 0:
            sys.stderr.write(l)
            if len(seq) < 1:
                key = l
                continue
            if len(seq) != length and length > 0:
                sys.stderr.write('Length mismatch {:d} =/= {:d}\n'.format(len(seq), length))
                sys.exit(1)
            data[key] = {}
            for i in lookup.keys():
                try:
                    data[key][i] = lookup[i][seq[i]]
                except:
                    print lookup[i], seq[i] 
                    sys.stderr.write('ERROR: For sequence {:s} processing failed at position {:d}\n'.format(key, i))
                    sys.exit(4)
            length = len(seq)
            seq = ''
            key = l
        else:
            seq += l.strip()
    return data
 

if __name__ == "__main__":
    try:
        infile = sys.argv[1]
        outfile = sys.argv[2]
    except:
        sys.stderr.write('Syntax: {:s} inputFile outputFile\n'.format(sys.argv[0]))
        sys.exit(2)
    if not os.path.exists(infile):
        sys.stderr.write('Input file {:s} does not exist.\n'.format(sys.argv[1]))
        sys.exit(3)
    o = parsefile(infile)
    joblib.dump(o, outfile)

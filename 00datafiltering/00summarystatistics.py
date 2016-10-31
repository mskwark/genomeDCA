#!/usr/bin/env python2.7

import sys, os

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
    output = []
    for i in range(length):
        data = frequencies[i].items()
        data = sorted(data, key=lambda x: -x[1])
        q = []
        q.append(i+1)
        others = 0
        for d in data:
            if d[0] == '-' or d[0] == 'N':
                continue
            if len(q) < 6:
                q.append(d[1])
            else:
                others += d[1]
        while len(q) != 5:
            q.append(0)
        q.append(others)
        gaps = 0
        for c in ['-', 'N']:
            try:
                gaps += frequencies[i][c]
            except:
                pass
        q.append(gaps)
        output.append(q)
    return output
    

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
    f = open(outfile, 'w')
    for i in o:
        f.write('{:7d}'.format(i[0]))
        for q in i[1:]:
            f.write(' {:5d}'.format(q))
        f.write(' {:6.4f}\n'.format(float(i[2])/(i[1]+i[2])))
    f.close()

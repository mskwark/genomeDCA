#!/usr/bin/python

import sys, os, joblib

chosen = set()
for l in open('statistics-filtered.txt'):
    x = l.split()
    chosen.add(int(x[0]))

sampleseq = open('maela.head').readlines()[1].strip()
lensampleseq = len(sampleseq)
counts = {}
for i in range(lensampleseq):
    counts[i] = {}
    for l in 'gtacun':
        counts[i][l] = 0

count = 0
for l in open('maela3K.fasta'):
    l = l.strip().lower()
    if l.find('>') == 0:
        count += 1
        sys.stderr.write(l + ' {:d}\n'.format(count))
        sys.stderr.flush()
        continue
    if len(l) != lensampleseq:
        sys.stderr.write('{:d} =/= {:d}\n'.format(len(l), lensampleseq))
        sys.stderr.flush()
        continue
    for i in chosen:
        counts[i][l[i]] += 1

print len(chosen)

mapping = {}
for cc in counts.keys():
    c = counts[cc]
    r = []
    for d in c.keys():
        if d != 'n':
            r.append((c[d], d))
    r.sort(reverse=True)
    if r[2][0] > 0:
        chosen.discard(cc)
        #print cc, r
        continue
    mapping[cc] = {}
    mapping[cc][r[0][1]] = 'E'
    mapping[cc][r[1][1]] = 'F'
    mapping[cc]['n'] = '-'

data = {}
count = 0
for l in open('maela3K.fasta'):
    l = l.strip().lower()
    if l.find('>') == 0:
        count += 1
        sys.stderr.write(l + ' {:d}\n'.format(count))
        key = l
        sys.stderr.flush()
        continue
    if len(l) != lensampleseq:
        sys.stderr.write('{:d} =/= {:d}\n'.format(len(l), lensampleseq))
        sys.stderr.flush()
        continue
    data[key] = {}
    for i in chosen:
        try:
            data[key][i] = mapping[i][l[i]]
        except:
            print i, l[i], mapping[i]
            sys.exit(0)

joblib.dump(data, 'processed.dat')


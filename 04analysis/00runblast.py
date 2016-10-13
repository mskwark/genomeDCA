#!/usr/bin/python

sequence = open('genome.fa').readlines()[1]

import subprocess, os
top = len(sequence)
chosen = set()
for l in open(f).readlines()[:1000]:
        x = l.split()
        chosen.add(int(x[0]))
        chosen.add(int(x[1]))

for c in chosen:
    f = open('sequences/sequence{:07d}.fa'.format(c), 'w')
    f.write('>position {:d}'.format(c) + '\n')
    f.write( sequence[max(0, c-500):min(top, c+501)]  + '\n')
    f.close()
    if not os.path.exists('sequences/sequence{:07d}.fa.blast'.format(c)):
        print 'Doing blast for', c
        subprocess.call('/home/mjs/sw/blast-2.2.26/bin/blastall -p blastx -i sequences/sequence{:07d}.fa -d pneumococcus.reference > sequences/sequence{:07d}.fa.blast'.format(c,c), shell=True)

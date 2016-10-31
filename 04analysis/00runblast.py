#!/usr/bin/env python2.7

# This script will very likely not work in a general case and requires a bit of preparation (see README.md).

import subprocess, os, sys

try:
    sequence = open('genome.fa').readlines()[1]
except:
    sys.stderr.write('Genome sequence does not exist!\n')
    sys.exit(0)

if len(sys.argv) != 2:
    sys.stderr.write('{:s} summaryOutfile.txt\nThis script takes the output of coupling inference and attempts to map it to the proteins in the target organism.\nRequires: genome.fa (sequence of genome in question) and BLAST formatted database of protein sequences in this organism (reference.fa).'.format(sys.argv[0]))

blastall = 'n/a'
try:
    if not os.path.exists(blastall):
        blastall = subprocess.check_output(['which', 'blastall'])
except:
    sys.stderr.write('BLAST executable not found')

top = len(sequence)
chosen = set()
for l in open(sys.argv[1]).readlines()[:1000]:
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
        subprocess.call('{:s} -p blastx -i sequences/sequence{:07d}.fa -d reference.fa > sequences/sequence{:07d}.fa.blast'.format(blastall, c,c), shell=True)

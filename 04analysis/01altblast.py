#!/usr/bin/env python2.7

import os,sys
import subprocess

blastall = 'n/a'
try:
    if not os.path.exists(blastall):
        blastall = subprocess.check_output(['which', 'blastall'])
except:
    sys.stderr.write('BLAST executable not found')

sequence = open('genome.fa').readlines()[1]

top = len(sequence) + 1
for c in range(0, len(sequence), 300):
    f = open('mapping/sequence{:07d}.fa'.format(c), 'w')
    f.write('>position {:d}'.format(c) + '\n')
    f.write( sequence[max(0, c-300):min(top, c+301)]  + '\n')
    f.close()
    if not os.path.exists('mapping/sequence{:07d}.fa.blast'.format(c)):
        print 'Doing blast for', c
        subprocess.call('{:s} -p blastx -i mapping/sequence{:07d}.fa -d pneumococcus-reference.fasta > mapping/sequence{:07d}.fa.blast'.format(blastall, c,c), shell=True)

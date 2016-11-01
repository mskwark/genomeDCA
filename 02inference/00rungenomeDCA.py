#!/usr/bin/env python

import sys, subprocess, os
import string as s

# Change 4 to the desired number of cores genomeDCA is to use.
cores = 4

### Change this to reflect the path to your MATLAB executable
matlab = '/change/this/path'
####

### Change this to reflect the path to the genomeDCA code
plmdca = '/home/guest/software/genomeDCA'
####

try:
    if len(sys.argv) < 2:
        raise
    try:
        if not os.path.exists(matlab):
            sys.stderr.write('MATLAB executable path is not set properly. Trying to find it in system path\n')
            matlab = subprocess.check_output(['which', 'matlab']).strip()
    except:
        sys.stderr.write('Cannot find MATLAB executable, the path in {:s} is set erroneusly and the executable cannot be found automatically.\n'.format(sys.argv[0]))
        sys.exit(0)
        
    if not os.path.exists(plmdca + '/plmDCA_asymmetric.m'):
        sys.stderr.write('genomeDCA path is not set properly. Trying to find it in {:s}\n'.format(os.path.dirname(os.path.realpath(sys.argv[0]))))
        plmdca = os.path.dirname(os.path.realpath(sys.argv[0])) + '/genomeDCA'

    if not os.path.exists(plmdca + '/plmDCA_asymmetric.m'):
        sys.stderr.write('Still not found!\n')
        sys.exit(0)
    else:
        sys.stderr.write('Found!\n (NB: Please do set the path properly...)\n')

    for infile in sys.argv[1:]:
        os.chdir(os.path.abspath(infile)[:os.path.abspath(infile).rfind('/')]) 
        infilestem = infile.split('/')[-1]
        infilestem = infilestem[:infilestem.rfind('.')]

        if not os.path.exists(infilestem + ".genomedca"):
            print "Running genomeDCA on {:s}'".format(infile)
            print ' '.join([matlab, '-nodesktop', '-r', "path(path, 'PLMDCAPATH'); path(path, 'PLMDCAPATH/functions'); path(path, 'PLMDCAPATH/3rd_party_code/minFunc/'); plmDCA_asymmetric ( '".replace('PLMDCAPATH', plmdca) + infilestem + ".seq', '" + infilestem + ".genomedca', 0.1, {:d}); exit".format(cores)])

            t = subprocess.check_output([matlab, '-nodesktop', '-r', "path(path, 'PLMDCAPATH'); path(path, 'PLMDCAPATH/functions'); path(path, 'PLMDCAPATH/3rd_party_code/minFunc/'); plmDCA_asymmetric ( '".replace('PLMDCAPATH', plmdca) + infilestem + ".seq', '" + infilestem + ".genomedca', 0.1, {:d}); exit".format(cores)])
except Exception as e:
    print e
    sys.stderr.write('{:s} inputfile1.seq [inputfile2.seq ...]\n'.format(sys.argv[0])) 
    sys.stderr.write('\nThis script will run genomeDCA on all the input files provided in the command line\nREMEMBER: set the path to MATLAB executable and genomeDCA code in the header of the script\n')

#!/usr/bin/env python

import sys, subprocess, os
import string as s

# Change 4 to the desired number of cores mplmDCA is to use.
cores = 4

# Hard-coded MATLAB path. To be changed.
matlab = '/share/apps/matlab/R2012b/bin/matlab'
if not os.path.exists(matlab):
	matlab = '/share/matlab/r2012b/bin/matlab'

# Path to ./maelaplmdca
plmdca = '/home/guest/software/genomeDCA'

# To increase backwards compatibility with older Python versions
def check_output(command):
	return subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]
	


if len(sys.argv) < 2:
	print sys.argv[0], '<target>'
	sys.exit(0)

infile = sys.argv[1]
os.chdir(os.path.abspath(infile)[:os.path.abspath(infile).rfind('/')]) 
infilestem = infile.split('/')[-1]
infilestem = infilestem[:infilestem.rfind('.')]

if not os.path.exists(infilestem + ".genomedca"):
    print "Running mplmDCA"
	t = check_output([matlab, '-nodesktop', '-r', "path(path, 'PLMDCAPATH'); path(path, 'PLMDCAPATH/functions'); path(path, 'PLMDCAPATH/3rd_party_code/minFunc/'); plmDCA_asymmetric ( '".replace('PLMDCAPATH', plmdca) + infilestem + ".seq', '" + infilestem + ".genomedca', 0.1, {:d}); exit".format(cores)])

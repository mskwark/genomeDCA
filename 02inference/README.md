# Coupling inference

This step will infer evolutionary couplings between loci in pseudo-alignments generated in the previous step. These steps may be time consuming and therefore, it is strongly suggested that large scale computational resources are to be used.

## Prerequisite:
* sampled alignments generated in previous step (directory sampled/)
* MATLAB
* modified plmDCA (included in ./genomeDCA)

## Procedure
1. (before first use) Edit 00rungenomeDCA.py
    * Set the path to your MATLAB executable
    * Set the desired number of cores to use, or use -1 for the program to use all available cores
    * Set the absolute path to the ./genomeDCA directory
2. For each of the alignments, run ./00rungenomeDCA.py. Preferably on a computational cluster. A single run requires ~2 GB of memory.

    Example:

    `$> for t in sampled/sampling*/input.seq; do ./00rungenomeDCA.py $t; done`

    Note: `./00rungenomeDCA` can take more than one alignment input in the command line. In such a case, the inference will be run sequentially.

3. Wait until inference finishes. Single run takes ~10 minutes, out of which ~75% is spent in parallelized loop. When using 20 cores the run time can be reduced to ~3 minutes. Each sample can be run independently.

## Using GNU octave instead of MATLAB

1. Move genomeDCA/plmDCA_asymmetric_octave.m to genomeDCA/plmDCA_asymmetric.m
2. Use ./00rungenomeDCAoctave.py instead of ./00rungenomeDCA.py

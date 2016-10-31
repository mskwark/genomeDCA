# Sampling

This step generates randomized pseudo-alignments used in the subsequent steps. Each of the pseudo-alignments has a fixed width, roughly equal to the length of full genome sequence divided by the step size. Randomized sampling enables computational inference of the the couplings within attainable memory limits.

The only prerequisite for this step is a data file (pickled dictionary) produced in the previous step. As a result of running this script a series of directories named `sampled/samplingXXXX` (where X's stand for digits) will be produced. If a particular directory exists, it will be omitted, not overwritten. The script can be run multiple times to yield more data for analysis.

## Adjustable parameters
* The number of samples to produce (change 5000 to desired number). The more samples, the greater expected accuracy of the method.
* Step size (currently 1,500 bp). The greater the step size, potentially more unbiased the inference, at expense of missing some medium-range interactions and necessity of running more iterations (samples). Smaller step sizes increase the memory requirements of the inference step.

## Procedure
Run 00sample.py (for internal operation details, see source code)
`./00sample.py myGenomes.dat`.

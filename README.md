# genomeDCA

Application of evolutionary coupling inference to study of bacterial epistasis, as described in  'Interacting networks of resistance, virulence and core machinery genes identified by genome-wide epistasis analysis' by  Marcin J Skwark, Nicholas J Croucher, Santeri Puranen, Claire Chewapreecha, Maiju Pesonen, Ying Ying Xu, Paul Turner, Simon R Harris, Stephen B. Beres, James M. Musser, Julian Parkhill, Stephen D Bentley, Erik Aurell, Jukka Corander. 

This repository is a snapshot of software used to obtain results presented in the paper.

## Prerequisites

In order to successfully conduct this analysis, one needs:
* Python interpreter
* MATLAB installation
* an alignment of whole genomes for analysis
* (optionally) BLAST for analysis of the results on protein level

## Usage

The computational procedure comprises the following steps:

1. Analysis of the allelle distribution in the input genomes, filtering and encoding information for subsequent steps (`00datafiltering`)
2. Generation of pseudo-alignments for coupling inference (`01sampling`)
3. Coupling inference (`02inference`). *Warning:* this step is computationally intensive, but is amenable to parallel processing. 
4. Extraction of information from inferred couplings (`03postprocessing`).
5. (optional) Mapping the inferred couplings onto protein sequences (`04analysis`)

## Using Octave instead of MATLAB

It is possible to replace MATLAB with its open-source counterpart, Octave. We do not support this procedure and do not guarantee reproducibility of results.

* All changes necessary are to be done in 02inference/genomeDCA/plmDCA\_asymmetric.m
* Remove reference to `matlabpool`
* Compile `*.c` files with `mkoctfile --mex`
* Ensure that resultant file are in Octave's search path

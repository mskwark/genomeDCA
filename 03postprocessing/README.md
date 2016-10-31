# Processing inferred couplings

This step maps the couplings inferred previously back onto their genomic locations, as well as computes the summary statistics of coupling strengths.

## Prerequisites
* sampled alignments generated in previous step (directory sampled/)
* files with couplings inferred in previous step (each directory should
        contain files: input.seq, input.mapping and input.plmdca)

## Procedure:
1. (optional) In ./00process.py change `compressResults` variable 
    to enable compression (recommended) of output files.

2. For each of directories with inferred couplings, run ./00process.py

    Example:
    `$> for t in sampled/sampling*; do ./00process.py $t; done`

    You can do it while the inferrence on some of the samples is ongoing,
    in the interest of saving disk space

    You can also provide more than one directory name in the command line, then these driectories will be analysed sequentially.

3. To compute summary statistics, run `./01summary.py outfile.txt sampled/sampling*/`, that is first argument being the output file and remaining directories containing processed data.
    
    This can be run with incomplete data. 
    
    Produces a text file, with following syntax:

    <pre>
    1059441 1086321  0.04345  0.00263  0.04082  0.04608 2 5
    |       |        |        |        |        |       | |
    |       |        |        |        |        |       | \- number of possible combinations
    |       |        |        |        |        |       |    (i.e. how many times these sites
    |       |        |        |        |        |       |     were in the same input alignment)
    |       |        |        |        |        |       |   
    |       |        |        |        |        |       \- number of times this site pair was among
    |       |        |        |        |        |          top 3000 couplings in the sampled alignments
    |       |        |        |        |        |          
    |       |        |        |        |        \- maximum value of coupling inferred
    |       |        |        |        \- minimum value of coupling inferred and kept (!)
    |       |        |        \- standard deviation of coupling value
    |       |        \- mean coupling value
    |       \- locus/site 2
    \- locus/site 1</pre>

    Site pairs which consistently score high (high mean, low standard deviation, number of times 
    sampled equal or almost equal to number of combinations) are likely to be true couplings

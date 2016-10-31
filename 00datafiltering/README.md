# Data pre-processing

To prepare the data for subsequent analysis by genomeDCA, you need a file with
aligned genomes of organism in question. This method (genomeDCA) is independent
of the alignment method used. For a sample input file, see `example/maela.head`.

The process of preparing the input data (pickled Python dictionary) is fully autonomous. Run it by `./00process.py maela3K.fas maela3K.data`.

The script will:
1. Read in the sequences of your aligned genomes
2. Compute allelle frequencies
3. Filter out these positions that do not meet criteria (see below)
4. Store the data in easily accessible format for further processing.

## Adjustable parameters

The required minor allelle frequency and maximum fraction of gaps can be
adjusted in the header of the script, as `minimalMAF` and `gapFraction`
respectively. The results in the paper have been obtained with these parameters
set to default values.

Lower `minimalMAF` allows to include more sites in the analysis, which comes at
a cost of increased time and memory requirements. 

Higher `gapFraction` allows to include more sites in the analysis, at the cost of 
gap-rich sites skewing the analysis.

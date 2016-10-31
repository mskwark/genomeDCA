= Identifying proteins corresponding to loci

Remark: This part of pipeline has not been fully automated

1. a) For each of the sites in top couplings identified in the previous steps, 
    extract a fragment of S. pneumoniae genome of length 1001, including
    500 positions up- and down-stream from the site.

   b) For each extracted sequence run tblastx against a reference database
        with pneumoccocal protein sequences (downloadable from uniprot.org)
        Sequences used in this research are in `./pneumococcus-reference.fa`

    For an example how it can be done, see `./00runblast.py`
    (requires a formatted BLAST database - use formatdb -i pneumococcus-reference.fa)

2. Cluster high-scoring sites by proteins to which they belong, with manual inspection
    to ensure correctness of idenitified hit (important for sites in the proximity of
    protein coding region, but not in the protein coding region itself).

Alternatively:
1. Divide genome into 600bp sequences, overlapping at 300bp
2. For each of sequences run tblastx against reference genome,
    thus mapping the S. pneumoniae proteome onto genome
3. Map each high scoring site to a corresponding protein-coding gene

For example how it can be done, see `./01altblast.py`




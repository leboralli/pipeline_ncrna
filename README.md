Created in 20/02/19

Snakefile will be the primary way to write pipelines for my PhD. But if this shows be too complicated, so maybe I write in bash or python.

For the first exploratory analysis we choose 3 samples from BrainSeq.

R3895_C101EACXX_CAGATC_L004_,R4255_D1AACACXX_GATCAG_L004_ and 'R5871_C0CEWACXX_TGACCA_L003_

For this test I will run the pipeline in Google Cloud (GC). The second version of GC server
was made in 02/09.

The pipeline run from FASTP (quality control) until the lnc predictor (FEELnc).

I start with $300

-----------------------------------------------------------------
Now I'm using the server NGS3, with 46gb RAM and 24 cores.

Versions of the programs:
FASTP - 0.20.0
STAR - 2.7.2b
Scallop - v0.10.4
stringtie - 1.3.6
FEElnc - v0.11
salmon - 0.14.1

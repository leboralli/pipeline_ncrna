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
snakemake - 5.6.0

PYTHON IN LINC = 3.6.8
PYTHON IN NGS3 = 3.7.3, so I need to create a conda env to run the pipeline

----------------------------------------------------------------

Test was a success, if we ignore the non statistical significance.
For the second test I will test patients vs control.

SCZ: R2809, R2810, R2816, R2825, R2827
Control: R2826, R2835, R2836, R2839, R2845

After many problems, I started the pipeline for the second test in 18:17,
18/10/2019

---------------------------------------------------------------
Ok, now I need to test my pipeline with more samples, because the statistical
test in edgeR demands a good pool of samples.
The samples:

SCZ: R2809, R2810, R2816, R2825, R2827, R2860, R2866, R2867
Control: R2826, R2835, R2836, R2839, R2845, R2897

I need to download this samples:
SCZ - R2828, R2831, R2834, R2840, R2841, R2868, R2885, R2886, R2889, R2890, R2893
Control - R2855, R2857, R2869, R2874, R2894, R2895, R2905, R2906, R2907, R2912,
          R2944, R2945, R2947, R2954

NEWS: the test was a success, but I still need a lot of samples.
------------------------------------------------------------------
I will change the lncRNA predictor, because I'm not confident with FEElnc.
And I will use two packages, combining the outputs, for more confident results.

The packages: CPAT and Slncky.

But I'm thinking in change a lot of things in my pipeline, using the paper
"The Long Noncoding RNA Landscape in Amygdala Tissues from Schizophrenia Patients"
as a parameter.

With the changes:
Fastp -> STAR -> medTIN (median transcript integrity number, for RNA integrity) ->
Scallop (LNCipedia, in the paper was used genomic regions with at least
reads coverage 2.5) -> Stringtie-merge (reference annotation - LNCipedia) ->
gffcompare (reference annotation - LNCipedia, for identify novel transcripts) ->
slncky + CPAT (using the novel transcripts - considered only the consensus results) ->
add novel lncRNAs in the reference annotation (LNCipedia)

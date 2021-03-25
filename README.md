### Created in 20/02/19

-----------------------------------------------------------------
Now I'm using the server NGS3, with 46gb RAM and 24 cores.

## Versions of the programs:
- FASTP - **0.20.0**
- STAR - **2.7.2b**
- Scallop - **v0.10.4**
- stringtie - **1.3.6**
- FEElnc - **v0.11**
- salmon - **0.14.1**
- snakemake - **5.6.0**

- PYTHON IN LINC = **3.6.8**
- PYTHON IN NGS3 = 3.7.3, so I need to create a conda env to run the pipeline

PLEASE ATTENTION TO THE VERSIONS OF THE PROGRAMS
# Install your enviroment with
conda env create -f pipe_v2.yml

----------------------------------------------------------------

Scripts used in the analyses:
- parameters.txt
- config.py
- get_fastq.py
- Snakefile

# PLEASE CONFIGURE config.py and get_fastq.py TO YOUR SYSTEM!

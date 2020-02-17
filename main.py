#############################################################
#Main file for running the pipeline
#Author: Leandro Boralli
#
#
#
#############################################################
import os
import config as cf
import get_fastq as GF

# print (cf.SAMPLES)
for smp in cf.SAMPLES:
    os.system('ls /homelocal/boralli/workdir/pipeline_v3/STAR/output/' + str(smp))

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

star_directory = '/homelocal/boralli/workdir/pipeline_v3/STAR/output/'
# print (cf.SAMPLES)
for smp in cf.SAMPLES:
    os.system('ls ' str(star_directory) + str(smp))

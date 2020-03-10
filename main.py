#############################################################
#               WORKING IN PROGRESS!!!!                     #
#Main file for running the pipeline
#Author: Leandro Boralli
#
#
#
#############################################################
import os
import config as cf
import get_fastq as GF

star_directory = cf.STAR_DIR

list_samples = cf.SAMPLES

os.system('snakemake -np')

# cleaning the temp files
# for smp in list_samples:
#     os.system('rm -v !(' + str(star_directory) + str(smp)) + '/' +
#         str(smp) + 'Aligned.sortedByCoord.out.bam)' #STAR directory
    # os.system('rm -v !(' + str(star_directory) + str(smp)) + '/' +
    #     str(smp) + 'Aligned.sortedByCoord.out.bam)' #STAR directory

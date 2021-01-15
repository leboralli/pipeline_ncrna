# from get_fastq import getListOfFastq, dirName
import get_fastq as GF
import os
# listOfFiles = GF.getListOfFastq(GF.dirName("/home/boralli/workdir/data"))
listOfFiles = GF.getListOfFastq(GF.dirName("/home/boralli/workdir/data"))
list_fastpFiles = GF.getListOfFastq(GF.dirName("/home/boralli/workdir/FASTP"))
# print(listOfFiles)
samples_fastq = GF.get_fastqFiles(listOfFiles)
samples_fastq_fastp = GF.get_fastqFiles(list_fastpFiles)
SAMPLES = samples_fastq
SAMPLES_FP = samples_fastq_fastp
# print (len(SAMPLES_FP))
# print(samples_fastq_fastp)
#TESTE
TESTE_DATA = "/home/leboralli/Documents/workdir"

#Directories
WORK_DIR = "/home/boralli/workdir/" #ngs
# WORK_DIR = "/mnt/disks/sba1/" #google
DATA_DIR =  "/home/boralli/workdir/data/" #ngs
# DATA_DIR =  "/mnt/disks/sba1/data/" #google
PIPE = WORK_DIR + "pipeline_allLanes/"
PIPE_OLD = WORK_DIR + "pipeline_v4/"

IDX_DIR = PIPE_OLD + "index/"
FASTP_DIR = WORK_DIR + "FASTP/"
STAR_DIR = PIPE + "STAR/"
SCALLOP_DIR = PIPE + "SCALLOP"

#Criando o diretorio do Stringtie, caso não exista
if not os.path.exists(PIPE + 'STRINGTIE'):
    os.makedirs(PIPE + 'STRINGTIE') 

STRINGTIE_DIR = PIPE + "STRINGTIE"
GTF_DIR = PIPE + "GTF/"
# TACO_DIR = PIPE + "TACO_output/"
STRINGTIE_OUT = PIPE + "STRINGTIE_MERGE/"
GTF_TO_FASTA = PIPE + "GTF_FASTA/"

FEELNC_DIR = PIPE + "FEELNC/"
FEELNC_FILTER = FEELNC_DIR + "FILTER/"
FEELNC_CODPOT = FEELNC_DIR + "CODPOT/"
FEELNC_CLASSIFIER = FEELNC_DIR + "CLASSIFIER/"

SALMON_DIR = PIPE + "SALMON"
SALMON_INDEX = SALMON_DIR + "/gencode.v33.transcripts.index"
SALMON_DIR_MRNA = PIPE + "SALMON_MRNA"
SALMON_INDEX_MRNA = SALMON_DIR + "/gencode.v33.transcripts_mRNA.index"
#index
GENOME_FILE = DATA_DIR + "GRCh38.p13.genome.fa"
GTF = DATA_DIR + "gencode.v33.annotation.gtf"
PC = DATA_DIR + "gencode.v33.pc_transcripts.fa"
# LNCRNA = DATA_DIR + "gencode.v31.long_noncoding_RNAs.gtf"
TRANSCRPT = DATA_DIR + "gencode.v33.transcripts.fa"
LNCRNA = DATA_DIR + "lncipedia_5_2_hg38.gtf"

#Log
LOGS = PIPE + "LOGS/"
FASTP_LOG = LOGS + "FASTP_LOG/"

#BENCHMARK
BENCHMARK_DIR = PIPE + "BENCHMARK"

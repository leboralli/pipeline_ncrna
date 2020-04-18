# from get_fastq import getListOfFastq, dirName
import get_fastq as GF

listOfFiles = GF.getListOfFastq(GF.dirName("/home/boralli/workdir/data"))
list_fastpFiles = GF.getListOfFastq(GF.dirName("/homelocal/boralli/workdir/pipeline_v4/FASTP"))
# print(listOfFiles)
samples_fastq = GF.get_fastqFiles(listOfFiles)
samples_fastq_fastp = GF.getListOfFastq(list_fastpFiles)
# print(samples_fastq)
#TESTE
TESTE_DATA = "/home/leboralli/Documents/workdir"

#Directories
WORK_DIR = "/homelocal/boralli/workdir/"
DATA_DIR =  "/home/boralli/workdir/data/"
PIPE = WORK_DIR + "pipeline_v4/"
PIPE_OLD = WORK_DIR + "pipeline_v3/"

IDX_DIR = PIPE_OLD + "index/"
FASTP_DIR = PIPE + "FASTP/"
STAR_DIR = PIPE + "STAR/"
SCALLOP_DIR = PIPE + "SCALLOP"
STRINGTIE_DIR = PIPE + "STRINGTIE/"
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

#Samples
# SAMPLES = ['R2809_D2A01ACXX_TAATGCGC_L005_',
#            'R2810_C00JVACXX_CGATGT_L001_',
#            'R2816_C0GTHACXX_ACTGAT_L007_',
#            'R2825_C00JVACXX_TTAGGC_L001_',
#            'R2826_C00JVACXX_TGACCA_L001_',
#            'R2827_C0JYLACXX_TTAGGC_L005_',
#            'R2835_C0JYLACXX_TGACCA_L004_',
#            'R2836_C3V3YACXX_CGGCTATG_L001_',
#            'R2839_C0UH3ACXX_ATTACTCG_L001_',
#            'R2845_C0J1FACXX_GCCAAT_L005_'
#            ]

SAMPLES = samples_fastq
SAMPLES_FP = list_fastpFiles
# print(SAMPLES)
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

# Pegando lista de samples
# listOfFiles = GF.getListOfFastq(GF.dirName("/home/leboralli/Documents/Aulas/Tutorial-Linux-1/arquivos_testes"))
# print(listOfFiles)
# samples_fastq = GF.get_fastqFiles(listOfFiles)
# #
# print(samples_fastq)

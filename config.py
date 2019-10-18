# from get_fastq import getListOfFastq, dirName
import get_fastq as GF

#TESTE
TESTE_DATA = "/home/leboralli/Documents/workdir"

#Directories
WORK_DIR = "/home/boralli/workdir/"
DATA_DIR = WORK_DIR + "data/"
PIPE_V1 = WORK_DIR + "pipeline-v01/"

IDX_DIR = PIPE_V1 + "index/"
FASTP_DIR = PIPE_V1 + "FASTP/"
STAR_DIR = PIPE_V1 + "STAR/"
SCALLOP_DIR = PIPE_V1 + "SCALLOP"
GTF_DIR = PIPE_V1 + "GTF/"
# TACO_DIR = PIPE_V1 + "TACO_output/"
STRINGTIE_OUT = PIPE_V1 + "STRINGTIE_MERGE/"
GTF_TO_FASTA = PIPE_V1 + "GTF_FASTA/"

FEELNC_DIR = PIPE_V1 + "FEELNC/"
FEELNC_FILTER = FEELNC_DIR + "FILTER/"
FEELNC_CODPOT = FEELNC_DIR + "CODPOT/"
FEELNC_CLASSIFIER = FEELNC_DIR + "CLASSIFIER/"

SALMON_DIR = PIPE_V1 + "SALMON"
SALMON_INDEX = SALMON_DIR + "/gencode.v31.transcripts.index"

#Samples
SAMPLES = ['R2809_D2A01ACXX_TAATGCGC_L005_',
           'R2810_C00JVACXX_CGATGT_L001_',
           'R2816_C0GTHACXX_ACTGAT_L007_',
           'R2825_C00JVACXX_TTAGGC_L001_',
           'R2826_C00JVACXX_TGACCA_L001_',
           'R2827_C0JYLACXX_TTAGGC_L005_',
           'R2835_C0JYLACXX_TGACCA_L004_',
           'R2836_C3V3YACXX_CGGCTATG_L001_',
           'R2839_C0UH3ACXX_ATTACTCG_L001_R1_',
           'R2845_C0J1FACXX_GCCAAT_L005_'          
           ]

#index
GENOME_FILE = DATA_DIR + "GRCh38.p12.genome.fa"
GTF = DATA_DIR + "gencode.v31.annotation.gtf"
PC = DATA_DIR + "gencode.v31.pc_transcripts.fa"
LNCRNA = DATA_DIR + "gencode.v31.long_noncoding_RNAs.gtf"
TRANSCRPT = DATA_DIR + "gencode.v31.transcripts.fa"

#Log
LOGS = PIPE_V1 + "LOGS/"
FASTP_LOG = LOGS + "FASTP_LOG/"

#BENCHMARK
BENCHMARK_DIR = PIPE_V1 + "BENCHMARK"

# Pegando lista de samples
listOfFiles = GF.getListOfFastq(GF.dirName(TESTE_DATA))
# print(listOfFiles)
samples_fastq = GF.get_fastqFiles(listOfFiles)

print(samples_fastq)

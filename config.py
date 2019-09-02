#Directories
WORK_DIR = "/home/leboralli/workdir/"
DATA_DIR = "/home/leboralli/data/"
PIPE_V1 = WORK_DIR + "pipeline-v01/"

IDX_DIR = PIPE_V1 + "index/"
FASTP_DIR = PIPE_V1 + "FASTP/"
STAR_DIR = PIPE_V1 + "STAR/"
SCALLOP_DIR = PIPE_V1 + "SCALLOP"
GTF_DIR = PIPE_V1 + "GTF/"
# TACO_DIR = PIPE_V1 + "TACO_output/"
STRINGTIE_OUT = PIPE_V1 + "STRINGTIE_MERGE/"

FEELNC_DIR = PIPE_V1 + "FEELNC/"
FEELNC_FILTER = FEELNC_DIR + "FILTER/"
FEELNC_CODPOT = FEELNC_DIR + "CODPOT/"
FEELNC_CLASSIFIER = FEELNC_DIR + "CLASSIFIER/"

SALMON_DIR = PIPE_V1 + "SALMON"
SALMON_INDEX = SALMON_DIR + "/gencode.v31.transcripts.index"

#Samples
SAMPLES = ['R3895_C101EACXX_CAGATC_L004_',
    'R4255_D1AACACXX_GATCAG_L004_',
    'R5871_C0CEWACXX_TGACCA_L003_']

#index
FASTA_FILE = DATA_DIR + "GRCh38.p12.genome.fa"
GTF = DATA_DIR + "gencode.v31.annotation.gtf"
PC = DATA_DIR + "gencode.v31.pc_transcripts.fa"
LNCRNA = DATA_DIR + "gencode.v31.long_noncoding_RNAs.gtf"
TRANSCRPT = DATA_DIR + "gencode.v31.transcripts.fa"
#Log

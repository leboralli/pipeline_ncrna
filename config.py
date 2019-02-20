#work
WORK_DIR = "/work/tbLincRnas/pipeline/pipeline_v02/"
# SAMPLES_DIR = WORK_DIR + "data/concatenated_data/"
LOGS = WORK_DIR +  "logs/"

#Index
REF_DIR = "/work/tbLincRnas/data/ref_gen/"
IDX_KALL = REF_DIR + "essembl_kallisto/Homo_sapiens.GRCh38.cdna.all.fa.idx"

# FASTP_OUT = WORK_DIR + "data/fastp/"
# KALL_OUT = WORK_DIR + "data/kallisto/"

#Logs e Benchmark
# KALLISTO_LOG = LOGS + "kallisto/"
STAR_LOG = LOGS + "star/"
BENCHMARK = LOGS + "benchmark/"

#Samples
SAMPLES_STAR = ['TFB267_S7', 'TFB269_S8','TFB271_S9', 'TFB273_S10', 'TFB275_S11' ,
           'TFB277_S12', 'TFB279_S13', 'TFB281_S14', 'TFB283_S15', 'TFB285_S16',
           'TFB287_S17', 'TFB289_S18', 'ZN21_S1','ZN22_S2','ZN27_S3','ZN28_S4',
           'ZN29_S5','ZN30_S6']

SAMPLES = ['TFB267', 'TFB269','TFB271', 'TFB273', 'TFB275', 'TFB277',
        'TFB279', 'TFB281', 'TFB283', 'TFB285', 'TFB287', 'TFB289',
        'ZN21','ZN22','ZN27','ZN28', 'ZN29','ZN30']

#Trimmed files
FASTP_DIR = "/work/tbLincRnas/data/fastp/"
SAMPLES_FASTP = ["TFB267_S7_R1.fastq.gz.good", "TFB267_S7_R2.fastq.gz.good",
            "TFB269_S8_R1.fastq.gz.good", "TFB269_S8_R2.fastq.gz.good",
            "TFB271_S9_R1.fastq.gz.good", "TFB271_S9_R2.fastq.gz.good",
            "TFB273_S10_R1.fastq.gz.good", "TFB273_S10_R2.fastq.gz.good",
            "TFB275_S11_R1.fastq.gz.good", "TFB275_S11_R2.fastq.gz.good",
            "TFB277_S12_R1.fastq.gz.good", "TFB277_S12_R2.fastq.gz.good",
            "TFB279_S13_R1.fastq.gz.good", "TFB279_S13_R2.fastq.gz.good",
            "TFB281_S14_R1.fastq.gz.good", "TFB281_S14_R2.fastq.gz.good",
            "TFB283_S15_R1.fastq.gz.good", "TFB283_S15_R2.fastq.gz.good",
            "TFB285_S16_R1.fastq.gz.good", "TFB285_S16_R2.fastq.gz.good",
            "TFB287_S17_R1.fastq.gz.good", "TFB287_S17_R2.fastq.gz.good",
            "TFB289_S18_R1.fastq.gz.good", "TFB289_S18_R2.fastq.gz.good",
            "ZN21_S1_R1.fastq.gz.good", "ZN21_S1_R2.fastq.gz.good",
            "ZN22_S2_R1.fastq.gz.good", "ZN22_S2_R2.fastq.gz.good",
            "ZN27_S3_R1.fastq.gz.good", "ZN27_S3_R2.fastq.gz.good",
            "ZN28_S4_R1.fastq.gz.good", "ZN28_S4_R2.fastq.gz.good",
            "ZN29_S5_R1.fastq.gz.good", "ZN29_S5_R2.fastq.gz.good",
            "ZN30_S6_R1.fastq.gz.good", "ZN30_S6_R2.fastq.gz.good"]

THREADS = 40
STAR_INDEX = WORK_DIR + "01-STAR/index/"
STAR = WORK_DIR + "01-STAR/"
STAR_LOG = STAR + "log/"


# INICONFIG = "saveCommand /usr/bin/time --verbose --output $output_star/star_run.time"

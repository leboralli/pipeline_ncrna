#work
WORK_DIR = "/work/tbLincRnas/users/leboralli/work/"
WORK_SAMPLES = WORK_DIR + "raw"

# SAMPLES_DIR = WORK_DIR + "data/concatenated_data/"
LOGS = WORK_DIR +  "logs/"

#Index
STAR_INDEX = "/work/tbLincRnas/data/ref_gen/gencode_Human/"

#Samples
# SAMPLES_STAR = []
SAMPLES = ['SRR7770783', 'SRR7770780', 'SRR7770776',
            'SRR7770793', 'SRR7770791', 'SRR7770789']

#Trimmed files
FASTP_DIR = WORK_DIR + "fastp/"
# SAMPLES_FASTP = ["TFB267_S7_R1.fastq.gz.good", "TFB267_S7_R2.fastq.gz.good",
#             "TFB269_S8_R1.fastq.gz.good", "TFB269_S8_R2.fastq.gz.good",
#             "TFB271_S9_R1.fastq.gz.good", "TFB271_S9_R2.fastq.gz.good",
#             "TFB273_S10_R1.fastq.gz.good", "TFB273_S10_R2.fastq.gz.good",
#             "TFB275_S11_R1.fastq.gz.good", "TFB275_S11_R2.fastq.gz.good",
#             "TFB277_S12_R1.fastq.gz.good", "TFB277_S12_R2.fastq.gz.good",
#             "TFB279_S13_R1.fastq.gz.good", "TFB279_S13_R2.fastq.gz.good",
#             "TFB281_S14_R1.fastq.gz.good", "TFB281_S14_R2.fastq.gz.good",
#             "TFB283_S15_R1.fastq.gz.good", "TFB283_S15_R2.fastq.gz.good",
#             "TFB285_S16_R1.fastq.gz.good", "TFB285_S16_R2.fastq.gz.good",
#             "TFB287_S17_R1.fastq.gz.good", "TFB287_S17_R2.fastq.gz.good",
#             "TFB289_S18_R1.fastq.gz.good", "TFB289_S18_R2.fastq.gz.good",
#             "ZN21_S1_R1.fastq.gz.good", "ZN21_S1_R2.fastq.gz.good",
#             "ZN22_S2_R1.fastq.gz.good", "ZN22_S2_R2.fastq.gz.good",
#             "ZN27_S3_R1.fastq.gz.good", "ZN27_S3_R2.fastq.gz.good",
#             "ZN28_S4_R1.fastq.gz.good", "ZN28_S4_R2.fastq.gz.good",
#             "ZN29_S5_R1.fastq.gz.good", "ZN29_S5_R2.fastq.gz.good",
#             "ZN30_S6_R1.fastq.gz.good", "ZN30_S6_R2.fastq.gz.good"]

THREADS = 40

STAR = WORK_DIR + "01-STAR/"
STAR_LOG = STAR + "log/"


# INICONFIG = "saveCommand /usr/bin/time --verbose --output $output_star/star_run.time"

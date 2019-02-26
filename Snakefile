include:
	'config.py'

rule all:
	input:
		# expand(FASTP_OUT + "{sample}_R{read_no}.fastq.gz.good",sample=SAMPLES ,read_no=['1', '2']),
		# expand(WORK_DIR + "/trimmed/{sample_ips}_R{read_no}.fastq.gz.good",sample_ips=SAMPLE_IPS, read_no=['1','2']),
		# expand(KALL_OUT + "{sample}", sample=SAMPLES),
		# expand(STAR + "/input/{sample}_R{read_no}.fastq.gz.good.sym", sample=SAMPLES, read_no=['1', '2']),
		# expand(STAR + "input/{sample}", sample=SAMPLES),
		# expand(STAR + "output/{sample}/{sample}", sample=SAMPLES),
		# expand(WORK_DIR + "02-SCALLOP/output/{sample}/{sample}Aligned.sortedByCoord.out.gtf", sample=SAMPLES)

#rule download_fastq:
	# input:
	# 	# names = lista_SRA
	# shell: """
	# 	fastq-dump {input.names} \
	#	mv {output.names} WORK_DIR + "{output}"
	#	"""


# rule fastp:
# 	input:
# 		R1= SAMPLES_DIR + "{sample}_R1.fastq.gz",
# 		R2= SAMPLES_DIR + "{sample}_R2.fastq.gz"
# 	output:
# 		R1out= FASTP_OUT + "{sample}_R1.fastq.gz.good",
# 		R2out= FASTP_OUT + "{sample}_R2.fastq.gz.good"
# 	log: WORK_DIR + "data/fastp/{sample}"
# 	shell:
# 		"fastp -i {input.R1} -I {input.R2} -o {output.R1out} -O {output.R2out} -h {log}"
#
# rule star:
# 	input:
# 		idx_star = STAR_INDEX,
# 		R1 = FASTP_DIR + "{sample}_R1.fastq.sym",
# 		R2 = FASTP_DIR + "{sample}_R2.fastq.sym",
# 		parameters = STAR + "config/parameters.txt"
# 	output:
# 		out = STAR + "output/{sample}/{sample}"
# 		#run_time = STAR + "log/star_run.time"
# 	#threads: THREADS
# 	# log: STAR_LOG
# 	# benchmark: BENCHMARK + "star/{sample_star}"
# 	shell:
# 		"saveCommand STAR --runThreadN 40 --genomeDir {input.idx_star} \
# 		--readFilesIn {input.R1} {input.R2} --outFileNamePrefix {output.out}\
# 		--parametersFiles {input.parameters} \
# 		--quantMode TranscriptomeSAM GeneCounts"

# rule scallop:
# 	input:
# 		star_output = STAR + "output/{sample}/{sample}Aligned.sortedByCoord.out.bam"
# 	output:
# 		scallop_output = WORK_DIR + "02-SCALLOP/output/{sample}/{sample}Aligned.sortedByCoord.out.gtf"
# 	shell:
# 		"scallop -i {input.star_output} -o${output.scallop_output} \
# 		--verbose 2 --min_transcript_lenght_base 200 --min_mapping_quality 255 \
# 		--min_splice_bundary_hits 2"

# # rule gffcompare:
# 	input:
# 		scallop_gtf =
# 	output:
# 		gffcompare_output
# 	shell:
# 		""
#
# rule come:
# 	input:
#
# 	output:
#
# 	shell:
#
# rule salmon:
#
# rule rsem:
#
# rule edgeR:

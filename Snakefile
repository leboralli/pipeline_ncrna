include:
	'config.py'

print (SAMPLES_FP)
rule all:
	input:
		# expand(SAMPLES_DIR + "{samples}", samples=SAMPLES), #fastq_dump
		# expand(FASTP_DIR + "{sample}R{read_no}.fastq",sample=SAMPLES ,read_no=['1', '2']), #fastp
		# IDX_DIR, #index
		expand(STAR_DIR + "output/{sample}/{sample}Aligned.sortedByCoord.out.bam",sample=SAMPLES_FP), #STAR
		# expand(STAR_DIR + "output/{sample}/{sample}Aligned.sortedByCoord.out.bam", sample=SAMPLES), #rm_star
		# expand(SCALLOP_DIR + "/{sample}/{sample}Aligned.sortedByCoord.out.gtf",sample=SAMPLES), #scallop
		expand(STRINGTIE_DIR + "/{sample}/{sample}Aligned.sortedByCoord.out.gtf", sample=SAMPLES_FP),
		GTF_DIR + "path_samplesGTF.txt",
		# # TACO_DIR, #taco
		STRINGTIE_OUT + "assembly.gtf", #STRINGTIE-MERGE
		# # "gffcompare_out_", #gffcompare
		GTF_TO_FASTA + "assembly_fasta.fa", #gffread
		FEELNC_FILTER + "candidate_lncrna.gtf", #FEELnc_filter
		FEELNC_CODPOT, #feelnc_codpot
		FEELNC_CLASSIFIER + "lncRNA_classes.txt", #feelnc_classifier
		# SALMON_DIR, #salmon_index
		expand(SALMON_DIR + "/output/{sample}_quant", sample=SAMPLES_FP)

# rule fastq_dump:
# 	input:
# 		samples = SAMPLES
# 	output:
# 		dir_out = SAMPLES_DIR + "{samples}"
# 	shell:
# 		"fastq-dump -I {input.samples} -o {output.dir_out}"

rule fastp:
	input:
		R1= DATA_DIR + "{sample}R1_001.fastq.gz",
		R2= DATA_DIR + "{sample}R2_001.fastq.gz"
	output:
		R1out= FASTP_DIR + "{sample}R1.fastq",
		R2out= FASTP_DIR + "{sample}R2.fastq"
	params:
		data_dir = DATA_DIR,
		name_sample = "{sample}"
	log: FASTP_LOG + "{sample}.html"
	message: "Executando o programa FASTP"
	run:
		shell('fastp -i {input.R1} -I {input.R2} -o {output.R1out} -O {output.R2out} \
		-h {log} -j {log}')
		shell("find {params.data_dir} -type f -name '{params.name_sample}*' -delete ")


# rule star_idx:
# 	input:
# 		fasta = GENOME_FILE,
# 		gtf = GTF
# 	output:
# 		genome_dir = directory(IDX_DIR)
# 	# threads: 18
# 	shell:
# 		"STAR --runThreadN 18 \
# 		--runMode genomeGenerate \
# 		--genomeDir {output.genome_dir} \
# 		--genomeFastaFiles {input.fasta} \
# 		--sjdbGTFfile {input.gtf} --sjdbOverhang 99"

rule star:
	input:
		idx_star = IDX_DIR,
		R1 = FASTP_DIR + "{sample}R1.fastq",
		R2 = FASTP_DIR + "{sample}R2.fastq",
		parameters = "parameters.txt",

	params:
		outdir = STAR_DIR + "output/{sample}/{sample}",
		star_dir = STAR_DIR,
		star_sample = '{sample}'
	# threads: 18
	output:
		out = STAR_DIR + "output/{sample}/{sample}Aligned.sortedByCoord.out.bam"
		#run_time = STAR + "log/star_run.time"
	# log: STAR_LOG
	# benchmark: BENCHMARK + "star/{sample_star}"
	run:
		print("{params.star_sample}")
		shell("STAR --runThreadN 9 --genomeDir {input.idx_star} \
		--readFilesIn {input.R1} {input.R2} --outFileNamePrefix {params.outdir}\
		--parametersFiles {input.parameters} \
		--quantMode TranscriptomeSAM GeneCounts \
		--genomeChrBinNbits 12")
		# shell("find {params.star_dir} -type f ! -name '{params.star_sample}Aligned.sortedByCoord.out.bam' -delete")


# rule rm_star:
# 	input:
# 		file = STAR_DIR + "output/{sample}/{sample}Aligned.sortedByCoord.out.bam"
# 	# params:
# 	# 	except_file = "{sample}Aligned.sortedByCoord.out.bam"
# 	output:
# 		file_to_maintain = STAR_DIR + "output/{sample}/{sample}Aligned.sortedByCoord.out.bam"
# 	shell:
# 		"rm !({input.file})"

# rule scallop:
# 	input:
# 		star_output = STAR_DIR + "output/{sample}/{sample}Aligned.sortedByCoord.out.bam"
# 	output:
# 		scallop_output = SCALLOP_DIR + "/{sample}/{sample}Aligned.sortedByCoord.out.gtf"
# 	run:
# 		shell("scallop -i {input.star_output} -o {output.scallop_output} \
# 		--verbose 1 --min_transcript_lenght_base 200 \
# 		--min_splice_bundary_hits 2 ")

rule stringtie:
	input:
		star_output = STAR_DIR + "output/{sample}/{sample}Aligned.sortedByCoord.out.bam"
	output:
		stringtie_output = STRINGTIE_DIR + "/{sample}/{sample}Aligned.sortedByCoord.out.gtf"
	run:
		shell("stringtie {input.star_output} -o {output.stringtie_output} \
		-v -p 12 ")

rule grep_gtf:
	input:
		list_gtf = STRINGTIE_DIR
	output:
		paths = GTF_DIR + "path_samplesGTF.txt"
	shell:
		"find {input.list_gtf} | grep .gtf > {output.paths}"

# #taco gera um problema na hora de rodar, pq provavelmente o snakemake tenta criar
# #a pasta antes e o taco identifica como pasta já criada, talvez usar params
# # rule taco:
# # 	input:
# # 		all_gtf = GTF_DIR + "path_samplesGTF.txt"
# # 	output:
# # 		taco_out = directory(TACO_DIR)
# # 	params:
# # 		taco_out = directory(TACO_DIR)
# # 	shell:
# # 		"taco_run -v -p 8  -o {params.taco_out} \
# # 		--filter-min-expr 1 --gtf-expr-attr RPKM {input.all_gtf}"
#
# #Mudemos para o Stringtie-merge!
rule stringtiemerge:
	input:
		samples_gtf = GTF_DIR + "path_samplesGTF.txt",
		annotation = GTF
	output:
		merge_out = STRINGTIE_OUT + "assembly.gtf"
	shell:
		"stringtie --merge -G {input.annotation} -o {output.merge_out} -m 200 \
		{input.samples_gtf}"

# rule gffcompare:
# 	input:
# 		assembly = STRINGTIE_OUT + "assembly.gtf",
# 		annotation = GTF
# 	output:
# 		out_prefix = "gffcompare_out_"
# 	shell:
# 		"gffcompare -r {input.annotation} -o {output.out_prefix} \
# 		-i {input.assembly}"

#GTF to FASTA
rule gtf_to_fasta:
	input:
		gtf_file = STRINGTIE_OUT + "assembly.gtf",
		genome = GENOME_FILE
	output:
		merged_fasta = GTF_TO_FASTA + "assembly_fasta.fa"
	shell:
		"gffread -w {output.merged_fasta} -g {input.genome} {input.gtf_file}"

rule feelnc_filter:
	input:
		assembly = STRINGTIE_OUT + "assembly.gtf",
		annotation = GTF
	# params:
	# 	assembly = TACO_DIR + "assembly.gtf"
	output:
		candidate_lncrna = FEELNC_FILTER + "candidate_lncrna.gtf"
	shell:
		"FEELnc_filter.pl -p 18 -i {input.assembly} -a {input.annotation} -o \
		--verbosity 1 --monoex=1 > {output.candidate_lncrna}"

rule feelnc_codpot:
	input:
		candidates = FEELNC_FILTER + "candidate_lncrna.gtf",
		# assembly = STRINGTIE_OUT + "assembly.gtf",
		know_pc = PC,
		know_lnc = LNCRNA,
		genome = GENOME_FILE
	output:
		out_dir = directory(FEELNC_CODPOT)
	shell:
		"FEELnc_codpot.pl -p 18 -i {input.candidates} -a {input.know_pc} -g {input.genome} \
		-l {input.know_lnc} --outdir {output.out_dir} --learnorftype=3 -v 1"

rule feelnc_classifier:
	input:
		codpot = FEELNC_CODPOT,
		annotation = GTF
	output:
		out_classifier = FEELNC_CLASSIFIER + "lncRNA_classes.txt"
	shell:
		"FEELnc_classifier.pl -i {input.codpot}candidate_lncrna.gtf.lncRNA.gtf -a {input.annotation} \
		> {output.out_classifier}"

# rule salmon_index:
# 	input:
# 		transcripts_fa = GTF_TO_FASTA + "assembly_fasta.fa"
# 	# params:
# 	# 	index_out = directory(SALMON_DIR)
# 	output:
# 		out = directory(SALMON_DIR) # + "/gencode.v31.transcripts.index"
# 	shell:
# 		"salmon index -t {input.transcripts_fa} -i {output.out} -k 31"

rule salmon_quantify:
	input:
		index = SALMON_DIR, #+ "/gencode.v31.transcripts.index",
		R1 = FASTP_DIR + "{sample}R1.fastq",
		R2 = FASTP_DIR + "{sample}R2.fastq"
	output:
		quant_out = directory(SALMON_DIR + "/output/{sample}_quant")
	params:
		fastp_dir = FASTP_DIR,
		sample_id = "{sample}"
	run:
		shell("salmon quant -i {input.index} -l A -1 {input.R1} -2 {input.R2} \
		-o {output.quant_out} -p 18 --validateMappings \
		--numBootstraps 100 --seqBias --writeMappings")
		shell("find {params.fastp_dir} -type f ! -name '{params.sample_id}*' -delete")

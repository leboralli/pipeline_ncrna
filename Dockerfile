##################################
# Dockerfile for lncRNA pipeline
# Author: Msc. Leandro A F Boralli
#
#
##################################

FROM continuumio/miniconda3
MAINTAINER leboralli

WORKDIR /workdir
VOLUME /data

RUN apt-get update -y && apt-get upgrade -y
RUN apt-      get install -y \
  build-essential \
  unzip \
  bzip2 \
  subversion \
  libboost-dev \
  gfortran \
  nano \
  gzip

# RUN cd /home && mkdir downloads && cd downloads
# RUN wget https://dl.bintray.com/boostorg/release/1.70.0/source/boost_1_70_0.zip && \
#   unzip boost_1_70_0.zip
#
# RUN cd /home/downloads && \
#   wget https://zlib.net/zlib-1.2.11.tar.gz && \
#   tar -vzxf zlib-1.2.11.tar.gz && \
#   cd zlib-1.2.11/ && \
#   ./configure && \
#   make && \
#   make install
#
# RUN cd /home/downloads && \
#   wget https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2 && \
#   tar -jxvf htslib-1.9.tar.bz2 && \
#   cd htslib-1.9 && \
#   ./configure --disable-bz2 --disable-lzma --disable-gcs --disable-s3 --enable-libcurl=no && \
#   make && \
#   make install
#
# RUN cd /home/downloads && \
#   svn co https://projects.coin-or.org/svn/Clp/stable/1.16 coin-Clp && \
#   cd coin-Clp && \
#   ./configure --disable-bzlib --disable-zlib && \
#   make && \
#   make install && \
#   export LD_LIBRARY_PATH=/home/downloads/coin-Clp/lib:$LD_LIBRARY_PATH
#
# RUN cd /home/downloads && \
#   wget https://github.com/Kingsford-Group/scallop/releases/download/v0.10.3/scallop-0.10.3.tar.gz && \
#   tar -vzxf scallop-0.10.3.tar.gz && \
#   cd scallop-0.10.3 && \
#   ./configure --with-clp=/home/downloads/coin-Clp --with-boost=/home/downloads/boost_1_70_0 && \
#   make && \
#   export PATH=$PATH:/home/downloads/scallop-0.10.3/src

RUN conda install -c bioconda -c conda-forge \
  fastp \
  star \
  snakemake \
  rsem \
  feelnc \
  salmon \
  scallop

#RUN conda install -c r r
#RUN echo "install.packages(\"randomForest\", repos=\"https://cran.rstudio.com\")" | R --no-save && \
  # echo "install.packages(\"rhdf5\", repos=\"https://cran.rstudio.com\")" | R --no-save

RUN cd /home/downloads && \
  wget https://github.com/tacorna/taco/releases/download/v0.7.3/taco-v0.7.3.Linux_x86_64.tar.gz && \
  tar -vzxf taco-v0.7.3.Linux_x86_64.tar.gz && \
  export PATH=$PATH:/home/downloads/taco-v0.7.3.Linux_x86_64


COPY Snakefile /workdir
COPY config.py /workdir
COPY get_list_samples.py /workdir
COPY parameters.txt /workdir

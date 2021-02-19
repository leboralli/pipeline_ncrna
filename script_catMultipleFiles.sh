#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "Coloque pelo menos um ID"
fi

IDs=$#
echo "Numero de amostras = $IDs"

for i in $@; do
  echo "Amostra: $i"
  for n in $(ls | grep $i | grep R2); do cat $n >> "$n"_allLanes_R1.fastq.gz; done
  for n in $(ls | grep $i | grep R1); do cat $n >> "$n"_allLanes_R1.fastq.gz; done
  # echo "$i"_allLanes_R1
  # echo "$i"_allLanes_R2
done

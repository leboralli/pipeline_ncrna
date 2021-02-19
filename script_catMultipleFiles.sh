#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "Coloque pelo menos um ID"
fi

numero=$#
id=$1
echo "Testando $1"
echo "Numero de argumentos = $numero"

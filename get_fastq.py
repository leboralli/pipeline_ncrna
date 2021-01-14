# Script para criar lista dos arquivos fastq em determinada pasta
# Autor: Leandro Augusto Freire Boralli
import os
import re

def getListOfFastq(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # # Create full path
        # fullPath = os.path.join(dirName, entry)
        # # If entry is a directory then get the list of files in this directory
        # if os.path.isdir(fullPath):
        #     allFiles = allFiles + getListOfFastq(fullPath)
        # else:
        allFiles.append(entry)

    return allFiles

def dirName(workdir):
    workdirName = workdir
    return workdirName

# Get the list of all files in directory tree at given path
# listOfFiles = getListOfFastq(dirName())

def get_fastqFiles(data):
    fastqList = list()
    flat_list = list()
    # print(data)
    for arquivo in data:
        if 'fastq' in arquivo:
            # print(arquivo)
            # regexList = re.findall('.+L00\d_', arquivo)
            regexList = re.findall('.+allLanes_', arquivo)
            # print(regexList)
            fastqList.append(regexList)
            # print(fastqList)
    for sublista in fastqList:
        for item in sublista:
            flat_list.append(item)
    print (flat_list)
    return flat_list
# print(fastqList)

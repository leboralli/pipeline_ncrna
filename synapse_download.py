import synapseclient
import shutil, os
syn = synapseclient.Synapse()
syn.login('leboralli','Eriol0284*')

#list of samples
#controle
samples = ['syn8231683']

 # Obtain a pointer and download the data by loop
for i in samples:
    # syn8238085 = syn.get(entity='syn8238085')
    print (i)
    i = syn.get(entity = i)
 # Get the path to the local copy of the data file
    filepath = i.path
    shutil.move(filepath, "/home/boralli/workdir/data")

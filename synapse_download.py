import synapseclient
import shutil, os
syn = synapseclient.Synapse()
syn.login('leboralli','Eriol0284*')

#list of samples
#controle
samples = ['syn8239554', 'syn8239555', 'syn8231270', 'syn8231271',
            'syn8230808', 'syn8230810', 'syn8229813', 'syn8229817']

 # Obtain a pointer and download the data by loop
for i in samples:
    # syn8238085 = syn.get(entity='syn8238085')
    print (i)
    i = syn.get(entity = i)
 # Get the path to the local copy of the data file
    filepath = i.path
    shutil.move(filepath, "/home/boralli/workdir/data")

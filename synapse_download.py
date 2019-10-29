import synapseclient
import shutil
syn = synapseclient.Synapse()
syn.login('leboralli','Eriol0284*')

#list of samples
#controle
# samples = ['syn8239554', 'syn8239555', 'syn8231270', 'syn8231271',
#             'syn8230808', 'syn8230810', 'syn8229813', 'syn8229817']
# samples_file = open("/home/boralli/workdir/data/list_samples.txt", "r")
# samples_read = samples_file.read()
 # Obtain a pointer and download the data by loop
with open("/home/boralli/workdir/data/list_samples.txt", "r") as f:
    for line in f:
    # syn8238085 = syn.get(entity='syn8238085')
        print (line)
        i = syn.get(entity = line)
     # Get the path to the local copy of the data file
        filepath = i.path
        shutil.move(filepath, "/home/boralli/workdir/data")

import synapseclient

syn = synapseclient.Synapse()
syn.login('leboralli','Eriol0284*')

#list of samples
samples = ['syn8238085', 'syn8238091', 'syn8230825', 'syn8230829',
            'syn8234562', 'syn8234563', 'syn8232353', 'syn8232354',
            'syn8229041', 'syn8229087']

 # Obtain a pointer and download the data by loop
for i in samples:
    # syn8238085 = syn.get(entity='syn8238085')
    print (i)
    i = syn.get(entity = i)
 # Get the path to the local copy of the data file
    # filepath = i.path

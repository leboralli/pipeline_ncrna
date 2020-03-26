import synapseclient
import shutil
syn = synapseclient.Synapse()
syn.login('leboralli','Eriol0284*')

#list of samples
#controle
# samples = ['syn8241621', 'syn8241622', 'syn8231515', 'syn8231516', 'syn8229621',
#            'syn8229622', 'syn8231026', 'syn8231032', 'syn8232245', 'syn8232249',
#            'syn8231735', 'syn8231736', 'syn8228259', 'syn8228263', 'syn8231564',
#            'syn8231565', 'syn8234601', 'syn8234606', 'syn8234388', 'syn8234392',
#            'syn8239833', 'syn8239835', 'syn8238853', 'syn8238855', 'syn8231340',
#            'syn8231341', 'syn8231288', 'syn8231293', 'syn8228250', 'syn8228252',
#            'syn8228173', 'syn8228179', 'syn8232765', 'syn8232777', 'syn8239312',
#            'syn8239326', 'syn8232140', 'syn8232143', 'syn8231207', 'syn8231208',
#            'syn8229705', 'syn8229707', 'syn8229339', 'syn8229367', 'syn8229434',
#            'syn8229445', 'syn8238697', 'syn8238698', 'syn8238287', 'syn8238291',
#            'syn8230523', 'syn8230529', 'syn8228450', 'syn8228459', 'syn8238215',
#            'syn8238216', 'syn8237787', 'syn8237798', 'syn8234414', 'syn8234420',
#            'syn8231114', 'syn8231118', 'syn8232866', 'syn8232874', 'syn8231110',
#            'syn8231111', 'syn8231238', 'syn8231239', 'syn8231976', 'syn8231989',
#            'syn8235550', 'syn8235557', 'syn8230315', 'syn8230321', 'syn8238729',
#            'syn8238730', 'syn8234191', 'syn8234195', 'syn8238878', 'syn8238879',
#            'syn8238676', 'syn8238677', 'syn8229611', 'syn8229613', 'syn8238763',
#            'syn8238767']
# samples = [ 'syn8238287', 'syn8238291',
#             'syn8230523', 'syn8230529', 'syn8228450', 'syn8228459',
#             'syn8238215', 'syn8238216', 'syn8237787', 'syn8237798',
#             'syn8234414', 'syn8234420', 'syn8231114', 'syn8231118',
#             'syn8232866', 'syn8232874', 'syn8231110', 'syn8231111',
#             'syn8231238', 'syn8231239', 'syn8231976', 'syn8231989',
#             'syn8235550', 'syn8235557', 'syn8230315', 'syn8230321',
#             'syn8238729', 'syn8238730', 'syn8234191', 'syn8234195',
#             'syn8238878', 'syn8238879', 'syn8238676', 'syn8238677',
#             'syn8229611', 'syn8229613', 'syn8238763', 'syn8238767']

samples = ['syn8230524']
# samples_file = open("/home/boralli/workdir/data/list_samples.txt", "r")
# samples_read = samples_file.read()
 # Obtain a pointer and download the data by loop
# with open("/home/boralli/workdir/data/list_samples.txt", "r") as f:
for i in samples:
    # syn8238085 = syn.get(entity='syn8238085')
        print (i)
        i = syn.get(entity = i)
     # Get the path to the local copy of the data file
        filepath = i.path
        shutil.move(filepath, "/home/boralli/workdir/data")

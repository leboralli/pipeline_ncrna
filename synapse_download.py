import synapseclient
import shutil
syn = synapseclient.Synapse()
syn.login('leboralli','Eriol0284*')

#list of samples
#controle
#
samples_scz = ['syn8229621', 'syn8229622', 'syn8232245', 'syn8232249',
            'syn8231270', 'syn8231271', 'syn8231288', 'syn8231293',
            'syn8228250', 'syn8228252', 'syn8230523', 'syn8230529',
            'syn8231976', 'syn8231989', 'syn8234191', 'syn8234195',
            'syn8229611', 'syn8229613', 'syn8231265', 'syn8231269',
            'syn8233132', 'syn8233139', 'syn8229651', 'syn8229656',
            'syn8230776', 'syn8230777', 'syn8230697', 'syn8230698',
            'syn8228780', 'syn8228824', 'syn8228115', 'syn8228119',
            'syn8228480', 'syn8228498', 'syn8230097', 'syn8230113',
            'syn8231517', 'syn8231518', 'syn8230338', 'syn8230339',
            'syn8232100', 'syn8232101', 'syn8233179', 'syn8233180',
            'syn8231744', 'syn8231748', 'syn8229772', 'syn8229773',
            'syn8233100', 'syn8233103', 'syn8231190', 'syn8231194',
            'syn8231990', 'syn8231991', 'syn8228374', 'syn8228376',
            'syn8228330', 'syn8228337', 'syn8231897', 'syn8231898',
            'syn8231919', 'syn8231920', 'syn8231926', 'syn8231931',
            'syn8231650', 'syn8231651', 'syn8228425', 'syn8228437',
            'syn8231170', 'syn8231174', 'syn8229862', 'syn8229863',
            'syn8229559', 'syn8229560', 'syn8230376', 'syn8230377',
            'syn8231710', 'syn8231711', 'syn8228575', 'syn8228578',
            'syn8231690', 'syn8231693', 'syn8232844', 'syn8232845',
            'syn8229587', 'syn8229588', 'syn8231342', 'syn8231346',
            'syn8229472', 'syn8229478', 'syn8230345', 'syn8230346',
            'syn8231618', 'syn8231622', 'syn8229918', 'syn8229919',
            'syn8234426', 'syn8234433', 'syn8234528', 'syn8234530' ]
samples_control = ['syn8228540', 'syn8228541', 'syn8231050', 'syn8231051',
                    'syn8228259', 'syn8228263', 'syn8228173', 'syn8228179',
                    'syn8229813', 'syn8229817', 'syn8231207', 'syn8231208',
                    'syn8229339', 'syn8229367', 'syn8229434', 'syn8229445',
                    'syn8231114', 'syn8231118', 'syn8231110', 'syn8231111',
                    'syn8228295', 'syn8228301', 'syn8229902', 'syn8229903',
                    'syn8230372', 'syn8230373', 'syn8230814', 'syn8230815',
                    'syn8230758', 'syn8230762', 'syn8229674', 'syn8229682',
                    'syn8229788', 'syn8229792', 'syn8230400', 'syn8230401',
                    'syn8230580', 'syn8230584', 'syn8230510', 'syn8230511',
                    'syn8228585', 'syn8228587', 'syn8228094', 'syn8228095',
                    'syn8230557', 'syn8230561', 'syn8227862', 'syn8227863',
                    'syn8230333', 'syn8230337', 'syn8231075', 'syn8231076',
                    'syn8230753', 'syn8230757', 'syn8230923', 'syn8230927',
                    'syn8228551', 'syn8228557', 'syn8229822', 'syn8229823',
                    'syn8229575', 'syn8229579', 'syn8229623', 'syn8229624',
                    'syn8228913', 'syn8228927', 'syn8231039', 'syn8231043',
                    'syn8230885', 'syn8230886', 'syn8230611', 'syn8230618',
                    'syn8230426', 'syn8230428', 'syn8230646', 'syn8230649',
                    'syn8228000', 'syn8228008', 'syn8229749', 'syn8229756',
                    'syn8230603', 'syn8230607', 'syn8228121', 'syn8228124',
                    'syn8230686', 'syn8230691', 'syn8230429', 'syn8230430',
                    'syn8230307', 'syn8230308', 'syn8230436', 'syn8230437',
                    'syn8230669', 'syn8230670', 'syn8230497', 'syn8230498',
                    'syn8230778', 'syn8230779', 'syn8229295', 'syn8229301',
                    'syn8231227', 'syn8231228', 'syn8228338', 'syn8228342',
                    'syn8231372', 'syn8231374', 'syn8231277', 'syn8231280',
                    'syn8228045', 'syn8228046', 'syn8229546', 'syn8229547',
                    'syn8229683', 'syn8229687', 'syn8230724', 'syn8230725',
                    'syn8229849', 'syn8229853', 'syn8231321', 'syn8231322',
                    'syn8230472', 'syn8230473', 'syn8230410', 'syn8230411',
                    'syn8231353', 'syn8231358', 'syn8231087', 'syn8231088',
                    'syn8230234', 'syn8230252', 'syn8231124', 'syn8231129',
                    'syn8231070', 'syn8231071', 'syn8228026', 'syn8228028',
                    'syn8229884', 'syn8229891', 'syn8228201', 'syn8228202',
                    'syn8229702', 'syn8229704', 'syn8229219', 'syn8229275',
                    'syn8230910', 'syn8230914', 'syn8231019', 'syn8231020',
                    'syn8228439', 'syn8228447', ]
# samples_file = open("/home/boralli/workdir/data/list_samples.txt", "r")
# samples_read = samples_file.read()
 # Obtain a pointer and download the data by loop
# with open("/home/boralli/workdir/data/list_samples.txt", "r") as f:

samples_single = ['syn8228123']
for i in samples_scz:
    # syn8238085 = syn.get(entity='syn8238085')
        print (i)
        i = syn.get(entity = i)
     # Get the path to the local copy of the data file
        filepath = i.path
        shutil.move(filepath, "/home3/boralli/workdir/data")

for i in samples_control:
    # syn8238085 = syn.get(entity='syn8238085')
        print (i)
        i = syn.get(entity = i)
     # Get the path to the local copy of the data file
        filepath = i.path
        shutil.move(filepath, "/home3/boralli/workdir/data")

for i in samples_single:
    # syn8238085 = syn.get(entity='syn8238085')
        print (i)
        i = syn.get(entity = i)
     # Get the path to the local copy of the data file
        filepath = i.path
        shutil.move(filepath, "/home3/boralli/workdir/data")

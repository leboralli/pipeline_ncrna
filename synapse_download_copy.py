import synapseclient
import shutil
syn = synapseclient.Synapse()
syn.login('leboralli','Eriol0284*')

'''
Amostras já analisadas:
SCZ
syn8232245, syn8232249, syn8231735, syn8231736, syn8232765, syn8232777,
syn8229813, syn8229817, syn8234414, syn8234420, syn8232866, syn8232874,
syn8231976, syn8231989, syn8238878, syn8238879, syn8231265, syn8231269,
syn8232562, syn8232575, syn8231971, syn8231972, syn8230776, syn8230777,
syn8230333, syn8230337, syn8231758, syn8231759, syn8239549, syn8239553,
syn8233046, syn8233052, syn8230611, syn8230618, syn8230426, syn8230428,
syn8239247, syn8239254, syn8230603, syn8230607, syn8234189, syn8234190,
syn8234155, syn8234163, syn8231708, syn8231709, syn8231372, syn8231374,
syn8233084, syn8233094, syn8229862, syn8229863, syn8239224, syn8239225,
syn8231070, syn8231071, syn8235393, syn8235401, syn8238712, syn8238716
syn8234552, syn8234553

29/06/2020
syn8238085, syn8238091, syn8241621, syn8241622, syn8229621, syn8229622,
syn8231270, syn8231271, syn8239833, syn8239835, syn8238853, syn8238855,
syn8231288, syn8231289, syn8228250, syn8228252, syn8238429, syn8238430

02/07/2020

'syn8238287', 'syn8238291', 'syn8230523', 'syn8230524',
                'syn8237787', 'syn8237798',
                'syn8234191', 'syn8234195', 'syn8229611', 'syn8229613',
                'syn8235667', 'syn8235668', 'syn8234971', 'syn8234998',
                'syn8233132', 'syn8233139',
                'syn8239762', 'syn8239763',
                'syn8230697', 'syn8230698', 'syn8228780', 'syn8228824',
                'syn8228480', 'syn8228498', 'syn8238486', 'syn8238487',
                'syn8230097', 'syn8230113', 'syn8231517', 'syn8231518'


04/07/2020
'syn8230338', 'syn8230339',
                'syn8239342', 'syn8239345', 'syn8232100', 'syn8232101',
                'syn8234792', 'syn8234793', 'syn8233179', 'syn8233180',
                'syn8231744', 'syn8231748', 'syn8229772', 'syn8229773',
                'syn8234707', 'syn8234711', 'syn8233100', 'syn8233103',
                'syn8235648', 'syn8235649', 'syn8231990', 'syn8231991',
                'syn8228374', 'syn8228376', 'syn8228330', 'syn8228337',
                'syn8231897', 'syn8231898', 'syn8238181', 'syn8238182'

09/07/2020
'syn8231926', 'syn8231931', 'syn8231650', 'syn8231651',
                'syn8228425', 'syn8228437',
                'syn8229559', 'syn8229560', 'syn8230376', 'syn8230377',
                'syn8231710', 'syn8231711', 'syn8231690', 'syn8231693',
                'syn8232844', 'syn8232845', 'syn8229587', 'syn8229588',
                'syn8231342', 'syn8231346', 'syn8229472', 'syn8229478',
                'syn8230345', 'syn8230346', 'syn8231618', 'syn8231622',
                'syn8238398', 'syn8238399',
                'syn8229918', 'syn8229919', 'syn8234426', 'syn8234433',
                'syn8234528', 'syn8234530', 'syn8238640', 'syn8238641',
                'syn8238989', 'syn8238996'

Controle:
13/07/2020
'syn8232353', 'syn8232354', 'syn8228530', 'syn8228531',
                    'syn8238294', 'syn8238298', 'syn8231050', 'syn8231051',
                    'syn8228259', 'syn8228263',
                    'syn8234601', 'syn8234606', 'syn8234388', 'syn8234392',
                    'syn8228173', 'syn8228179',
                    'syn8229339', 'syn8229367', 'syn8229434', 'syn8229445',
                    'syn8238697', 'syn8238698', 'syn8228450', 'syn8228459',
                    'syn8231110', 'syn8231111',
                    'syn8238842', 'syn8238843', 'syn8238336', 'syn8238337',
                    'syn8231403', 'syn8231404', 'syn8229902', 'syn8229903',
                    'syn8238185', 'syn8238189', 'syn8230814', 'syn8230815',
                    'syn8230758', 'syn8230762', 'syn8229674', 'syn8229682',
                    'syn8229788', 'syn8229792', 'syn8234164', 'syn8234168',
                    'syn8228585', 'syn8228587', 'syn8232384', 'syn8232391'

17/07/2020
'syn8228094', 'syn8228095', 'syn8238321', 'syn8238322',
                    'syn8232509', 'syn8232512',
                    'syn8228551', 'syn8228557',
                    'syn8231496', 'syn8231497', 'syn8241377', 'syn8241515',
                    'syn8238246', 'syn8238247', 'syn8231575', 'syn8231576',
                    'syn8232068', 'syn8232072', 'syn8235451', 'syn8235452',
                    'syn8234890', 'syn8234898', 'syn8238662', 'syn8238663',
                    'syn8230646', 'syn8230649',
                    'syn8234136', 'syn8234139',
                    'syn8229749', 'syn8229756',
                    'syn8236092', 'syn8236142',
                    'syn8228121', 'syn8228123', 'syn8230686', 'syn8230687',
                    'syn8229720', 'syn8229721', 'syn8239327', 'syn8239328',
                    'syn8230429', 'syn8230430', 'syn8230307', 'syn8230308',
                    'syn8230436', 'syn8230437', 'syn8230497', 'syn8230498',
                    'syn8231530', 'syn8231537',
                    'syn8239093', 'syn8239094', 'syn8231436', 'syn8231437',
                    'syn8232155', 'syn8232159',
                    'syn8228338', 'syn8228342',
'''


samples_scz = [ ]

samples_control = [ 'syn8232222', 'syn8232223', 'syn8235341', 'syn8235346',
                    'syn8234480', 'syn8234486', 'syn8239706', 'syn8239708',
                    'syn8232080', 'syn8232081', 'syn8229546', 'syn8229547',
                    'syn8235139', 'syn8235180', 'syn8229849', 'syn8229853',
                    'syn8231321', 'syn8231322', 'syn8230472', 'syn8230473',
                    'syn8235779', 'syn8235818',
                    'syn8230410', 'syn8230411', 'syn8235511', 'syn8235512',
                    'syn8231353', 'syn8231358',
                    'syn8231087', 'syn8231088',
                    'syn8229884', 'syn8229891', 'syn8239382', 'syn8239388',
                    'syn8238914', 'syn8238918', 'syn8228201', 'syn8228202',
                    'syn8229702', 'syn8229704', 'syn8231754', 'syn8231755',
                    'syn8235480', 'syn8235481',
                    'syn8228439', 'syn8228447',
                    'syn8232734', 'syn8232736', 'syn8234722', 'syn8234724',
                    'syn8228154', 'syn8228159']
# samples_file = open("/home/boralli/workdir/data/list_samples.txt", "r")
# samples_read = samples_file.read()
 # Obtain a pointer and download the data by loop
# with open("/home/boralli/workdir/data/list_samples.txt", "r") as f:

samples_n = ['syn8228094', 'syn8228095', 'syn8238321', 'syn8238322',
                    'syn8232509', 'syn8232512',
                    'syn8228551', 'syn8228557',
                    'syn8231496', 'syn8231497', 'syn8241377', 'syn8241515',
                    'syn8238246', 'syn8238247', 'syn8231575', 'syn8231576',
                    'syn8232068', 'syn8232072', 'syn8235451', 'syn8235452',
                    'syn8234890', 'syn8234898', 'syn8238662', 'syn8238663',
                    'syn8230646', 'syn8230649',
                    'syn8234136', 'syn8234139',
                    'syn8229749', 'syn8229756',
                    'syn8236092', 'syn8236142',
                    'syn8228121', 'syn8228123', 'syn8230686', 'syn8230687',
                    'syn8229720', 'syn8229721', 'syn8239327', 'syn8239328',
                    'syn8230429', 'syn8230430', 'syn8230307', 'syn8230308',
                    'syn8230436', 'syn8230437', 'syn8230497', 'syn8230498',
                    'syn8231530', 'syn8231537',
                    'syn8239093', 'syn8239094', 'syn8231436', 'syn8231437',
                    'syn8232155', 'syn8232159',
                    'syn8228338', 'syn8228342']
# for i in samples_scz:
#     # syn8238085 = syn.get(entity='syn8238085')
#         print (i)
#         i = syn.get(entity = i)
#      # Get the path to the local copy of the data file
#         filepath = i.path
#         # shutil.move(filepath, "/homelocal/boralli/workdir/data") #ngs
#         shutil.move(filepath, "/mnt/disks/sba1/data")
#
# for i in samples_control:
#     # syn8238085 = syn.get(entity='syn8238085')
#         print (i)
#         i = syn.get(entity = i)
#      # Get the path to the local copy of the data file
#         filepath = i.path
#         # shutil.move(filepath, "/homelocal/boralli/workdir/data") #ngs
#         shutil.move(filepath, "/mnt/disks/sba1/data")
#
for i in samples_n:
    # syn8238085 = syn.get(entity='syn8238085')
        print (i)
        i = syn.get(entity = i)
     # Get the path to the local copy of the data file
        filepath = i.path
        shutil.move(filepath, "/home/boralli/workdir/data")

f = open('bitburnerSave_cracked_open.json', 'r')
data = f.read()
f.close()

import base64

dcdata = base64.b64decode(data).decode('utf-8')
# nldata = data.replace(';',';\n')
# print(data[:500])
# print(dcdata[:500])

srstr = 'rank'
printpad = 95


# old_ = '\\"TimeCompression\\"'
# new_ = '\\"TimeCompression\\",\\"RealityAlteration\\",\\"N00dles\\",\\"Bypass\\",\\"PrototypeTampering\\",\\"Unclickable\\",\\"UndocumentedFunctionCall\\",\\"N00dles\\"'
# dcdata = dcdata.replace(old_, new_, 1)

# allaugs = ['Augmented Targeting I', 'Augmented Targeting II', 'Augmented Targeting III', 'Synthetic Heart', 'Synfibril Muscle', 'Combat Rib I', 'Combat Rib II', 'Combat Rib III', 'Nanofiber Weave', 'NEMEAN Subdermal Weave', 'Wired Reflexes', 'Graphene Bone Lacings', 'Bionic Spine', 'Graphene Bionic Spine Upgrade', 'Bionic Legs', 'Graphene Bionic Legs Upgrade', 'Speech Processor Implant', 'TITN-41 Gene-Modification Injection', 'Enhanced Social Interaction Implant', 'BitWire', 'Artificial Bio-neural Network Implant', 'Artificial Synaptic Potentiation', 'Enhanced Myelin Sheathing', 'Synaptic Enhancement Implant', 'Neural-Retention Enhancement', 'DataJack', 'Embedded Netburner Module', 'Embedded Netburner Module Core Implant', 'Embedded Netburner Module Core V2 Upgrade', 'Embedded Netburner Module Core V3 Upgrade', 'Embedded Netburner Module Analyze Engine', 'Embedded Netburner Module Direct Memory Access Upgrade', 'Neuralstimulator', 'Neural Accelerator', 'Cranial Signal Processors - Gen I', 'Cranial Signal Processors - Gen II', 'Cranial Signal Processors - Gen III', 'Cranial Signal Processors - Gen IV', 'Cranial Signal Processors - Gen V', 'Neuronal Densification', 'Neuroreceptor Management Implant', 'Nuoptimal Nootropic Injector Implant', 'Speech Enhancement', 'FocusWire', 'PC Direct-Neural Interface', 'PC Direct-Neural Interface Optimization Submodule', 'PC Direct-Neural Interface NeuroNet Injector', 'PCMatrix', 'ADR-V1 Pheromone Gene', 'ADR-V2 Pheromone Gene', "The Shadow's Simulacrum", 'Hacknet Node CPU Architecture Neural-Upload', 'Hacknet Node Cache Architecture Neural-Upload', 'Hacknet Node NIC Architecture Neural-Upload', 'Hacknet Node Kernel Direct-Neural Interface', 'Hacknet Node Core Direct-Neural Interface', 'NeuroFlux Governor', 'Neurotrainer I', 'Neurotrainer II', 'Neurotrainer III', 'HyperSight Corneal Implant', 'LuminCloaking-V1 Skin Implant', 'LuminCloaking-V2 Skin Implant', 'HemoRecirculator', 'SmartSonar Implant', 'Power Recirculation Core', 'QLink', 'The Red Pill', 'SPTN-97 Gene Modification', 'ECorp HVMind Implant', 'CordiARC Fusion Reactor', 'SmartJaw', 'Neotra', 'Xanipher', 'nextSENS Gene Modification', 'OmniTek InfoLoad', 'Photosynthetic Cells', 'BitRunners Neurolink', 'The Black Hand', 'Unstable Circadian Modulator', 'CRTX42-AA Gene Modification', 'Neuregen Gene Modification', 'CashRoot Starter Kit', 'NutriGen Implant', 'INFRARET Enhancement', 'DermaForce Particle Barrier', 'Graphene BrachiBlades Upgrade', 'Graphene Bionic Arms Upgrade', 'BrachiBlades', 'Bionic Arms', 'Social Negotiation Assistant (S.N.A)', 'Hydroflame Left Arm', 'EsperTech Bladeburner Eyewear', 'EMS-4 Recombination', 'ORION-MKIV Shoulder', 'Hyperion Plasma Cannon V1', 'Hyperion Plasma Cannon V2', 'GOLEM Serum', 'Vangelis Virus', 'Vangelis Virus 3.0', 'I.N.T.E.R.L.I.N.K.E.D', "Blade's Runners", 'BLADE-51b Tesla Armor', 'BLADE-51b Tesla Armor: Power Cells Upgrade', 'BLADE-51b Tesla Armor: Energy Shielding Upgrade', 'BLADE-51b Tesla Armor: Unibeam Upgrade', 'BLADE-51b Tesla Armor: Omnibeam Upgrade', 'BLADE-51b Tesla Armor: IPU Upgrade', "The Blade's Simulacrum", "Stanek's Gift - Genesis", "Stanek's Gift - Awakening", "Stanek's Gift - Serenity"]
# newaugs = []
#
# for aug in allaugs:
#     if dcdata.count(aug,0,26700) == 0:
#         newaugs.append(aug)

# print(newaugs)
# templatestrt = ',{\\"name\\":\\"'
# templateendd = '\\",\\"level\\":1}'
# suffix = ''
# for aug in newaugs:
#     suffix += templatestrt + aug + templateendd
#
# old_ = '{\\"name\\":\\"NeuroFlux Governor\\",\\"level\\":84}'
# new_ = '{\\"name\\":\\"NeuroFlux Governor\\",\\"level\\":254}' + suffix
# dcdata = dcdata.replace(old_, new_, 1)
#
# old_ = 'Daedalus\\"],\\"queuedAugmentations\\":[]'
# new_ = 'Daedalus\\"],\\"queuedAugmentations\\":[{\\"name\\":\\"NeuroFlux Governor\\",\\"level\\":255}]'
# dcdata = dcdata.replace(old_, new_, 1)


# dcdata = dcdata.replace(':18625971239102820,', ':18625971239102820000000000000,')
# dcdata = dcdata.replace('4.102139913677849e+22', '1.335599906176118e+74')
# dcdata = dcdata.replace('[537,8,9,7,8,8,8,8,8,8]', '[44000,8,9,7,8,8,8,8,8,8]')
# dcdata = dcdata.replace('[17.11,1.8,1.009,1.035,1.8,1.8,', '[9000.01,1.8,1.009,1.035,1.8,1.8,')
# dcdata = dcdata.replace('6.140419461861013', '6140.419461861013')
# dcdata = dcdata.replace('"qty\\":0,', '"qty\\":400000000000000,')
# dcdata = dcdata.replace('1470}}', '14700}}')
# dcdata = dcdata.replace('"lvl\\":7,\\"n\\":12','"lvl\\":128,\\"n\\":12')
# dcdata = dcdata.replace('skillPoints\\":58','skillPoints\\":5800000')
# dcdata = dcdata.replace('Overclock\\":17','Overclock\\":90')
dcdata = dcdata.replace('32015.037092999737','32015037.092999737')


idx = dcdata.find(srstr)
while idx > 0:
    print(f'#### chr index is {idx} ####')
    print(dcdata[idx-printpad:idx+printpad])
    # print(nldata[:idx *2 ])
    idx += 1
    idx = dcdata.find(srstr, idx)
    # idx = -1

# print(dcdata[7770:9001])

newdata = base64.b64encode(bytes(dcdata, 'utf-8'))

f = open('bitburnerSave_cracked_open_and_rifled.json', 'wb')
f.write(newdata)
f.close()

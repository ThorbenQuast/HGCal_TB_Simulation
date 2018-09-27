import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

 
beamprofiles = {
    1: {    #configuration index: September 2017
        11: {   #particle ID
            80: {   #energy
                "type": "Flat",
                "minX": -2.0,
                "maxX": 2.0,
                "minY": -2.0,
                "maxY": 2.0,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            },
            200: {   #energy
                "type": "Flat",
                "minX": -2.0,
                "maxX": 2.0,
                "minY": -2.0,
                "maxY": 2.0,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            }
        },
        13: {   #particle ID
            150: {   #energy
                "type": "Flat",
                "minX": -2.0,
                "maxX": 2.0,
                "minY": -2.0,
                "maxY": 2.0,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            }
        },
        211: {  #particle ID
            100: {  #energy
                "type": "Flat",
                "minX": -2.0,
                "maxX": 2.0,
                "minY": -2.0,
                "maxY": 2.0,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            },
            150: {  #energy
                "type": "Gauss",
                "meanX": 0.,
                "sigmaX": 1.8,
                "meanY": 0.5,
                "sigmaY": 1.0,
                #"meanZ": 1095., #for v3 to test impact of upstream material in beam line 
                "meanZ": -800.00000, 
                #"sigmaZ": 0.00001 #for v3 to test impact of upstream material in beam line
                "sigmaZ": 0.000003
            },
            200: {  #energy
                "type": "Gauss",
                "meanX": 0.,
                "sigmaX": 1.1,
                "meanY": 0.4,
                "sigmaY": 1.1,
                #"meanZ": 1095., #for v3 to test impact of upstream material in beam line 
                "meanZ": -800.00000, 
                #"sigmaZ": 0.00001 #for v3 to test impact of upstream material in beam line
                "sigmaZ": 0.000003
            },
            250: {  #energy
                "type": "Gauss",
                "meanX": 0.2,
                "sigmaX": 1.9,
                "meanY": 0.3,
                "sigmaY": 2.1,
                #"meanZ": 1095., #for v3 to test impact of upstream material in beam line 
                "meanZ": -800.00000, 
                #"sigmaZ": 0.00001 #for v3 to test impact of upstream material in beam line
                "sigmaZ": 0.000003
            },
            300: {  #energy
                "type": "Flat",
                "minX": -2.0,
                "maxX": 2.0,
                "minY": -2.0,
                "maxY": 2.0,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            }
        }
    },
    2: {    #configuration index: September 2017
        11: {   #particle ID
            20: {   #energy
                "type": "Flat",
                "minX": -2.8,   #cm!
                "maxX": 3.4,
                "minY": -2.8,
                "maxY": 2.4,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            },
            32: {   #energy
                "type": "Flat",
                "minX": -2.8,
                "maxX": 3.4,
                "minY": -2.8,
                "maxY": 2.4,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            },
            50: {   #energy
                "type": "Flat",
                "minX": -2.8,
                "maxX": 3.4,
                "minY": -2.8,
                "maxY": 2.4,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            },
            80: {   #energy
                "type": "Flat",
                "minX": -2.8,
                "maxX": 3.4,
                "minY": -2.8,
                "maxY": 2.4,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            },
            90: {   #energy
                "type": "Flat",
                "minX": -2.8,
                "maxX": 3.6,
                "minY": -2.8,
                "maxY": 2.4,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            },
            70: {   #Energy, used for evaluation of GAN study, T.Q. 30 April 2018
                "type": "Flat",
                "minX": -3.,
                "maxX": 3.0,
                "minY": -3.0,
                "maxY": 3.0,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            },
            100: {   #Energy, used for evaluation of GAN study, T.Q. 30 April 2018
                "type": "Flat",
                "minX": -3.,
                "maxX": 3.0,
                "minY": -3.0,
                "maxY": 3.0,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            },      
            5: {   #Energy, used for further evaluation of WGAN study, T.Q. 27 September 2018
                "type": "Flat",
                "minX": -3.,
                "maxX": 3.0,
                "minY": -3.0,
                "maxY": 3.0,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            },
            10: {   #Energy, used for further evaluation of WGAN study, T.Q. 27 September 2018
                "type": "Flat",
                "minX": -3.,
                "maxX": 3.0,
                "minY": -3.0,
                "maxY": 3.0,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            },
            55: {   #Energy, used for further evaluation of WGAN study, T.Q. 27 September 2018
                "type": "Flat",
                "minX": -3.,
                "maxX": 3.0,
                "minY": -3.0,
                "maxY": 3.0,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            },  
            65: {   #Energy, used for further evaluation of WGAN study, T.Q. 27 September 2018
                "type": "Flat",
                "minX": -3.,
                "maxX": 3.0,
                "minY": -3.0,
                "maxY": 3.0,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            }              
        },
        211: {  #particle ID
            100: {  #energy
                "type": "Flat",
                "minX": -2.4,
                "maxX": 3.6,
                "minY": -2.8, 
                "maxY": 2.4,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            },
            150: {  #energy
                "type": "Flat",
                "minX": -2.5,
                "maxX": 1.6,
                "minY": -0.2, 
                "maxY": 2.2,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            },
            200: {  #energy
                "type": "Flat",
                "minX": -2.8, 
                "maxX": 0.6,
                "minY": -2.8,
                "maxY": 2.2,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            },
            250: {  #energy
                "type": "Gauss",
                "meanX": -1.1,
                "sigmaX": 2.2,
                "meanY": 0.1,
                "sigmaY": 1.9,
                #"meanZ": 1095., #for v3 to test impact of upstream material in beam line 
                "meanZ": -800.00000, 
                #"sigmaZ": 0.00001 #for v3 to test impact of upstream material in beam line
                "sigmaZ": 0.000003
            },
            300: {  #energy
                "type": "Flat",
                "minX": -2.8,
                "maxX": 3.0,
                "minY": -2.8,
                "maxY": 2.0,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            },
            350: {  #energy
                "type": "Flat",
                "minX": -2.8,
                "maxX": 2.0,
                "minY": -0.8,
                "maxY": 1.0,
                #"minZ": 1094.99999, #for v3 to test impact of upstream material in beam line
                "minZ": -800.00001,  
                #"maxZ": 1095.000001 #for v3 to test impact of upstream material in beam line
                "maxZ": -799.99999
            }
        },
        13: {   #particle ID
            150: {  #energy
                "type": "Gauss",
                "meanX": -1.0,
                "sigmaX": 1.3,
                "meanY": 0.1,
                "sigmaY": 1.9,
                #"meanZ": 1095., #for v3 to test impact of upstream material in beam line 
                "meanZ": -800.00000, 
                #"sigmaZ": 0.00001 #for v3 to test impact of upstream material in beam line
                "sigmaZ": 0.000003
            }
        }
    }
}

beamprofiles[1][2212] = beamprofiles[1][211]
beamprofiles[2][11][250] = beamprofiles[2][211][250]
beamprofiles[2][211][50] = beamprofiles[2][11][50]
beamprofiles[2][211][80] = beamprofiles[2][11][80]
beamprofiles[2][211][90] = beamprofiles[2][11][90]
beamprofiles[2][13][250] = beamprofiles[2][211][250]
beamprofiles[2][2212] = beamprofiles[2][211]

options = VarParsing.VarParsing('standard')

options.register('outputFolder',
                 '/sshfs_lxPlus/tmp/',
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 'Directory to which the files are being written.')

options.register('outputPostfix',
                 '',
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 'File postfix, should be unique for each file.')

options.register('NEvents',
                 100,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 'Number of events to be generated')

options.register('setupConfiguration',
                1,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 'setupConfiguration (0: September 2016, 1: July - 4: 20 Layers in October in H6A".'
                )

options.register('Energy',
                 200.,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 'Electron energy +/- EnergyWidth'
                )

options.register('EnergyWidth',
                 1.,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.float,
                 'Spread of the energy'
                )

options.register('physicsList',
                 'FTFP_BERT_EMM',
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 'PhysicsList to be used')

options.register('PDGID',
                 11,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 'Particle ID of the incident particle whose shower is to be simulated'
                )

options.register('RandomSeed',
                 12345678,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 'RandomSeed for the generator. Important if same configuration is simulated multiple times.'
                )

options.parseArguments()



process = cms.Process('SIM')

# import of standard configurations
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
if options.setupConfiguration==1:
    process.load('SimG4CMS.HGCalTestBeam.HGCalTB170JulyXML_cfi')
elif options.setupConfiguration==2:
    process.load('SimG4CMS.HGCalTestBeam.HGCalTB170SepXML_cfi')
else:
    print "Setup configuration",options.setupConfiguration,"is not in simulation"
    from sys import exit
    exit()
    
process.load('Geometry.HGCalCommonData.hgcalNumberingInitialization_cfi')
process.load('Geometry.HGCalCommonData.hgcalParametersInitialization_cfi')
process.load('Configuration.StandardSequences.MagneticField_0T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
if beamprofiles[options.setupConfiguration][options.PDGID][options.Energy]["type"]=="Flat":
    process.load('IOMC.EventVertexGenerators.VtxSmearedFlat_cfi')
else:
    process.load('IOMC.EventVertexGenerators.VtxSmearedGauss_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('SimG4CMS.HGCalTestBeam.HGCalTBCheckGunPosition_cfi')
process.load('SimG4CMS.HGCalTestBeam.HGCalTBAnalyzer_cfi')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.NEvents)
)

if 'MessageLogger' in process.__dict__:
    process.MessageLogger.categories.append('HGCSim')
    process.MessageLogger.categories.append('HcalSim')
    process.MessageLogger.categories.append('ValidHGCal')

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('SingleMuonE200_cfi nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition


# Additional output definition
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('file:%s/TBGenSim_%s.root' % (options.outputFolder, options.outputPostfix))
                                   )

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

process.generator = cms.EDProducer("FlatRandomEThetaGunProducer",
    AddAntiParticle = cms.bool(False),
    PGunParameters = cms.PSet(
        MinE = cms.double(options.Energy-options.EnergyWidth),
        MaxE = cms.double(options.Energy+options.EnergyWidth),
        MinTheta = cms.double(0.0),
        MaxTheta = cms.double(0.0),
        MinPhi = cms.double(-3.14159265359),
        MaxPhi = cms.double(3.14159265359),
        PartID = cms.vint32(options.PDGID)
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('single muon E 100')
)


#definition of physics lists:
#http://grupo.us.es/geterus/images/pdf/ieav-ita-2014/L9b-ReferencePhysicsLists.pdf
physicsList = 'SimG4Core/Physics/%s' % options.physicsList    
print "Using as physics list: %s" % physicsList
print "Using initial seed: ", options.RandomSeed
process.g4SimHits.Physics.type = cms.string(physicsList)

process.g4SimHits.StackingAction.SaveFirstLevelSecondary = cms.untracked.bool(True)
process.g4SimHits.StackingAction.SaveAllPrimaryDecayProductsAndConversions = cms.untracked.bool(True)

process.RandomNumberGeneratorService.generator.initialSeed = cms.untracked.uint32(options.RandomSeed)
process.RandomNumberGeneratorService.VtxSmeared.initialSeed = cms.untracked.uint32(options.RandomSeed)


if beamprofiles[options.setupConfiguration][options.PDGID][options.Energy]["type"]=="Flat":
    process.VtxSmeared.MinZ = beamprofiles[options.setupConfiguration][options.PDGID][options.Energy]["minZ"]
    process.VtxSmeared.MaxZ = beamprofiles[options.setupConfiguration][options.PDGID][options.Energy]["maxZ"]
    process.VtxSmeared.MinX = beamprofiles[options.setupConfiguration][options.PDGID][options.Energy]["minX"]
    process.VtxSmeared.MaxX = beamprofiles[options.setupConfiguration][options.PDGID][options.Energy]["maxX"]
    process.VtxSmeared.MinY = beamprofiles[options.setupConfiguration][options.PDGID][options.Energy]["minY"]
    process.VtxSmeared.MaxY = beamprofiles[options.setupConfiguration][options.PDGID][options.Energy]["maxY"]
else:
    process.VtxSmeared.MeanY = beamprofiles[options.setupConfiguration][options.PDGID][options.Energy]["meanY"]
    process.VtxSmeared.MeanX = beamprofiles[options.setupConfiguration][options.PDGID][options.Energy]["meanX"]
    process.VtxSmeared.MeanZ = beamprofiles[options.setupConfiguration][options.PDGID][options.Energy]["meanZ"]
    process.VtxSmeared.SigmaX = beamprofiles[options.setupConfiguration][options.PDGID][options.Energy]["sigmaX"]
    process.VtxSmeared.SigmaY = beamprofiles[options.setupConfiguration][options.PDGID][options.Energy]["sigmaY"]
    process.VtxSmeared.SigmaZ = beamprofiles[options.setupConfiguration][options.PDGID][options.Energy]["sigmaZ"]

process.g4SimHits.HGCSD.RejectMouseBite = True
process.g4SimHits.HGCSD.RotatedWafer    = True
process.g4SimHits.Watchers = cms.VPSet(cms.PSet(
		HGCPassive = cms.PSet(
			LVNames = cms.vstring('HGCalEE','HGCalHE','HGCalAH', 'HGCalBeam', 'CMSE'),
			MotherName = cms.string('OCMS'),
			),
		type = cms.string('HGCPassive'),
		)
				       )


process.HGCalTBAnalyzer.DoDigis     = False
process.HGCalTBAnalyzer.DoRecHits   = False
process.HGCalTBAnalyzer.UseFH       = True
process.HGCalTBAnalyzer.UseBH       = True
process.HGCalTBAnalyzer.UseBeam     = True
process.HGCalTBAnalyzer.ZFrontEE    = 1110.0
process.HGCalTBAnalyzer.ZFrontFH    = 1172.3
process.HGCalTBAnalyzer.DoPassive   = True

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.gunfilter_step  = cms.Path(process.HGCalTBCheckGunPostion)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.analysis_step = cms.Path(process.HGCalTBAnalyzer)
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,
				process.genfiltersummary_step,
				process.simulation_step,
				process.gunfilter_step,
				process.analysis_step,
				process.endjob_step#,
				#process.RAWSIMoutput_step,
				)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 



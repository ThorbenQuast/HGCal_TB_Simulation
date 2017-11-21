import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

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
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('SimG4CMS.HGCalTestBeam.HGCalTB161Module8XML_cfi')    #September 2016 TB at CERN 20-250 GeV electrons, module 15X0
#process.load('SimG4CMS.HGCalTestBeam.HGCalTB161Module8V2XML_cfi')      #September 2016 TB at CERN 20-250 GeV electrons, module 27X0
process.load('Geometry.HGCalCommonData.hgcalNumberingInitialization_cfi')
process.load('Geometry.HGCalCommonData.hgcalParametersInitialization_cfi')
process.load('Configuration.StandardSequences.MagneticField_0T_cff')
process.load('Configuration.StandardSequences.Generator_cff')


#Gaussian distribution of vertices
if options.Energy in [20., 32.]:
    process.load('IOMC.EventVertexGenerators.VtxSmearedFlat_cfi')
else: 
    process.load('IOMC.EventVertexGenerators.VtxSmearedGauss_cfi')




#process.load('IOMC.EventVertexGenerators.VtxSmearedGauss_cfi')

process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('SimG4CMS.HGCalTestBeam.HGCalTBCheckGunPosition_cfi')
process.load('SimG4CMS.HGCalTestBeam.HGCalTBAnalyzer_cfi')


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.NEvents)
)

process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        HGCSim = cms.untracked.PSet(
            limit = cms.untracked.int32(-1)
        ),
    ),
    categories = cms.untracked.vstring('HGCSim'),
    destinations = cms.untracked.vstring('cout','cerr')
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('SingleElectronE1000_cfi nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Additional output definition
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('file:%s/TBGenSim_%s.root' % (options.outputFolder, options.outputPostfix))
                                   )

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

# Gaussian momentum distribution of incoming particle guns
process.generator = cms.EDProducer("GaussRandomPThetaGunProducer",
    AddAntiParticle = cms.bool(False),
    PGunParameters = cms.PSet(
        MeanP = cms.double(options.Energy),
        SigmaP = cms.double(options.EnergyWidth),
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

#Flat momentum distribution of incoming particle guns
'''
process.generator = cms.EDProducer("FlatRandomEThetaGunProducer",
    AddAntiParticle = cms.bool(False),
    PGunParameters = cms.PSet(
        MinE = cms.double(options.Energy-options.EnergyWidth),    #options.Energy-options.EnergyWidth
        MaxE = cms.double(options.Energy+options.EnergyWidth),    #options.Energy+options.EnergyWidth
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
'''

#definition of physics lists:
#http://grupo.us.es/geterus/images/pdf/ieav-ita-2014/L9b-ReferencePhysicsLists.pdf
physicsList = 'SimG4Core/Physics/%s' % options.physicsList    
print "Using as physics list: %s" % physicsList
print "Using initial seed: ", options.RandomSeed
process.g4SimHits.Physics.type = cms.string(physicsList)

process.g4SimHits.StackingAction.SaveFirstLevelSecondary = cms.untracked.bool(True)
process.g4SimHits.StackingAction.SaveAllPrimaryDecayProductsAndConversions = cms.untracked.bool(True)


#setting for the gaussian beam profile (September 2016 TB at CERN with high energetic electrons)
if options.Energy in [20., 32.]: 
    process.VtxSmeared.MinY = {20.:-0.5, 32.: -1.0}[options.Energy]
    process.VtxSmeared.MaxY = {20.:3.6, 32.: 3.5}[options.Energy]
    process.VtxSmeared.MinX = {20.:-3.2, 32.: -1.5}[options.Energy]
    process.VtxSmeared.MaxX = {20.:1.0, 32.: 3.0}[options.Energy]   
    process.VtxSmeared.MinZ = 1094.99999
    process.VtxSmeared.MaxZ = 1095.00001

else:
    process.VtxSmeared.MeanY = {70.:1.3, 100.:0.6, 150.:0.9, 200.:0.5, 250.:1.1}[options.Energy]
    process.VtxSmeared.MeanX = {70.:-0.8, 100.:0.6, 150.:-1.1, 200.:0.3, 250.:-1.4}[options.Energy]
    process.VtxSmeared.MeanZ =  1095.
    process.VtxSmeared.SigmaX = {70.:1.2, 100.:1.4, 150.:0.7, 200.:0.8, 250.:1.0}[options.Energy]
    process.VtxSmeared.SigmaY = {70.:1.2, 100.:0.9, 150.:0.7, 200.:0.5, 250.:0.5}[options.Energy]
    process.VtxSmeared.SigmaZ = 0.00001   

#process.VtxSmeared.MeanX = 0.0
#process.VtxSmeared.MeanY = 0.0
#process.VtxSmeared.MeanZ =  1000.
#process.VtxSmeared.SigmaX = 5.01
#process.VtxSmeared.SigmaY = 5.01
#process.VtxSmeared.SigmaZ = 0.00001   




process.HGCalTBAnalyzer.DoDigis = False
process.HGCalTBAnalyzer.DoRecHits = False


process.RandomNumberGeneratorService.generator.initialSeed = cms.untracked.uint32(options.RandomSeed)
process.RandomNumberGeneratorService.VtxSmeared.initialSeed = cms.untracked.uint32(options.RandomSeed)

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
				process.endjob_step,
				#process.RAWSIMoutput_step,
				)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

print "Output file: "
print "Number of events: ",options.NEvents
print 'file:%s/TBGenSim_%s.root' % (options.outputFolder, options.outputPostfix)
print "Running..."

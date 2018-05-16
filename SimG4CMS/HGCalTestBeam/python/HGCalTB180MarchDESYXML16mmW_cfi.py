import FWCore.ParameterSet.Config as cms

XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/materials.xml',
        'Geometry/CMSCommonData/data/rotations.xml',
        'Geometry/HGCalCommonData/data/TB180/cms.xml',
        'Geometry/HGCalCommonData/data/TB180/March18/CaloRuns16mmW/hgcal.xml',
        'Geometry/HGCalCommonData/data/TB180/March18/CaloRuns16mmW/hgcalEE.xml',
        'Geometry/HGCalCommonData/data/TB180/March18/CaloRuns16mmW/hgcalwafer.xml',
        'Geometry/HGCalCommonData/data/TB180/March18/CaloRuns16mmW/hgcalBeam.xml',
        'Geometry/HGCalCommonData/data/TB180/hgcalsense.xml',
        'Geometry/HGCalCommonData/data/TB180/hgcProdCuts.xml',
        'Geometry/HGCalCommonData/data/TB180/March18/CaloRuns16mmW/hgcalCons.xml'),
    rootNodeName = cms.string('cms:OCMS')
)



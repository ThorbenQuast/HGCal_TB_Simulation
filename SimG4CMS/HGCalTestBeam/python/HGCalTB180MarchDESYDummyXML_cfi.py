import FWCore.ParameterSet.Config as cms

XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/materials.xml',
                               'Geometry/CMSCommonData/data/rotations.xml',
                               'Geometry/HGCalCommonData/data/TB180/cms.xml',
                               'Geometry/HGCalCommonData/data/TB180/March18/dummy/hgcal.xml',
                               'Geometry/HGCalCommonData/data/TB180/March18/dummy/hgcalEE.xml',
                               'Geometry/HGCalCommonData/data/TB180/March18/dummy/hgcalHE.xml',
                               'Geometry/HGCalCommonData/data/TB180/March18/dummy/hgcalBeam.xml',
                               'Geometry/HGCalCommonData/data/hgcalwafer/v7/hgcalwafer.xml',
                               'Geometry/HGCalCommonData/data/TB180/hgcalsense.xml',
                               'Geometry/HGCalCommonData/data/TB180/hgcProdCuts.xml',
                               'Geometry/HGCalCommonData/data/TB180/March18/dummy/hgcalCons.xml'
                               ),
    rootNodeName = cms.string('cms:OCMS')
)



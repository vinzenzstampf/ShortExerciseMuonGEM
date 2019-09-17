
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
process = cms.Process("ISPY",eras.Phase2)

process.load('Configuration.Geometry.GeometryExtended2023D17Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2023D17_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('file:step3.root')
)
  
from FWCore.MessageLogger.MessageLogger_cfi import *

process.add_(
    cms.Service("ISpyService",
    outputFileName = cms.untracked.string('ispy.ig'),
    outputIg = cms.untracked.bool(True),
    outputMaxEvents = cms.untracked.int32(10), # These are the number of events per ig file 
    debug = cms.untracked.bool(False)
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10) # These are the number of events to cycle through in the input root file
)

# Load everything here instead of using ISpy_Producer so that we can
# explicitly see what is running and change parameters easily in one
# place if needed

process.load("ISpy.Analyzers.ISpyEvent_cfi")
process.load('ISpy.Analyzers.ISpyCSCRecHit2D_cfi')
process.load('ISpy.Analyzers.ISpyCSCSegment_cfi')
process.load('ISpy.Analyzers.ISpyCSCStripDigi_cfi')
process.load('ISpy.Analyzers.ISpyCSCWireDigi_cfi')
process.load('ISpy.Analyzers.ISpyGEMRecHit_cfi')
process.load('ISpy.Analyzers.ISpyGEMSegment_cfi')
process.load('ISpy.Analyzers.ISpyDTDigi_cfi')
process.load('ISpy.Analyzers.ISpyDTRecHit_cfi')
process.load('ISpy.Analyzers.ISpyDTRecSegment4D_cfi')
process.load('ISpy.Analyzers.ISpyEBRecHit_cfi')
process.load('ISpy.Analyzers.ISpyEERecHit_cfi')
process.load('ISpy.Analyzers.ISpyESRecHit_cfi')
process.load('ISpy.Analyzers.ISpyGsfElectron_cfi')
process.load('ISpy.Analyzers.ISpyHBRecHit_cfi')
process.load('ISpy.Analyzers.ISpyHERecHit_cfi')
process.load('ISpy.Analyzers.ISpyHFRecHit_cfi')
process.load('ISpy.Analyzers.ISpyHORecHit_cfi')
process.load('ISpy.Analyzers.ISpyJet_cfi')
process.load('ISpy.Analyzers.ISpyL1GlobalTriggerReadoutRecord_cfi')
process.load('ISpy.Analyzers.ISpyMET_cfi')
process.load('ISpy.Analyzers.ISpyMuon_cfi')
process.load('ISpy.Analyzers.ISpyPhoton_cfi')
process.load('ISpy.Analyzers.ISpyPixelDigi_cfi')
process.load('ISpy.Analyzers.ISpyPreshowerCluster_cfi')
process.load('ISpy.Analyzers.ISpyRPCRecHit_cfi')
process.load('ISpy.Analyzers.ISpySiPixelCluster_cfi')
process.load('ISpy.Analyzers.ISpySiPixelRecHit_cfi')
process.load('ISpy.Analyzers.ISpySiStripCluster_cfi')
process.load('ISpy.Analyzers.ISpySiStripDigi_cfi')
process.load('ISpy.Analyzers.ISpySuperCluster_cfi')
process.load('ISpy.Analyzers.ISpyTrack_cfi')
process.load('ISpy.Analyzers.ISpyTrackingRecHit_cfi')
process.load('ISpy.Analyzers.ISpyTriggerEvent_cfi')
process.load('ISpy.Analyzers.ISpyVertex_cfi')

process.ISpyCSCRecHit2D.iSpyCSCRecHit2DTag = cms.InputTag("csc2DRecHits")

process.ISpyCSCSegment.iSpyCSCSegmentTag = cms.InputTag("cscSegments")
process.ISpyCSCStripDigi.iSpyCSCStripDigiTag = cms.InputTag('muonCSCDigis:MuonCSCStripDigi')
process.ISpyCSCStripDigi.thresholdOffset = cms.int32(9)
process.ISpyCSCWireDigi.iSpyCSCWireDigiTag = cms.InputTag('muonCSCDigis:MuonCSCWireDigi')

process.ISpyDTDigi.iSpyDTDigiTag = cms.InputTag('muonDTDigis')
process.ISpyDTRecHit.iSpyDTRecHitTag = cms.InputTag('dt1DRecHits')
process.ISpyDTRecSegment4D.iSpyDTRecSegment4DTag = cms.InputTag('dt4DSegments')

process.ISpyEBRecHit.iSpyEBRecHitTag = cms.InputTag('ecalRecHit:EcalRecHitsEB')
process.ISpyEERecHit.iSpyEERecHitTag = cms.InputTag('ecalRecHit:EcalRecHitsEE')
process.ISpyESRecHit.iSpyESRecHitTag = cms.InputTag('ecalPreshowerRecHit:EcalRecHitsES')

process.ISpyGsfElectron.iSpyGsfElectronTag = cms.InputTag('gsfElectrons')

process.ISpyHBRecHit.iSpyHBRecHitTag = cms.InputTag("hbhereco")
process.ISpyHERecHit.iSpyHERecHitTag = cms.InputTag("hbhereco")
process.ISpyHFRecHit.iSpyHFRecHitTag = cms.InputTag("hfreco")
process.ISpyHORecHit.iSpyHORecHitTag = cms.InputTag("horeco")

process.ISpyJet.iSpyJetTag = cms.InputTag("iterativeCone5CaloJets")

process.ISpyL1GlobalTriggerReadoutRecord.iSpyL1GlobalTriggerReadoutRecordTag = cms.InputTag("gtDigis")

process.ISpyMET.iSpyMETTag = cms.InputTag("htMetIC5")

process.ISpyMuon.iSpyMuonTag = cms.InputTag("muons")

process.ISpyPhoton.iSpyPhotonTag = cms.InputTag('photons')

process.ISpyPixelDigi.iSpyPixelDigiTag = cms.InputTag("siPixelDigis")

process.ISpyPreshowerCluster.iSpyPreshowerClusterTags = cms.VInputTag(cms.InputTag('multi5x5SuperClustersWithPreshower:preshowerXClusters'), cms.InputTag('multi5x5SuperClustersWithPreshower:preshowerYClusters'))

process.ISpyRPCRecHit.iSpyRPCRecHitTag = cms.InputTag("rpcRecHits")

process.ISpySiPixelCluster.iSpySiPixelClusterTag = cms.InputTag("siPixelClusters")
process.ISpySiPixelRecHit.iSpySiPixelRecHitTag = cms.InputTag("siPixelRecHits")
process.ISpySiStripCluster.iSpySiStripClusterTag = cms.InputTag("siStripClusters")
process.ISpySiStripDigi.iSpySiStripDigiTag = cms.InputTag("siStripDigis:ZeroSuppressed")

process.ISpySuperCluster.iSpySuperClusterTag = cms.InputTag('hybridSuperClusters')

process.ISpyTrack.iSpyTrackTags = cms.VInputTag(cms.InputTag("generalTracks"))
process.ISpyTrackingRecHit.iSpyTrackingRecHitTags = cms.VInputTag(cms.InputTag("generalTracks"))

process.ISpyTriggerEvent.triggerEventTag = cms.InputTag('hltTriggerSummaryAOD')
process.ISpyTriggerEvent.triggerResultsTag = cms.InputTag('TriggerResults')
process.ISpyTriggerEvent.processName = cms.string('HLT')

process.ISpyVertex.iSpyVertexTag = cms.InputTag('offlinePrimaryVertices')

process.iSpy = cms.Path(process.ISpyEvent*
                        process.ISpyCSCRecHit2D*
                        process.ISpyCSCSegment*
                        process.ISpyCSCStripDigi*
                        process.ISpyCSCWireDigi*
                        process.ISpyGEMRecHit*
                        process.ISpyGEMSegment*
                        process.ISpyDTDigi*
                        process.ISpyDTRecHit*
                        process.ISpyDTRecSegment4D*
                        process.ISpyEBRecHit*
                        process.ISpyEERecHit*
                        process.ISpyESRecHit*
                        process.ISpyGsfElectron*
                        process.ISpyHBRecHit*
                        process.ISpyHERecHit*
                        process.ISpyHFRecHit*
                        process.ISpyHORecHit*
                        process.ISpyJet*
                        process.ISpyL1GlobalTriggerReadoutRecord*
                        process.ISpyMET*
                        process.ISpyMuon*
                        process.ISpyPhoton*
                        process.ISpyPixelDigi*
                        process.ISpyPreshowerCluster*
                        process.ISpyRPCRecHit*
                        process.ISpySiPixelCluster*
                        process.ISpySiPixelRecHit*
                        #process.ISpySiStripCluster*
                        #process.ISpySiStripDigi*
                        process.ISpySuperCluster*
                        process.ISpyTrack*
                        process.ISpyTrackingRecHit*
                        #process.ISpyTriggerEvent*
                        process.ISpyVertex)

process.schedule = cms.Schedule(process.iSpy)


from scale_factors_config import *
from ttalps_extra_collections import extraEventCollections

nEvents = -1
printEveryNevents = 10000

runDefaultHistograms = True
runTriggerHistograms = False
runPileupHistograms = False
runLLPNanoAODHistograms = False

weightsBranchName = "genWeight"

pileupScaleFactorsPath = "/nfs/dust/cms/user/jniedzie/ttalps_cms/pileup_scale_factors.root"
pileupScaleFactorsHistName = "pileup_scale_factors"

applyScaleFactors = {
  "muon": False,
  "muonTrigger": False,
  "pileup": True,
}

defaultHistParams = (
#  collection             variable               bins    xmin    xmax    dir
  ("Event"              , "PV_npvs"             , 300   , 0     , 300   , ""  ),
  ("Event"              , "PV_npvsGood"         , 300   , 0     , 300   , ""  ),
  ("Event"              , "MET_pt"              , 1000  , 0     , 1000  , ""  ),
  
  ("Event"              , "nMuon"               , 50    , 0     , 50    , ""  ),
  ("Muon"               , "pt"                  , 2000  , 0     , 1000  , ""  ),
  ("Muon"               , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("Muon"               , "dxy"                 , 8000  , -1000  , 1000   , ""  ),
  ("Muon"               , "dz"                  , 8000  , -1000  , 1000   , ""  ),
  
  ("Event"              , "nTightMuons"         , 50    , 0     , 50    , ""  ),
  ("TightMuons"         , "pt"                  , 2000  , 0     , 1000  , ""  ),
  ("TightMuons"         , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("TightMuons"         , "dxy"                 , 8000  , -1000  , 1000   , ""  ),
  ("TightMuons"         , "dz"                  , 8000  , -1000  , 1000   , ""  ),
  ("TightMuons"         , "pfRelIso04_all"      , 2000  , -10   , 10    , ""  ),
  ("TightMuons"         , "pfRelIso03_chg"      , 2000  , -10   , 10    , ""  ),
  ("TightMuons"         , "pfRelIso03_all"      , 2000  , -10   , 10    , ""  ),
  ("TightMuons"         , "tkRelIso"            , 2000  , -10   , 10    , ""  ),
  ("TightMuons"         , "miniPFRelIso_chg"    , 2000  , -10   , 10    , ""  ),
  ("TightMuons"         , "miniPFRelIso_all"    , 2000  , -10   , 10    , ""  ),
  ("TightMuons"         , "jetRelIso"           , 2000  , -10   , 10    , ""  ),

  
  ("Event"              , "nLooseMuons"         , 50    , 0     , 50    , ""  ),
  ("LooseMuons"         , "pt"                  , 2000  , 0     , 1000  , ""  ),
  ("LooseMuons"         , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("LooseMuons"         , "dxy"                 , 8000  , -1000  , 1000   , ""  ),
  ("LooseMuons"         , "dz"                  , 8000  , -1000  , 1000   , ""  ),
  ("LooseMuons"         , "pfRelIso04_all"      , 2000  , -10   , 10    , ""  ),
  ("LooseMuons"         , "pfRelIso03_chg"      , 2000  , -10   , 10    , ""  ),
  ("LooseMuons"         , "pfRelIso03_all"      , 2000  , -10   , 10    , ""  ),
  ("LooseMuons"         , "tkRelIso"            , 2000  , -10   , 10    , ""  ),
  ("LooseMuons"         , "miniPFRelIso_chg"    , 2000  , -10   , 10    , ""  ),
  ("LooseMuons"         , "miniPFRelIso_all"    , 2000  , -10   , 10    , ""  ),
  ("LooseMuons"         , "jetRelIso"           , 2000  , -10   , 10    , ""  ),
  
  # ("Event"              , "nLooseDSAMuons"      , 50    , 0     , 50    , ""  ),
  # ("LooseDSAMuons"      , "pt"                  , 2000  , 0     , 1000  , ""  ),
  # ("LooseDSAMuons"      , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  # ("LooseDSAMuons"      , "dxy"                 , 8000  , -1000  , 1000   , ""  ),
  # ("LooseDSAMuons"      , "dz"                  , 8000  , -1000  , 1000   , ""  ),
  
  ("Event"              , "nElectron"           , 50    , 0     , 50    , ""  ),
  ("Electron"           , "pt"                  , 2000  , 0     , 1000  , ""  ),
  ("Electron"           , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("Electron"           , "dxy"                 , 8000  , -1000  , 1000   , ""  ),
  ("Electron"           , "dz"                  , 8000  , -1000  , 1000   , ""  ),
  
  ("Event"              , "nLooseElectrons"     , 50    , 0     , 50    , ""  ),
  ("LooseElectrons"     , "pt"                  , 2000  , 0     , 1000  , ""  ),
  ("LooseElectrons"     , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("LooseElectrons"     , "dxy"                 , 8000  , -1000  , 1000   , ""  ),
  ("LooseElectrons"     , "dz"                  , 8000  , -1000  , 1000   , ""  ),
  
  ("Event"              , "nJet"                , 50    , 0     , 50    , ""  ),
  ("Jet"                , "pt"                  , 2000  , 0     , 1000  , ""  ),
  ("Jet"                , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("Jet"                , "phi"                 , 100   , -2.5  , 2.5   , ""  ),
  ("Jet"                , "btagDeepB"           , 200   , -1    , 1     , ""  ),
  
  ("Event"              , "nGoodJets"           , 50    , 0     , 50    , ""  ),
  ("GoodJets"           , "pt"                  , 2000  , 0     , 2000  , ""  ),
  ("GoodJets"           , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("GoodJets"           , "phi"                 , 100   , -2.5  , 2.5   , ""  ),
  ("GoodJets"           , "btagDeepB"           , 200   , -1    , 1     , ""  ),
  ("GoodJets"           , "btagDeepFlavB"       , 200   , -1    , 1     , ""  ),
  
  ("Event"                    , "nGoodMediumBtaggedJets"    , 50    , 0     , 50    , ""  ),
  ("GoodMediumBtaggedJets"    , "pt"                  , 2000  , 0     , 2000  , ""  ),
  ("GoodMediumBtaggedJets"    , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("GoodMediumBtaggedJets"    , "phi"                 , 100   , -2.5  , 2.5   , ""  ),
  ("GoodMediumBtaggedJets"    , "btagDeepB"           , 200   , -1    , 1     , ""  ),
  ("GoodMediumBtaggedJets"    , "btagDeepFlavB"       , 200   , -1    , 1     , ""  ),
  
  ("Event"                    , "nGoodNonTightBtaggedJets" , 50    , 0     , 50    , ""  ),
  ("GoodNonTightBtaggedJets"  , "pt"                  , 2000  , 0     , 2000  , ""  ),
  ("GoodNonTightBtaggedJets"  , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("GoodNonTightBtaggedJets"  , "phi"                 , 100   , -2.5  , 2.5   , ""  ),
  ("GoodNonTightBtaggedJets"  , "btagDeepB"           , 200   , -1    , 1     , ""  ),
  ("GoodNonTightBtaggedJets"  , "btagDeepFlavB"       , 200   , -1    , 1     , ""  ),

)

LLPNanoAOD_defaultHistParams = (

  ("Event"              , "nDSAMuon"            , 50    , 0     , 50    , ""  ),
  ("DSAMuon"            , "pt"                  , 2000  , 0     , 1000  , ""  ),
  ("DSAMuon"            , "eta"                 , 100   , -2.5  , 2.5   , ""  ),
  ("DSAMuon"            , "dxy"                 , 1600  , -400  , 400   , ""  ),
  ("DSAMuon"            , "dz"                  , 1600  , -400  , 400   , ""  ),

  ("Event"              , "nMuonVertex"         , 50    , 0     , 50    , ""  ),
  ("MuonVertex"         , "chi2"                , 500   , 0     , 500   , ""  ),
  ("MuonVertex"         , "vxy"                 , 500   , 0     , 500   , ""  ),
  ("MuonVertex"         , "vxySigma"            , 500   , 0     , 500   , ""  ),
  ("MuonVertex"         , "vz"                  , 1000  , -500  , 500   , ""  ),
  ("MuonVertex"         , "dR"                  , 500   , 0     , 10    , ""  ),

  ("Event"              , "nDSAMuonVertex"      , 50    , 0     , 50    , ""  ),
  ("DSAMuonVertex"      , "chi2"                , 500   , 0     , 500   , ""  ),
  ("DSAMuonVertex"      , "vxy"                 , 500   , 0     , 500   , ""  ),
  ("DSAMuonVertex"      , "vxySigma"            , 500   , 0     , 500   , ""  ),
  ("DSAMuonVertex"      , "vz"                  , 1000  , -500  , 500   , ""  ),
  ("DSAMuonVertex"      , "dR"                  , 500   , 0     , 10    , ""  ),

  ("Event"              , "nMuonCombVertex"     , 50    , 0     , 50    , ""  ),
  ("MuonCombVertex"     , "chi2"                , 500   , 0     , 500   , ""  ),
  ("MuonCombVertex"     , "vxy"                 , 500   , 0     , 500   , ""  ),
  ("MuonCombVertex"     , "vxySigma"            , 500   , 0     , 500   , ""  ),
  ("MuonCombVertex"     , "vz"                  , 1000  , -500  , 500   , ""  ),
  ("MuonCombVertex"     , "dR"                  , 500   , 0     , 10    , ""  ),
)

if runLLPNanoAODHistograms:
  defaultHistParams = defaultHistParams + LLPNanoAOD_defaultHistParams

histParams = (
#  collection         variable                      bins   xmin   xmax    dir
  ("Muon"           , "leadingPt"                 , 2000  , 0   , 1000  , ""  ),
  ("TightMuons"     , "leadingPt"                 , 2000  , 0   , 1000  , ""  ),
  ("LooseMuons"     , "leadingPt"                 , 2000  , 0   , 1000  , ""  ),
  ("Electron"       , "leadingPt"                 , 2000  , 0   , 1000  , ""  ),
  ("LooseElectrons" , "leadingPt"                 , 2000  , 0   , 1000  , ""  ),
  ("Jet"            , "leadingPt"                 , 2000  , 0   , 1000  , ""  ),
  ("GoodJets"       , "leadingPt"                 , 2000  , 0   , 1000  , ""  ),
  
  ("Muon"           , "subleadingPt"              , 2000  , 0   , 1000  , ""  ),
  ("TightMuons"     , "subleadingPt"              , 2000  , 0   , 1000  , ""  ),
  ("LooseMuons"     , "subleadingPt"              , 2000  , 0   , 1000  , ""  ),
  ("Electron"       , "subleadingPt"              , 2000  , 0   , 1000  , ""  ),
  ("LooseElectrons" , "subleadingPt"              , 2000  , 0   , 1000  , ""  ),
  ("Jet"            , "subleadingPt"              , 2000  , 0   , 1000  , ""  ),
  ("GoodJets"       , "subleadingPt"              , 2000  , 0   , 1000  , ""  ),
  
  ("LooseMuons"     , "dimuonMinv"                , 200   , 0   , 200   , ""  ),
  ("LooseMuons"     , "dimuonMinvClosestToZ"      , 200   , 0   , 200   , ""  ),
  ("LooseMuons"     , "dimuonDeltaRclosestToZ"    , 200   , -10 , 10    , ""  ),
  ("LooseMuons"     , "dimuonDeltaEtaclosestToZ"  , 200   , -10 , 10    , ""  ),
  ("LooseMuons"     , "dimuonDeltaPhiclosestToZ"  , 200   , -10 , 10    , ""  ),
  ("GoodJets"       , "minvBjet2jets"             , 2000  , 0   , 2000  , ""  ),
  ("TightMuons"     , "deltaPhiMuonMET"           , 200   , -4  , 4     , ""  ),
  ("TightMuons"     , "minvMuonMET"               , 1000  , 0   , 1000  , ""  ),
  
  ("Event"          , "normCheck"                 , 1     , 0   , 1     , ""  ),
)

LLPNanoAOD_histParams = (
  ("Event"          , "nAllLooseMuons"            , 50    , 0     , 50    , ""  ),
  ("AllLooseMuons"  , "pt"                        , 2000  , 0     , 1000  , ""  ),
  ("AllLooseMuons"  , "eta"                       , 100   , -2.5  , 2.5   , ""  ),
  ("AllLooseMuons"  , "dxy"                       , 1600  , -400  , 400   , ""  ),
  ("AllLooseMuons"  , "dz"                        , 1600  , -400  , 400   , ""  ),
  ("AllLooseMuons"  , "deltaR"                    , 500   , 0     , 50    , ""  ),
  ("AllLooseMuons"  , "minDeltaR"                 , 500   , 0     , 50    , ""  ),

  ("Event"          , "nLooseDSAMuons"            , 50    , 0     , 50    , ""  ),
  ("LooseDSAMuons"  , "pt"                        , 2000  , 0     , 1000  , ""  ),
  ("LooseDSAMuons"  , "eta"                       , 100   , -2.5  , 2.5   , ""  ),
  ("LooseDSAMuons"  , "dxy"                       , 1600  , -400  , 400   , ""  ),
  ("LooseDSAMuons"  , "dz"                        , 1600  , -400  , 400   , ""  ),
)

if runLLPNanoAODHistograms:
  histParams = histParams + LLPNanoAOD_histParams

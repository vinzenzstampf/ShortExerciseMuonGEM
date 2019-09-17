import ROOT
from DataFormats.FWLite import Events, Handle

muonsLable, muons = "muons", Handle("vector<reco::Muon>")

fdir = "../step3.root"

events = Events(fdir)
for iev, event in enumerate(events):
    print "iev", iev

    event.getByLabel(muonsLable, muons)

    for mu in muons.product(): 
        for chamber in mu.matches():
            for seg in chamber.gemMatches:
                if seg.gemSegmentRef.gemDetId().station() == 1:
                    dx = chamber.x - seg.gemSegmentRef.get().localPosition().x() 
                    print dx

        muTrack = mu.standAloneMuon() # track built with only muon system
        if muTrack.isNonnull():
            for i in range(muTrack.recHitsSize()):
                rh = muTrack.recHit(i)
                if rh.geographicalId().det() != 2: continue # Muon detector
                if rh.geographicalId().subdetId() != 4: continue # GEM detector

                if rh.gemId().station() != 1: continue # GE1/1
                print rh.localPosition().x()



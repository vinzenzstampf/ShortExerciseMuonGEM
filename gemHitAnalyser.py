import ROOT
from DataFormats.FWLite import Events, Handle
from pdb import set_trace

gemRecHitsLabel, gemRecHits = "gemRecHits", Handle("edm::RangeMap<GEMDetId,edm::OwnVector<GEMRecHit,edm::ClonePolicy<GEMRecHit> >,edm::ClonePolicy<GEMRecHit> >")
muons_label, muons = 'muons', Handle('vector<reco::Muon>'))

fdir = "../step3.root"

events = Events(fdir)
for iev, event in enumerate(events):

    event.getByLabel(gemRecHitsLabel, gemRecHits)
    event.getByLabel(muons_label, muons)
    print "nGEMRecHit:", gemRecHits.product().size()

    muons = muons.product()

    for rh in gemRecHits.product():
        print rh.gemId().region(), rh.gemId().station(), rh.gemId().layer(), rh.gemId().chamber(), rh.localPosition().x(), rh.gemId().roll()

    




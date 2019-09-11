import ROOT
from DataFormats.FWLite import Events, Handle

gemRecHitsLabel, gemRecHits = "gemRecHits", Handle("edm::RangeMap<GEMDetId,edm::OwnVector<GEMRecHit,edm::ClonePolicy<GEMRecHit> >,edm::ClonePolicy<GEMRecHit> >")

fdir = "../step3.root"

events = Events(fdir)
for iev, event in enumerate(events):

    event.getByLabel(gemRecHitsLabel, gemRecHits)
    print "nGEMRecHit:", gemRecHits.product().size()

    #for rh in gemRecHits.product():
    #    print rh.gemId().region(), rh.gemId().station(), rh.gemId().layer(), rh.gemId().chamber(), rh.localPosition().x(), rh.gemId().roll()




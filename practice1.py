import ROOT
from DataFormats.FWLite import Events, Handle

gemRecHitsLabel, gemRecHits = "gemRecHits", Handle("edm::RangeMap<GEMDetId,edm::OwnVector<GEMRecHit,edm::ClonePolicy<GEMRecHit> >,edm::ClonePolicy<GEMRecHit> >")
simHitsLabel, simHits = ("g4SimHits", "MuonGEMHits"), Handle("vector<PSimHit>")

h_cls = ROOT.TH2D("GEM RecHit Cluster size", "GEM RecHit Cluster size; Cluster size; i#eta", 10, 0, 10, 8, 1, 9)
h_dx = ROOT.TH1D("GEM RecHit Resolution X", "GEM RecHit Resolution X; #delta x; i#eta", 30, -5, 5)
h_sim_ieta = ROOT.TH1D("GEM SimHit i#eta", "GEM SimHit i#eta; i#eta; Number of GEMSimHit", 8, 1, 9)
h_sim_ieta_matched = ROOT.TH1D("GEM SimHit i#eta matched", "GEM SimHit i#eta matched; #ieta; Number of GEMSimHit", 8, 1, 9)

fdir = "../step3.root"

events = Events(fdir)
for iev, event in enumerate(events):
    print "iev", iev

    event.getByLabel(simHitsLabel, simHits)
    event.getByLabel(gemRecHitsLabel, gemRecHits)

    for rh in gemRecHits.product():
        h_cls.Fill(rh.gemId().roll(), rh.clusterSize())

    for sh in simHits.product():
        detId = ROOT.DetId(sh.detUnitId())
        if detId.det() != 2: continue # Muon detector
        if detId.subdetId() != 4: continue # GEM detector

        gemDetId = ROOT.GEMDetId(detId)
        if gemDetId.station() != 1: continue # GE1/1
        h_sim_ieta.Fill(gemDetId.roll())

        matched = False
        for rh in gemRecHits.product():
            dx = -99
            if sh.detUnitId() == rh.gemId().rawId():
                dx = sh.localPosition().x() - rh.localPosition().x()
                h_dx.Fill(dx)
            if abs(dx) < 0.5:
                matched = True
        h_sim_ieta_matched.Fill(gemDetId.roll())

c = ROOT.TCanvas()
eff = ROOT.TEfficiency(h_sim_ieta, h_sim_ieta_matched)
eff.Draw()
c.Print("eff.png")

h_dx.Fit('gaus')




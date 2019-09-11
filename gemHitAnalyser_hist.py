import ROOT
from DataFormats.FWLite import Events, Handle

gemRecHitsLabel, gemRecHits = "gemRecHits", Handle("edm::RangeMap<GEMDetId,edm::OwnVector<GEMRecHit,edm::ClonePolicy<GEMRecHit> >,edm::ClonePolicy<GEMRecHit> >")
simHitsLabel, simHits = ("g4SimHits", "MuonGEMHits"), Handle("vector<PSimHit>")

h_map = ROOT.TH2D("GEM RecHit Position", "GEM RecHit Position; Local x; i#eta", 30, -80, 80, 8, 1, 9)
h_rechit_y = ROOT.TH1D("GEM RecHit local position y", "GEM RecHit local position y; Local y; Number of hits", 30, -15, 15)
h_simhit_y = ROOT.TH1D("GEM SimHit local position y", "GEM SimHit local position y; Local y; Number of hits", 30, -15, 15)

fdir = "../step3.root"

events = Events(fdir)
for iev, event in enumerate(events):
    print "iev", iev

    event.getByLabel(simHitsLabel, simHits)
    event.getByLabel(gemRecHitsLabel, gemRecHits)

    for rh in gemRecHits.product():
        h_map.Fill(rh.localPosition().x(), rh.gemId().roll())
        h_rechit_y.Fill(rh.localPosition().y())

    for sh in simHits.product():
        detId = ROOT.DetId(sh.detUnitId())
        if detId.det() != 2: continue # Muon detector
        if detId.subdetId() != 4: continue # GEM detector

        gemDetId = ROOT.GEMDetId(detId)
        if gemDetId.station() != 1: continue # GE1/1
        h_simhit_y.Fill(sh.localPosition().y())

c = ROOT.TCanvas()
h_map.Draw("colz")
c.Print("map.png")

outroot = ROOT.TFile("histo.root", "RECREATE")
h_map.Write()
h_rechit_y.Write()
h_simhit_y.Write()
outroot.Write()
outroot.Close()


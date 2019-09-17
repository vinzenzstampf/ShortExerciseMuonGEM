import ROOT
from DataFormats.FWLite import Events, Handle
from collections import OrderedDict as od
import numpy as np
from pdb import set_trace

gemRecHitsLabel, gemRecHits = "gemRecHits", Handle("edm::RangeMap<GEMDetId,edm::OwnVector<GEMRecHit,edm::ClonePolicy<GEMRecHit> >,edm::ClonePolicy<GEMRecHit> >")
simHitsLabel, simHits = ("g4SimHits", "MuonGEMHits"), Handle("vector<PSimHit>")

h_map          = ROOT.TH2D("GEM RecHit Position",               "GEM RecHit Position; Local x; i#eta",                              30, -80, 80, 8, 1, 9)
h_1st_x        = ROOT.TH2D("GEM RecHit First Strip vs x",       "GEM RecHit First Strip vs x; Local x; First Strip",                30, -80, 80, 374, 0, 374)
h_rechit_y     = ROOT.TH1D("GEM RecHit local position y",       "GEM RecHit local position y; Local y; Number of hits",             30, -15, 15)
h_simhit_y     = ROOT.TH1D("GEM SimHit local position y",       "GEM SimHit local position y; Local y; Number of hits",             30, -15, 15)
h_rechit_x_err = ROOT.TH1D("GEM RecHit local position x error", "GEM RecHit local position x error; Local x error; Number of hits", 30, -15, 15)
h_rechit_y_err = ROOT.TH1D("GEM RecHit local position y error", "GEM RecHit local position y error; Local y error; Number of hits", 30, -15, 15)

fdir = "../step3.root"

cluster_sizes = od()

events = Events(fdir)
for iev, event in enumerate(events):
    print "iev", iev

    event.getByLabel(simHitsLabel, simHits)
    event.getByLabel(gemRecHitsLabel, gemRecHits)

    for rh in gemRecHits.product():
        h_map.Fill(rh.localPosition().x(), rh.gemId().roll())
        h_1st_x.Fill(rh.localPosition().x(), rh.firstClusterStrip())
        h_rechit_y.Fill(rh.localPosition().y())
        h_rechit_x_err.Fill(np.sqrt(rh.localPositionError().xx()))
        h_rechit_y_err.Fill(np.sqrt(rh.localPositionError().yy()))
        try: cluster_sizes[rh.gemId().roll()].append(rh.clusterSize())
        except:
            cluster_sizes[rh.gemId().roll()] = []
            cluster_sizes[rh.gemId().roll()].append(rh.clusterSize())

    for sh in simHits.product():
        detId = ROOT.DetId(sh.detUnitId())
        if detId.det() != 2: continue # Muon detector
        if detId.subdetId() != 4: continue # GEM detector

        gemDetId = ROOT.GEMDetId(detId)
        if gemDetId.station() != 1: continue # GE1/1
        h_simhit_y.Fill(sh.localPosition().y())

# set_trace()
cluster_size_avg = od()
for k in cluster_sizes.keys():
    cluster_size_avg[k] = np.mean(cluster_sizes[k])
    print 'ieta', k, ';  size', cluster_size_avg[k]

# c = ROOT.TCanvas()
# h_map.Draw("colz")
# c.Print("map.png")

outroot = ROOT.TFile("histo.root", "RECREATE")
h_map.Write()
h_1st_x.Write()
h_rechit_x_err.Write()
h_rechit_y_err.Write()
h_rechit_y.Write()
h_simhit_y.Write()
outroot.Write()
outroot.Close()


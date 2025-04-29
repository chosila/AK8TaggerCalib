import uproot
import numpy as np
import matplotlib.pyplot as plt

# fmu = uproot.open('/afs/cern.ch/work/c/csutanta/public/unskimmed_histograms/v1/lepjet/unskimmed_SingleMuon_bdtHi.root')
# feg = uproot.open('/afs/cern.ch/work/c/csutanta/public/unskimmed_histograms/v1/lepjet/unskimmed_EGamma_bdtHi.root')
# branches = [
#     ## XbbOverQCD. signal is semilep bbqq, bq, bb, and dilep bb
#     'evt/TTToSemiLeptonic_powheg_bbqq/particleNetMD_XbbOverQCD_sel_0b_BBQQ_central',
#     'evt/TTToSemiLeptonic_powheg_bbq/particleNetMD_XbbOverQCD_sel_0b_BBQQ_central',
#     'evt/TTToSemiLeptonic_powheg_bb/particleNetMD_XbbOverQCD_sel_0b_BBQQ_central',
#     'evt/TTTo2L2Nu_powheg_bb/particleNetMD_XbbOverQCD_sel_0b_BBQQ_central',
# ]


# fmu = uproot.open('/afs/cern.ch/work/c/csutanta/public/unskimmed_histograms/v2/unskimmed_SingleMuon_bdtHi.root')
# feg = uproot.open('/afs/cern.ch/work/c/csutanta/public/unskimmed_histograms/v2/unskimmed_EGamma_bdtHi.root')
# branches = [
#     ## PNet_TT_bbqq_vs_01b. signal is semilep bbqq, bbq
#     'evt/TTToSemiLeptonic_powheg_bbqq/PNet_TT_bbqq_vs_01b_sel_0b_BBQQ_central',
#     'evt/TTToSemiLeptonic_powheg_bbq/PNet_TT_bbqq_vs_01b_sel_0b_BBQQ_central',
# ]

## X4b

## signal files:
fns = {
    '/eos/cms/store/user/ssawant/htoaa/analysis/20250317_CR_QCD4b_FullSyst/2018/CombineFit_inputFiles/CR4b_3M3T/CR4b_3M3T_QCD_4bAndMoreCat_2018.root' : 'CR4b_3M3T_QCD_4bAndMoreCat_2018_X4b_v2ab_Haa4b_score_Nom',
    '/eos/cms/store/user/ssawant/htoaa/analysis/20250317_CR_QCD4b_FullSyst/2018/CombineFit_inputFiles/CR4b_4M3T/CR4b_4M3T_QCD_4bAndMoreCat_2018.root' : 'CR4b_4M3T_QCD_4bAndMoreCat_2018_X4b_v2ab_Haa4b_score_Nom',
    '/eos/cms/store/user/ssawant/htoaa/analysis/20250317_CR_QCD4b_FullSyst/2018/CombineFit_inputFiles/CR4b_4M4T/CR4b_4M4T_QCD_4bAndMoreCat_2018.root' : 'CR4b_4M4T_QCD_4bAndMoreCat_2018_X4b_v2ab_Haa4b_score_Nom'
}
print('threshold,efficiency')
thresholds = [1]# np.linspace(0,1,1000)

for threshold in thresholds:
    passed = 0
    total = 0
    vals = []
    edges = []
    for fn in fns:
        binval = uproot.open(fn)[fns[fn]].values()
        binedge =  uproot.open(fn)[fns[fn]].axis().edges()[1:]
        passed = passed + np.sum(binval[binedge > threshold])
        total = total + binval.sum()
        vals.append(binval)
        edges.append(binedge)



    vals = np.array(vals).sum(axis=0) ## sum the hist values so it is 1 histogram
    edges = np.array(edges)
    fig, ax = plt.subplots()
    ax.step(edges[0],vals)
    ax.vlines(0.98, 0,300, color='red', label = '0.98')
    ax.legend()
    ax.set_title('X4b 3M3T+4M3T+4M4T')
    ax.set_xlabel('X4b')
    fig.savefig('histogram_X4b_3M3T_4M3T_4M4T.png')
    print(f'{threshold},{passed/total}')




exit()

fmu = uproot.open('/afs/cern.ch/work/c/csutanta/public/unskimmed_histograms/v2/unskimmed_SingleMuon_bdtHi.root')
feg = uproot.open('/afs/cern.ch/work/c/csutanta/public/unskimmed_histograms/v2/unskimmed_EGamma_bdtHi.root')
branches = [
    ## PNet_X4b_v2_Haa34b_score. signal is semilep bbqq, bbq
    'evt/TTToSemiLeptonic_powheg_bbqq/PNet_X4b_v2_Haa34b_score_sel_0b_BBQQ_central',
    'evt/TTToSemiLeptonic_powheg_bbq/PNet_X4b_v2_Haa34b_score_sel_0b_BBQQ_central',
]

thresholds = np.linspace(0, 1, 1000)
print('threshold,efficiency')
for threshold in thresholds:
    mupass = 0
    mutot = 0
    egpass = 0
    egtot = 0
    for branch in branches:
        mubin = fmu[branch].values()
        muedge = fmu[branch].axis().edges()
        muedge = muedge[1:] ## we don't need to count edge = 0
        mupass = mupass + np.sum(mubin[muedge > threshold])
        mutot = mutot + mubin.sum()

        egbin = feg[branch].values()
        egedge = feg[branch].axis().edges()
        egedge = egedge[1:] ## we don't need to count edge = 0
        egpass = egpass + np.sum(egbin[egedge > threshold])
        egtot = egtot + egbin.sum()



    print(f'{threshold},{(mupass+egpass)/(mutot+egtot)}')


## use the bineed files

eg = uproot.open('/afs/cern.ch/work/c/csutanta/HTOAA_CMSSW/CMSSW_14_1_0_pre4/src/HiggsAnalysis/CombinedLimit/AK8TaggerCalib/data/v1/lepjet/EGamma/AK8_tagger_calib_Xbb_0b_BBQQ_2p0_slc7.root')['Sum2B_bdtHi_Xbb'].values()
mu = uproot.open('/afs/cern.ch/work/c/csutanta/HTOAA_CMSSW/CMSSW_14_1_0_pre4/src/HiggsAnalysis/CombinedLimit/AK8TaggerCalib/data/v1/lepjet/SingleMuon/AK8_tagger_calib_Xbb_0b_BBQQ_2p0_slc7.root')['Sum2B_bdtHi_Xbb'].values()

print('the rebinned file')
print(eg)
print(mu)

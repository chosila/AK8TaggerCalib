import uproot
import numpy as np
# import matplotlib.pyplot as plt

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
#fns = {
    #'/eos/cms/store/user/ssawant/htoaa/analysis/20250317_CR_QCD4b_FullSyst/2018/CombineFit_inputFiles/CR4b_3M3T/CR4b_3M3T_QCD_4bAndMoreCat_2018.root' : 'CR4b_3M3T_QCD_4bAndMoreCat_2018_X4b_v2ab_Haa4b_score_Nom',
    #'/eos/cms/store/user/ssawant/htoaa/analysis/20250317_CR_QCD4b_FullSyst/2018/CombineFit_inputFiles/CR4b_4M3T/CR4b_4M3T_QCD_4bAndMoreCat_2018.root' : 'CR4b_4M3T_QCD_4bAndMoreCat_2018_X4b_v2ab_Haa4b_score_Nom',
    #'/eos/cms/store/user/ssawant/htoaa/analysis/20250317_CR_QCD4b_FullSyst/2018/CombineFit_inputFiles/CR4b_4M4T/CR4b_4M4T_QCD_4bAndMoreCat_2018.root' : 'CR4b_4M4T_QCD_4bAndMoreCat_2018_X4b_v2ab_Haa4b_score_Nom'

    ## finer binning for finer thresholds
#    '/eos/cms/store/user/ssawant/htoaa/analysis/20250502_CR_QCD4b_FullSyst/2018/CombineFit_inputFiles/CR4b_3M3T/CR4b_3M3T_QCD_4bAndMoreCat_2018.root' : ['CR4b_3M3T_QCD_4bAndMoreCat_2018_X4b_v2ab_Haa4b_score_Nom'],
#    '/eos/cms/store/user/ssawant/htoaa/analysis/20250502_CR_QCD4b_FullSyst/2018/CombineFit_inputFiles/CR4b_4M3T/CR4b_4M3T_QCD_4bAndMoreCat_2018.root' : ['CR4b_4M3T_QCD_4bAndMoreCat_2018_X4b_v2ab_Haa4b_score_Nom'],
#    '/eos/cms/store/user/ssawant/htoaa/analysis/20250502_CR_QCD4b_FullSyst/2018/CombineFit_inputFiles/CR4b_4M4T/CR4b_4M4T_QCD_4bAndMoreCat_2018.root' : ['CR4b_4M4T_QCD_4bAndMoreCat_2018_X4b_v2ab_Haa4b_score_Nom']

    #}

## bbqq

# fns = {
#     '/afs/cern.ch/work/c/csutanta/public/unskimmed_histograms/v1/lepjet/unskimmed_SingleMuon_bdtHi.root' :[
#         'evt/TTToSemiLeptonic_powheg_bbqq/particleNetMD_XbbOverQCD_sel_0b_BBQQ_central',
#         'evt/TTToSemiLeptonic_powheg_bbq/particleNetMD_XbbOverQCD_sel_0b_BBQQ_central',] ,
#     '/afs/cern.ch/work/c/csutanta/public/unskimmed_histograms/v1/lepjet/unskimmed_EGamma_bdtHi.root' : [
#         'evt/TTToSemiLeptonic_powheg_bbqq/particleNetMD_XbbOverQCD_sel_0b_BBQQ_central',
#         'evt/TTToSemiLeptonic_powheg_bbq/particleNetMD_XbbOverQCD_sel_0b_BBQQ_central']

#     }

## bbqq with new scale factor
# fns = {
#     '/afs/cern.ch/work/c/csutanta/public/unskimmed_histograms/v2_scalefactor/unskimmed_SingleMuon_bdtHi.root' :[
#         'evt/TTToSemiLeptonic_powheg_bbqq/particleNetMD_XbbOverQCD_sel_0b_BBQQ_central',
#         'evt/TTToSemiLeptonic_powheg_bbq/particleNetMD_XbbOverQCD_sel_0b_BBQQ_central',] ,
#     '/afs/cern.ch/work/c/csutanta/public/unskimmed_histograms/v2_scalefactor/unskimmed_EGamma_bdtHi.root' : [
#         'evt/TTToSemiLeptonic_powheg_bbqq/particleNetMD_XbbOverQCD_sel_0b_BBQQ_central',
#         'evt/TTToSemiLeptonic_powheg_bbq/particleNetMD_XbbOverQCD_sel_0b_BBQQ_central']

#     }

## X34b with new scale factor
# fns = {
#      '/afs/cern.ch/work/c/csutanta/public/unskimmed_histograms/v2_scalefactor/unskimmed_SingleMuon_bdtHi.root' :[
#          'evt/TTToSemiLeptonic_powheg_bbqq/PNet_X4b_v2_Haa34b_score_sel_0b_BBQQ_central',
#          'evt/TTToSemiLeptonic_powheg_bbq/PNet_X4b_v2_Haa34b_score_sel_0b_BBQQ_central',
#          ],
#          '/afs/cern.ch/work/c/csutanta/public/unskimmed_histograms/v2_scalefactor/unskimmed_EGamma_bdtHi.root' : [
#          'evt/TTToSemiLeptonic_powheg_bbqq/PNet_X4b_v2_Haa34b_score_sel_0b_BBQQ_central',
#          'evt/TTToSemiLeptonic_powheg_bbq/PNet_X4b_v2_Haa34b_score_sel_0b_BBQQ_central',
#          ]
#     }

## Xbb with new scale factor
fns = {
    ## 2018
    # 'eg': '/afs/cern.ch/work/c/csutanta/HTOAA_CMSSW/analysis/v1_202505_scalefactor/unskimmed_EGamma_bdtHi/2018/analyze_htoaa_stage1.root' ,
    # 'mu': '/afs/cern.ch/work/c/csutanta/HTOAA_CMSSW/analysis/v1_202505_scalefactor/unskimmed_singlemuon_bdtHi/2018/analyze_htoaa_stage1.root'

    ## 2017
    # 'eg' : '/afs/cern.ch/work/c/csutanta/HTOAA_CMSSW/analysis/v1_202505_scalefactor/unskimmed_egamma_1b_BBQ_BBQQ/2017/analyze_htoaa_stage1.root',
    # 'mu' : '/afs/cern.ch/work/c/csutanta/HTOAA_CMSSW/analysis/v1_202505_scalefactor/unskimmed_singlemuon_1b_BBQ_BBQQ/2017/analyze_htoaa_stage1.root',

    ## 2016pre
    'eg' : '/afs/cern.ch/work/c/csutanta/HTOAA_CMSSW/analysis/v1_202505_scalefactor/unskimmed_singlemuon_1b_BBQ_BBQQ/2016APV/analyze_htoaa_stage1.root',
    'mu' : '/afs/cern.ch/work/c/csutanta/HTOAA_CMSSW/analysis/v1_202505_scalefactor/unskimmed_egamma_1b_BBQ_BBQQ/2016APV/analyze_htoaa_stage1.root'

    ## 2016post
    # 'eg' : '/afs/cern.ch/work/c/csutanta/HTOAA_CMSSW/analysis/v1_202505_scalefactor/unskimmed_singlemuon_1b_BBQ_BBQQ/2016/analyze_htoaa_stage1.root',
    #'mu' : '/afs/cern.ch/work/c/csutanta/HTOAA_CMSSW/analysis/v1_202505_scalefactor/unskimmed_egamma_1b_BBQ_BBQQ/2016/analyze_htoaa_stage1.root'

}

## branches for 2018
# branches = [
#         'evt/TTToSemiLeptonic_powheg_bbqq/particleNetMD_XbbOverQCD_sel_0b_BBQQ_central',
#         'evt/TTToSemiLeptonic_powheg_bbq/particleNetMD_XbbOverQCD_sel_0b_BBQQ_central',
#         'evt/TTToSemiLeptonic_powheg_bb/particleNetMD_XbbOverQCD_sel_0b_BBQQ_central',
#         'evt/TTTo2L2Nu_powheg_bb/particleNetMD_XbbOverQCD_sel_0b_BBQQ_central'
# ]

## branches for 2016-2017
branches = [
         'evt/TTToSemiLeptonic_powheg_bbqq/particleNetMD_XbbOverQCD_sel_0b_BBQQ_bdtHi_central',
         'evt/TTToSemiLeptonic_powheg_bbq/particleNetMD_XbbOverQCD_sel_0b_BBQQ_bdtHi_central',
         'evt/TTToSemiLeptonic_powheg_bb/particleNetMD_XbbOverQCD_sel_0b_BBQQ_bdtHi_central',
         'evt/TTTo2L2Nu_powheg_bb/particleNetMD_XbbOverQCD_sel_0b_BBQQ_bdtHi_central'
]



print('threshold,efficiency')
thresholds = np.linspace(0,1,1001)

## sum hist from all branches and eg and mu together

histmu = 0
histeg = 0

for branch in branches:
    histmu = histmu + uproot.open(fns['mu'])[branch].values()
    leftedges = uproot.open(fns['mu'])[branch].axis().edges()[:-1]

    histeg = histeg + uproot.open(fns['eg'])[branch].values()



## calculate how many passes threshold
for threshold in thresholds:
    # print(threshold, np.sum(hist[leftedges > threshold])/np.sum(hist))
    mueff = np.sum(histmu[leftedges >= threshold])/np.sum(histmu)
    egeff = np.sum(histeg[leftedges >= threshold])/np.sum(histeg)


    print(f'{threshold},{(mueff+egeff)/2}')






### -------------------------------------- no scale factor -----------------------------------
# fmu = uproot.open('/afs/cern.ch/work/c/csutanta/public/unskimmed_histograms/v2/unskimmed_SingleMuon_bdtHi.root')
# feg = uproot.open('/afs/cern.ch/work/c/csutanta/public/unskimmed_histograms/v2/unskimmed_EGamma_bdtHi.root')
# branches = [
#     ## PNet_X4b_v2_Haa34b_score. signal is semilep bbqq, bbq
#     'evt/TTToSemiLeptonic_powheg_bbqq/PNet_X4b_v2_Haa34b_score_sel_0b_BBQQ_central',
#     'evt/TTToSemiLeptonic_powheg_bbq/PNet_X4b_v2_Haa34b_score_sel_0b_BBQQ_central',
# ]

# thresholds = np.linspace(0, 1, 1000)
# print('threshold,efficiency')
# for threshold in thresholds:
#     mupass = 0
#     mutot = 0
#     egpass = 0
#     egtot = 0
#     for branch in branches:
#         mubin = fmu[branch].values()
#         muedge = fmu[branch].axis().edges()
#         muedge = muedge[1:] ## we don't need to count edge = 0
#         mupass = mupass + np.sum(mubin[muedge > threshold])
#         mutot = mutot + mubin.sum()

#         egbin = feg[branch].values()
#         egedge = feg[branch].axis().edges()
#         egedge = egedge[1:] ## we don't need to count edge = 0
#         egpass = egpass + np.sum(egbin[egedge > threshold])
#         egtot = egtot + egbin.sum()



#     print(f'{threshold},{(mupass+egpass)/(mutot+egtot)}')


# ## use the bineed files

# eg = uproot.open('/afs/cern.ch/work/c/csutanta/HTOAA_CMSSW/CMSSW_14_1_0_pre4/src/HiggsAnalysis/CombinedLimit/AK8TaggerCalib/data/v1/lepjet/EGamma/AK8_tagger_calib_Xbb_0b_BBQQ_2p0_slc7.root')['Sum2B_bdtHi_Xbb'].values()
# mu = uproot.open('/afs/cern.ch/work/c/csutanta/HTOAA_CMSSW/CMSSW_14_1_0_pre4/src/HiggsAnalysis/CombinedLimit/AK8TaggerCalib/data/v1/lepjet/SingleMuon/AK8_tagger_calib_Xbb_0b_BBQQ_2p0_slc7.root')['Sum2B_bdtHi_Xbb'].values()

# print('the rebinned file')
# print(eg)
# print(mu)

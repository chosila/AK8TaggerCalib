#! /usr/bin/env python
## Counts events passing different tagger cuts

import os
import sys
import subprocess
import numpy as np
import ROOT as R
import json

R.gROOT.SetBatch(True)  ## Don't display histograms or canvases when drawn

MAX_EVT = -1     ## Maximum number of events to process per MC sample
PRT_EVT = 10000  ## Print every Nth event while processing
DEBUG   = False
MAS = ['60'] # ['12']+[str(mA*5) for mA in range(3,13)]  ## Signal "a" boson masses
#MAS = ['12','30','60']
# YEAR = '2016APV'

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('year', )
args = parser.parse_args()
YEAR = args.year

if YEAR == '2018':
    bfit = 0.76
    up   = .661
    down = 0.811
elif YEAR == '2017' :
    bfit = 0.743
    up = 0.621
    down = 0.8
elif YEAR == '2016':
    bfit = 0.63
    up   = 0
    down = 0.792
elif YEAR =='2016APV':
    bfit = 0.583
    up   = 0
    down = 0.808
else :
    print('define year please')



## Location of postprocessed input files

# IN_DIR = f'/eos/cms/store/group/phys_susy/HToaaTo4b/NanoAOD/{YEAR}/MC/PNet_v2_2024_11_22/'
## IN_DIR = '/eos/cms/store/group/phys_susy/HToaaTo4b/NanoAOD/2017/MC/PNet_v2_2024_11_22/'

## Count events passing tagger cuts
count = {}
for mA in MAS:
    count[mA] = {}
    for sys in ['den','nom','bfit','up','down']:
        count[mA][sys] = 0

print('\n\n*** Looping over all values of mA: ***')
print(MAS)
fns = json.load(open(f'Haa4b_signal_fileslist_{YEAR}.json'))# [YEAR]




for fn in fns:
    for mA in MAS:
        print('\n\n*** Beginning to look at mA = %s ***\n' % mA)
        in_file_name = fn#'/eos/cms/store/group/phys_susy/HToaaTo4b/NanoAOD/2016APV/MC/NanoAODv9/SUSY_GluGluH_01J_HToAATo4B_Pt150_M-57.5_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL16APVNanoAODv9/20241025_000000/0003/NanoAODv9_320_nEvents500.root'
        #if ('2018' in IN_DIR) or ('2016' in IN_DIR):
        #    in_file_name = IN_DIR+'SUSY_GluGluH_01J_HToAATo4B_Pt150_M-%s_TuneCP5_13TeV_madgraph_pythia8/r1/PNet_v1_Skim_Lp_weight.root' % mA
        #elif '2017' in IN_DIR:
        #    in_file_name = IN_DIR+'SUSY_GluGluH_01J_HToAATo4B_Pt150_M-%s_TuneCP5_13TeV_madgraph_pythia8/r2/PNet_v1_Skim_Lp_weight.root' % mA

        print('Adding file %s' % in_file_name)
        chains = {}
        chains['Events'] = R.TChain('Events')
        chains['Events'].Add(in_file_name)


        ## Loop through events, select, and count
        ch = chains['Events']  ## Shortcut expression
        nEntries = ch.GetEntries()
        print('\nEntering loop over %d events\n' % (nEntries))

        for iEvt in range(nEntries):

            if iEvt > MAX_EVT and MAX_EVT > 0: break
            if (iEvt % PRT_EVT) == 0: print('Looking at event #%d / %d' % (iEvt, nEntries))

            ch.GetEntry(iEvt)

            if DEBUG: print('Here!')
            if DEBUG: print(bool(ch.Haa4b_passFilters))

            for iF in range(ch.nFatJet):
                #if 0.5*(ch.FatJet_PNet_X4b_v2a_Haa4b_score[iF] +
                #        ch.FatJet_PNet_X4b_v2a_Haa4b_score[iF]) <= 0.93: continue  ## X4b WP60 cut
                if ch.FatJet_nBHadrons[iF] <   4  : continue  ## Only keep events with 4b or more
                if ch.FatJet_msoftdrop[iF] <=  60.: continue  ## Global soft-drop mass cut
                if ch.FatJet_mass[iF]      <= 110.: continue  ## mass requirement
                if ch.FatJet_pt[iF]        <= 250.: continue  ## pT cut for most categories
                if abs(ch.FatJet_eta[iF])  >= 2.4:  continue  ## Global eta cut
                if ch.FatJet_jetId[iF]      < 6:    continue  ## Global ID cut
                if DEBUG: print('Passed initial selection!')

                ## For Xbb thresholds, see https://docs.google.com/presentation/d/1vf0Bxjt_7Mn2OD-PHbih2Ba47RZObB4VBSj4ivq-4v4
                Xbb = ch.FatJet_particleNetMD_Xbb[iF] / (ch.FatJet_particleNetMD_Xbb[iF] + ch.FatJet_particleNetMD_QCD[iF]) # ch.FatJet_particleNetMD_XbbvsQCD[iF]
                count[mA]['den']  += 1
                count[mA]['nom']   += (Xbb > 0.75)
                count[mA]['bfit']  += (Xbb > bfit) # 0.745)
                count[mA]['up']   += (Xbb > up) # 0.645)
                count[mA]['down'] += (Xbb > down) # 0.804)

                break  ## Only consider 1 FatJet per event
            ## End loop: for iF in range(ch.nFatJet)
        ## End loop: for iEvt in range(nEntries)
        del chains
        print('mA = %s has nom efficiency %d / %d = %.2f%%' % (mA, count[mA]['nom'], count[mA]['den'], 100.*count[mA]['nom']/count[mA]['den']))
    ## End loop: for mA in MAS
## End loop: for fn in fns

print('\n\nFinal efficiencies:\n')
for mA in MAS:
    enom   = 100.*count[mA]['nom']   / count[mA]['den']
    eBfit  = 100.*count[mA]['bfit']  / count[mA]['den']
    eUp   = 100.*count[mA]['up']   / count[mA]['den']
    eDown = 100.*count[mA]['down'] / count[mA]['den']
    print('mA = %s efficiency in nom = %.2f%%, measured = %.2f%% +%.2f/%.2f%%' % (mA, enom, eBfit, eUp-eBfit, eDown-eBfit))
    print('  * SF (w.r.t. nom) Up = %.4f (%.4f), Down = %.4f (%.4f)' % (eUp/eBfit, eUp/enom, eDown/eBfit, eDown/enom))
## End loop: for mA in MAS

print('\n*** All done!!! ***\n\n')

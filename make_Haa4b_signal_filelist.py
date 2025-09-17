import glob
import json

masspoint_18 = [25,30,45,55,60]
masspoint_1617 = [27.5, 32.5, 42.5, 52.5, 57.5]

fns ={
    '2018' : '/eos/cms/store/group/phys_susy/HToaaTo4b/NanoAOD/2018/MC/NanoAODv9/SUSY_GluGluH_01J_HToAATo4B_Pt150_M-{mp}_TuneCP5_13TeV_madgraph_pythia8/106X_upgrade2018_realistic_v16_L1v1-v1/*/*root',

    '2017': '/eos/cms/store/group/phys_susy/HToaaTo4b/NanoAOD/2017/MC/NanoAODv9/SUSY_GluGluH_01J_HToAATo4B_Pt150_M-{mp}_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17NanoAODv9/20241025_000000/*/*root',

    '2016' : '/eos/cms/store/group/phys_susy/HToaaTo4b/NanoAOD/2016/MC/NanoAODv9/SUSY_GluGluH_01J_HToAATo4B_Pt150_M-{mp}_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL16NanoAODv9/20241025_000000/*/*root',

    '2016APV': '/eos/cms/store/group/phys_susy/HToaaTo4b/NanoAOD/2016APV/MC/NanoAODv9/SUSY_GluGluH_01J_HToAATo4B_Pt150_M-{mp}_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL16APVNanoAODv9/20241025_000000/*/*root'
}


flist = []
for mp in masspoint_18:
    flist = flist + glob.glob(fns['2018'].format(mp=mp))

fdict = {'2018' : flist}

with open('Haa4b_signal_fileslist_2018.json', 'w') as outf: json.dump(flist, outf, indent=4)


for fn in fns:
    if fn == '2018' : continue
    fdict[fn] = []
    for mp in masspoint_1617:
        fdict[fn] = fdict[fn] + glob.glob(fns[fn].format(mp=mp))

    with open(f'Haa4b_signal_fileslist_{fn}.json', 'w') as outf: json.dump(fdict[fn], outf, indent=4)
    #print(json.dumps(fdict[fn], indent=4))
    #print('------------------------------------------------------')

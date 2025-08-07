import uproot
import numpy as np


def f(v, dup, ddown):
    return (1/2)*((dup-ddown)*v+(1/8)*(dup+ddown)*(3*pow(v,6)-10*pow(v,4)+15*pow(v,2)))

if False:
    f40 = uproot.open('/afs/cern.ch/work/a/abrinke1/public/HiggsToAA/coffea/eventloop/plots/HtoAA_QCD_AK8_tagger_calib/AK8_tagger_calib_X4b_v2_WP40_2p0_slc7.root')
    f60 = uproot.open('/afs/cern.ch/work/a/abrinke1/public/HiggsToAA/coffea/eventloop/plots/HtoAA_QCD_AK8_tagger_calib/AK8_tagger_calib_X4b_v2_WP60_2p0_slc7.root')

    rebin = '4bin' #'cSB' #
    print('Efficiencies for rebin: ', rebin)


    if rebin == 'cSB':
        nom_branches = [f'Sum4B_cSB{x}_X4b_v2' for x in ['3M3T', '4M4T', '4M3T']] ## for cSB (3bin) calcualtion
        up_branches = [f'Sum4B_cSB{x}_X4b_v2_s4B_4binUp' for x in ['3M3T', '4M4T', '4M3T']]
        down_branches = [f'Sum4B_cSB{x}_X4b_v2_s4B_4binDown' for x in ['3M3T', '4M4T', '4M3T']]
        hist40 = np.array([0,0,0])
        hist60 = np.array([0,0,0])

        hist40up = np.array([0,0,0])
        hist60up = np.array([0,0,0])

        hist40down = np.array([0,0,0])
        hist60down = np.array([0,0,0])

    elif rebin == '4bin':
        nom_branches = [f'Sum4B_c{x}_X4b_v2' for x in ['3M3T', '4M4T', '4M3T']] ## for 4bin calcualtion
        up_branches = [f'Sum4B_c{x}_X4b_v2_s4B_4binUp' for x in ['3M3T', '4M4T', '4M3T']]
        down_branches = [f'Sum4B_c{x}_X4b_v2_s4B_4binDown' for x in ['3M3T', '4M4T', '4M3T']]

        hist40 = np.array([0,0,0,0])
        hist60 = np.array([0,0,0,0])

        hist40up = np.array([0,0,0,0])
        hist60up = np.array([0,0,0,0])

        hist40down = np.array([0,0,0,0])
        hist60down = np.array([0,0,0,0])

    else:
        print('rebin is defined wrong. Exiting.')
        exit()


    for nom_branch in nom_branches:
        hist40 = hist40 + f40[nom_branch].values()
        hist60 = hist60 + f60[nom_branch].values()
    for up_branch in up_branches:
        hist40up = hist40up + f40[up_branch].values()
        hist60up = hist60up + f60[up_branch].values()
    for down_branch in down_branches:
        hist40down = hist40down + f40[down_branch].values()
        hist60down = hist60down + f60[down_branch].values()


    nom40 = hist40[-1]/hist40.sum()
    nom60 = hist60[-1]/hist60.sum()
    dup40 = hist40up[-1]/hist40up.sum() - nom40#.5*(1-nom40)
    ddown40 = hist40down[-1]/hist40down.sum() - nom40 #nom40*nom40/(nom40+dup40) - nom40
    dup60 = hist60up[-1]/hist60up.sum() - nom60 #0.5*(1-nom60)
    ddown60 = hist60down[-1]/hist60down.sum() -nom60  # nom60*nom60/(nom60+dup60) - nom60
    print('---------------------------------- X4b QCD ----------------------------')
    print(f'nominal 40 : {nom40*100:.3f}% +{dup40*100:.3f} {ddown40*100:.3f}')
    print(f'nominal 60 : {nom60*100:.3f}% +{dup60*100:.3f} {ddown60*100:.3f}')

    if rebin == 'cSB':
        ##cSB
        mu40 = 0.14
        sup40 = 0.76
        sdown40 = -0.74
    elif rebin == '4bin':
        ## 4bin
        mu40 = -.62 # -0.57
        sup40 = -.34 # 0.04
        sdown40 = -.87 # -0.96

    nom40p = nom40+ f(mu40, dup40, ddown40)
    dup40p = f(sup40, dup40, ddown40) - f(mu40, dup40, ddown40)
    ddown40p = f(sdown40, dup40, ddown40) - f(mu40, dup40, ddown40)

    print(f'postfit 40: {nom40p*100:.3f}% +{dup40p*100:.3f} {ddown40p*100:.3f}')

    if rebin == 'cSB':
        ## cSB
        mu60 = -.3
        sup60 = 0.93
        sdown60 = -2.86
    elif rebin == '4bin':
        ## 4bin
        mu60 = .19
        sup60 = .48
        sdown60 = -0.14
    nom60p = nom60+ f(mu60, dup60, ddown60)
    dup60p = f(sup60, dup60, ddown60) - f(mu60, dup60, ddown60)
    ddown60p = f(sdown60, dup60, ddown60) - f(mu60, dup60, ddown60)

    print(f'postfit 60: {nom60p*100:.3f}% +{dup60p*100:.3f} {ddown60p*100:.3f}')



if False:
    print('--------------------------- bbqq vs 01b ------------------------')

    ## ------ no scale factor ------
    # nom60 = 0.645 ## got these from calculate_efficiency.py
    # dup60 = 0.177
    # ddown60 = -0.139
    # mu60 = 0.11
    # sup60 = 0.56
    # sdown60 = -0.34

    bbqq_vs_01b_wp = 60
    if bbqq_vs_01b_wp == 40:
        ## ----- wp40 scale factor ---
        # 39.9285 % + 30.0357 - 16.8683
        nom = 0.399285
        dup = 0.300356
        ddown = -0.168683
        mu = 0.05
        sup = 0.31
        sdown = -.22
    elif bbqq_vs_01b_wp == 60:
        ## ----- wp60 scale factor ----
        # 64.3634 % + 17.8183 - 13.8238
        nom = 0.643634
        dup = 0.178183
        ddown = -0.138238
        mu = 0.25
        sup = 0.70
        sdown = -.10
    else :
        print('bbqq vs 01b wp not defined correctly')


    nomp = nom+ f(mu, dup, ddown)
    dupp = f(sup, dup, ddown) - f(mu, dup, ddown)
    ddownp = f(sdown, dup, ddown) - f(mu, dup, ddown)

    print(f'postfit bbqq_vs_01b wp{bbqq_vs_01b_wp}: {nomp*100:.3f}% +{dupp*100:.3f} {ddownp*100:.3f}')



    # /afs/cern.ch/work/c/csutanta/HTOAA_CMSSW/CMSSW_14_1_0_pre4/src/HiggsAnalysis/CombinedLimit/AK8TaggerCalib/data/v2/bbqq_vs_01b/splitbkg_BB_BQQ_01B/WP40/EGamma/AK8_tagger_calib_TT_bbqq_vs_01b_0b_BBQQ_2p0_slc7.root
    # /afs/cern.ch/work/c/csutanta/HTOAA_CMSSW/CMSSW_14_1_0_pre4/src/HiggsAnalysis/CombinedLimit/AK8TaggerCalib/data/v2/bbqq_vs_01b/splitbkg_BB_BQQ_01B/WP40/SingleMuon/AK8_tagger_calib_TT_bbqq_vs_01b_0b_BBQQ_2p0_slc7.root


    nom40 = 0.408
    dup40 = 0.296
    ddown40 = -0.169
    mu40 = -.04
    sup40 = 0.23
    sdown40 = -0.35

    nom40p = nom40+ f(mu40, dup40, ddown40)
    dup40p = f(sup40, dup40, ddown40) - f(mu40, dup40, ddown40)
    ddown40p = f(sdown40, dup40, ddown40) - f(mu40, dup40, ddown40)

    print(f'postfit 40: {nom40p*100:.3f}% +{dup40p*100:.3f} {ddown40p*100:.3f}')




if False:

    ## --------------------- this X4b_v2_Haa34b using TTBar -------------------------
    x34b_wp = 80
    mufile = uproot.open(f'data/v2_scalefactor/X4b_TTbar/SingleMuon/AK8_tagger_calib_X4b_v2_Haa34b_0b_WP{x34b_wp}_2p0_slc7.root')
    egfile = uproot.open(f'data/v2_scalefactor/X4b_TTbar/EGamma/AK8_tagger_calib_X4b_v2_Haa34b_0b_WP{x34b_wp}_2p0_slc7.root')
    nom_branch = 'Sum2B2Q_bdtHi_X4b_v2_Haa34b'
    up_branch = 'Sum2B2Q_bdtHi_X4b_v2_Haa34b_s2B2Q_4binUp'
    down_branch = 'Sum2B2Q_bdtHi_X4b_v2_Haa34b_s2B2Q_4binDown'
    mu = mufile[nom_branch].values()
    eg = egfile[nom_branch].values()

    muup = mufile[up_branch].values()
    mudown = mufile[down_branch].values()

    egup = egfile[up_branch].values()
    egdown = egfile[down_branch].values()


    nom = (1/2) * (mu[-1]/np.sum(mu) + eg[-1]/np.sum(eg))
    dup = (1/2) * (muup[-1]/np.sum(muup) + egup[-1]/np.sum(egup)) - nom
    ddown = (1/2) * (mudown[-1]/np.sum(mudown) + egdown[-1]/np.sum(egdown)) - nom
    mu = -.01
    sup = 0.54
    sdown = -1.02

    nomp = nom+ f(mu, dup, ddown)
    dupp = f(sup, dup, ddown) - f(mu, dup, ddown)
    ddownp = f(sdown, dup, ddown) - f(mu, dup, ddown)

    print('-------------------------------')
    print(f'prefit X34b WP{x34b_wp}: {nom*100:.3f}% +{dup*100:.3f} {ddown*100:.3f}')
    print(f'postfit X34b WP{x34b_wp}: {nomp*100:.3f}% +{dupp*100:.3f} {ddownp*100:.3f}')



if False:

    ## -------------------- Xbb with scale factor -------------------------------
    # 69.3467 % + 15.3266 - 12.4532
    del mu, eg, muup, mudown, egup, egdown
    mufile = uproot.open(f'data/v1_scalefactor/SingleMuon/AK8_tagger_calib_Xbb_0b_BBQQ_2p0_slc7.root')
    egfile = uproot.open(f'data/v1_scalefactor/EGamma/AK8_tagger_calib_Xbb_0b_BBQQ_2p0_slc7.root')
    nom_branch = 'Sum2B_bdtHi_Xbb'
    up_branch = 'Sum2B_bdtHi_Xbb_s2B_4binUp'
    down_branch = 'Sum2B_bdtHi_Xbb_s2B_4binDown'
    mu = mufile[nom_branch].values()
    eg = egfile[nom_branch].values()

    muup = mufile[up_branch].values()
    mudown = mufile[down_branch].values()

    egup = egfile[up_branch].values()
    egdown = egfile[down_branch].values()


    nom = (1/2) * (mu[-1]/np.sum(mu) + eg[-1]/np.sum(eg))
    dup = (1/2) * (muup[-1]/np.sum(muup) + egup[-1]/np.sum(egup)) - nom
    ddown = (1/2) * (mudown[-1]/np.sum(mudown) + egdown[-1]/np.sum(egdown)) - nom
    mu = -.1
    sup = 0.47
    sdown = -0.61

    nomp = nom+ f(mu, dup, ddown)
    dupp = f(sup, dup, ddown) - f(mu, dup, ddown)
    ddownp = f(sdown, dup, ddown) - f(mu, dup, ddown)
    print('-------------------------------')
    print(f'prefit Xbb : {nom*100:.3f}% +{dup*100:.3f} {ddown*100:.3f}')
    print(f'postfit Xbb : {nomp*100:.3f}% +{dupp*100:.3f} {ddownp*100:.3f}')




if True:
    ## ------------------------- X4b runII ---------------------------------------------------
    WPs = [40, 60]

    # 60 : 0.62 [0.41, 0.99]
    # 40 : 0.36 [0.14, 0.64]

    for wp in WPs:
        fdata = uproot.open(f'data/v2_scalefactor/runII/X4b/AK8_tagger_calib_X4b_v2_WP{wp}_2p0_slc7.root')
        nom_h = fdata['Sum4B_c4M4T_X4b_v2'].values()
        dup_h = fdata['Sum4B_c4M4T_X4b_v2_s4B_4binUp'].values()
        ddown_h = fdata['Sum4B_c4M4T_X4b_v2_s4B_4binDown'].values()

        nom = nom_h[-1]/nom_h.sum()
        dup = dup_h[-1]/dup_h.sum() - nom
        ddown = ddown_h[-1]/ddown_h.sum() - nom

        if wp == 40:
            mu    = 0.36
            sup   = 0.64
            sdown = 0.14
        elif wp == 60:
            mu    = 0.62
            sup   = 0.99
            sdown = 0.41
        else:
            print('bro what did u do')
            exit()
        nomp = nom + f(mu, dup, ddown)
        dupp = f(sup, dup, ddown) - f(mu, dup, ddown)
        ddownp = f(sdown, dup, ddown) - f(mu, dup, ddown)

        print('--------------------------------------------')
        print(f'prefit X4b  WP{wp}: {nom*100:.3f}% +{dup*100:.3f} {ddown*100:.3f}')
        print(f'postfit X4b WP{wp}: {nomp*100:.3f}% +{dupp*100:.3f} {ddownp*100:.3f}')

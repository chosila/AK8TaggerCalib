import uproot
import numpy as np


def f(v, dup, ddown):
    return (1/2)*((dup-ddown)*v+(1/8)*(dup+ddown)*(3*pow(v,6)-10*pow(v,4)+15*pow(v,2)))


f40 = uproot.open('/afs/cern.ch/work/a/abrinke1/public/HiggsToAA/coffea/eventloop/plots/HtoAA_QCD_AK8_tagger_calib/AK8_tagger_calib_X4b_v2_WP40_2p0_slc7.root')
f60 = uproot.open('/afs/cern.ch/work/a/abrinke1/public/HiggsToAA/coffea/eventloop/plots/HtoAA_QCD_AK8_tagger_calib/AK8_tagger_calib_X4b_v2_WP60_2p0_slc7.root')

rebin = '4bin' #'cSB' #
print('Efficiencies for rebin: ', rebin)

if rebin == 'cSB':
    branches = [f'Sum4B_cSB{x}_X4b_v2' for x in ['3M3T', '4M4T', '4M3T']] ## for cSB (3bin) calcualtion
    hist40 = np.array([0,0,0])
    hist60 = np.array([0,0,0])
elif rebin == '4bin':
    branches = [f'Sum4B_c{x}_X4b_v2' for x in ['3M3T', '4M4T', '4M3T']] ## for 4bin calcualtion
    hist40 = np.array([0,0,0,0])
    hist60 = np.array([0,0,0,0])
else:
    print('rebin is defined wrong. Exiting.')
    exit()


for branch in branches:
    hist40 = hist40 + f40[branch].values()
    hist60 = hist60 + f60[branch].values()


nom40 = hist40[-1]/hist40.sum()
nom60 = hist60[-1]/hist60.sum()
dup40 = 0.5*(1-nom40)
ddown40 = nom40*nom40/(nom40+dup40) - nom40
dup60 = 0.5*(1-nom60)
ddown60 = nom60*nom60/(nom60+dup60) - nom60
print(f'nominal 40 : {nom40*100:.3f}% +{dup40*100:.3f} {ddown40*100:.3f}')
print(f'nominal 60 : {nom60*100:.3f}% +{dup60*100:.3f} {ddown60*100:.3f}')

if rebin == 'cSB':
    ##cSB
    mu40 = 0.14
    sup40 = 0.76
    sdown40 = -0.74
elif rebin == '4bin':
    ## 4bin
    mu40 = -0.57
    sup40 = 0.04
    sdown40 = -0.96

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




exit()

## this X4b_v2_Haa34b using TTBar
mu = uproot.open('data/v2/X4b_TTbar/SingleMuon/AK8_tagger_calib_X4b_v2_Haa34b_0b_WP80_2p0_slc7.root')['Sum2B2Q_bdtHi_X4b_v2_Haa34b'].values()
eg = uproot.open('data/v2/X4b_TTbar/EGamma/AK8_tagger_calib_X4b_v2_Haa34b_0b_WP80_2p0_slc7.root')['Sum2B2Q_bdtHi_X4b_v2_Haa34b'].values()

mudown = uproot.open('data/v2/X4b_TTbar/SingleMuon/AK8_tagger_calib_X4b_v2_Haa34b_0b_WP80_2p0_slc7.root')['Sum2B2Q_bdtHi_X4b_v2_Haa34b_s2B2Q_4binDown'].values()

eff = (1/2) * (mu[-1]/np.sum(mu) + eg[-1]/np.sum(eg))
dup = eff*2 - eff ## this is one of the two defnition. look at the HtoAA_...py to check for true deifnition
ddown = eff/2 - eff ## same as above

print('prefit, up, down')
print(eff)
print(dup)
print(ddown)



print('postfit, up, down')
print(eff + f(-0.01, dup, ddown))
print(f(0.54, dup, ddown)-f(-0.01, dup,ddown))
print(f(-.98, dup, ddown)-f(-0.01, dup,ddown))


nom = 0.645
dup = .177
ddown  = -0.139

print(f'{nom+f(0.1, dup, ddown)=}')
print(f'{f(0.53, dup, ddown) - f(0.1, dup,ddown)=}')
print(f'{f(-0.34, dup, ddown) - f(0.1, dup,ddown)=}')


## for Xbb efficiency calibration
nom = 0.688
dup = 0.156
ddown = -0.127
mu = 0.049
sup = 0.64
sdown = -0.46

print('xbb efficiency')
print('ep prime : ', nom+f(mu, dup, ddown))
print('delta up prime: ', f(sup, dup, ddown) - f(mu, dup, ddown))
print('delta down prime: ', f(sdown, dup, ddown) - f(mu, dup,ddown))

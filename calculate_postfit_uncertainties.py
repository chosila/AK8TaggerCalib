import uproot
import numpy as np


def f(v, delta_up, delta_down):
    return (1/2)*((delta_up-delta_down)*v+(1/8)*(delta_up+delta_down)*(3*pow(v,6)-10*pow(v,4)+15*pow(v,2)))

rootfile = 'data/v1/lepjet/SingleMuon/AK8_tagger_calib_Xbb_0b_BBQQ_2p0_slc7.root'
signal_branch_name = 'Sum2B_bdtHi_Xbb'
syst_branch_name = 'Sum2B_bdtHi_Xbb_s2B'
mu = -0.12 # mu from deltaNLL plot
sigma_up = 0.18 # right crossing of deltaNLL plot
sigma_down  = -0.40 # left crossing of deltaNLL plot


rootfile = uproot.open(rootfile)
## get the nominal prefit
nominal_hist = rootfile[signal_branch_name].values()
nominal = nominal_hist[-1]/nominal_hist.sum()
## up uncertainty prefit
delta_up_hist = rootfile[f'{syst_branch_name}_4binUp'].values()
delta_up = delta_up_hist[-1]/delta_up_hist.sum() - nominal
## down uncertainty prefit. This value will be negative
delta_down_hist = rootfile[f'{syst_branch_name}_4binDown'].values()
delta_down = delta_down_hist[-1]/delta_down_hist.sum() - nominal

postfit_nominal = nominal + f(mu, delta_up, delta_down)
postfit_up = f(sigma_up, delta_up, delta_down) - f(mu, delta_up, delta_down)
postfit_down = f(sigma_down, delta_up, delta_down) - f(mu, delta_up, delta_down)

print(f'postfit : {postfit_nominal*100:.3f}% +{postfit_up*100:.3f} {postfit_down*100:.3f}')

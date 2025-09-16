## from TTG longexercise at DAS 2023 https://github.com/jennetd/TTGamma_LongExercise/blob/main2023/MakePostfitFigures.ipynb
import uproot
import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
plt.style.use(hep.style.CMS)


def add_uncertainty(hist, ax, ratio=False):
    opts = {'step': 'post', 'label': 'Uncertainty', 'hatch': '///',
                    'facecolor': 'none', 'edgecolor': (0, 0, 0, .5), 'linewidth': 0, 'zorder':10.}

    if ratio:
        down = np.ones(len(hist.counts())) - hist.errors()/hist.counts()
        up = np.ones(len(hist.counts())) + hist.errors()/hist.counts()
    else:
        down = hist.counts()-hist.errors()
        up =   hist.counts()+hist.errors()

        ax.fill_between(x=hist.axes[0].edges(), y1=np.r_[down, down[-1]], y2=np.r_[up, up[-1]], **opts)





def make_plots(dc_sr):
    h = dc_sr['data']
    #processes = ['Sum0b', 'Sum1B', 'Sum2B']
    processes = ['Sum01B', 'SumBB', 'SumBQQ', 'Sum2B2Q']
    #processes = ['Sum4B', 'Sum3B', 'Sum012B', 'SumTWZ']

    fig, ax = plt.subplots(figsize=(9,6))
    hep.cms.label(
        "Preliminary",
        data=True,
        # lumi=59.83,
        loc=0,
        ax=ax,
    )
    hep.histplot(
        [ dc_sr[x].counts() for x in processes ],
        dc_sr['total'].axes[0].edges(),
        histtype="fill",
        stack=True,
        label=processes,
        ax=ax
    )
    hep.histplot(
        dc_sr['data'].values()[1],
        dc_sr['total'].axes[0].edges(),
        w2=dc_sr['data'].values()[1],
        histtype="errorbar",
        stack=False,
        label='Observation',
        color='black',
        ax=ax
    )


    ax.set_ylabel(r'Events')
    add_uncertainty(dc_sr['total'],  ax)
    ax.legend()
    labels = [item.get_text() for item in ax.get_xticklabels()]

    ax.set_xticks(range(0,5)) # used for to avoid this error: UserWarning: FixedFormatter should only be used together with FixedLocator

    ## bbqq vs 01 b tick and axes label
    #ax.set_xticklabels([0.0, 0.40,0.66,0.93, 1.0]) # x34b WP60
    #ax.set_xlabel('bbqq_vs_01b WP60', loc='right')
    #ax.set_xticklabels([0.0, 0.40, 0.84, 0.96, 1.0]) # x34b WP40

    #ax.set_xticklabels([0.0, 0.10,0.40,0.84, 1.0]) # x34b WP80
    #ax.set_xlabel('X34b WP80', loc='right')



    #ax.set_xticklabels([0.0, 0.1, 0.5, 0.75, 1.0]) ## v1 Xbb axis label and tick label
    #ax.set_xlabel('ParticleNet Xbb vs. QCD')

    return fig,ax


fns = {
    #'fitDiagnosticsX34b_ttbar_WP80_sf.root' : ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],

    #2017
    #'fitDiagnosticsX34b_2017_WP80.root' : ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],
    #'fitDiagnosticsX34b_2017_WP60.root' : ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],
    #'fitDiagnosticsX34b_2017_WP40.root' : ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],

    # 2016
    #'fitDiagnosticsX34b_2016_WP80.root' :  ['postVFP_mu_zerob_bdtHi', 'postVFP_mu_zerob_bdtMed', 'postVFP_mu_zerob_bdtLo', 'postVFP_mu_zerob_bdtVeto', 'postVFP_mu_oneb','postVFP_eg_zerob_bdtHi', 'postVFP_eg_zerob_bdtMed', 'postVFP_eg_zerob_bdtLo', 'postVFP_eg_zerob_bdtVeto', 'postVFP_eg_oneb', 'preVFP_mu_zerob_bdtHi', 'preVFP_mu_zerob_bdtMed', 'preVFP_mu_zerob_bdtLo', 'preVFP_mu_zerob_bdtVeto', 'preVFP_mu_oneb','preVFP_eg_zerob_bdtHi', 'preVFP_eg_zerob_bdtMed', 'preVFP_eg_zerob_bdtLo', 'preVFP_eg_zerob_bdtVeto', 'preVFP_eg_oneb'],

    # 'fitDiagnosticsX34b_2016_WP80_preVFP.root' :  ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],
    # 'fitDiagnosticsX34b_2016_WP60_preVFP.root' :  ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],
    # 'fitDiagnosticsX34b_2016_WP40_preVFP.root' :  ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],

    # 'fitDiagnosticsX34b_2016_WP80_postVFP.root' :  ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],
    # 'fitDiagnosticsX34b_2016_WP60_postVFP.root' :  ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],
    # 'fitDiagnosticsX34b_2016_WP40_postVFP.root' :  ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],

    ## ------- full run II one root input ----------
    'fitDiagnosticsX34b_runII_WP80_unmerged.root' :  ['y2016_postVFP_eg_oneb', 'y2016_postVFP_eg_zerob_bdtHi', 'y2016_postVFP_eg_zerob_bdtLo', 'y2016_postVFP_eg_zerob_bdtMed', 'y2016_postVFP_eg_zerob_bdtVeto', 'y2016_postVFP_mu_oneb', 'y2016_postVFP_mu_zerob_bdtHi', 'y2016_postVFP_mu_zerob_bdtLo', 'y2016_postVFP_mu_zerob_bdtMed', 'y2016_postVFP_mu_zerob_bdtVeto', 'y2016_preVFP_eg_oneb', 'y2016_preVFP_eg_zerob_bdtHi', 'y2016_preVFP_eg_zerob_bdtLo', 'y2016_preVFP_eg_zerob_bdtMed', 'y2016_preVFP_eg_zerob_bdtVeto', 'y2016_preVFP_mu_oneb', 'y2016_preVFP_mu_zerob_bdtHi', 'y2016_preVFP_mu_zerob_bdtLo', 'y2016_preVFP_mu_zerob_bdtMed', 'y2016_preVFP_mu_zerob_bdtVeto', 'y2017_eg_oneb', 'y2017_eg_zerob_bdtHi', 'y2017_eg_zerob_bdtLo', 'y2017_eg_zerob_bdtMed', 'y2017_eg_zerob_bdtVeto', 'y2017_mu_oneb', 'y2017_mu_zerob_bdtHi', 'y2017_mu_zerob_bdtLo', 'y2017_mu_zerob_bdtMed', 'y2017_mu_zerob_bdtVeto', 'y2018_eg_oneb', 'y2018_eg_zerob_bdtHi', 'y2018_eg_zerob_bdtLo', 'y2018_eg_zerob_bdtMed', 'y2018_eg_zerob_bdtVeto', 'y2018_mu_oneb', 'y2018_mu_zerob_bdtHi', 'y2018_mu_zerob_bdtLo', 'y2018_mu_zerob_bdtMed', 'y2018_mu_zerob_bdtVeto'],
    'fitDiagnosticsX34b_runII_WP80_merged.root' :  ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],
    #'fitDiagnosticsX34b_runII_WP60.root' :  ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],
    #'fitDiagnosticsX34b_runII_WP40.root' :  ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],

}

for fn in fns:
    for branch in fns[fn]:

        fitDiagnostics = uproot.open(fn)


        dc_sr = fitDiagnostics[f'shapes_prefit/{branch}']
        fig, ax = make_plots(dc_sr)
        pltname = f"{fn.removesuffix('.root').removeprefix('fitDiagnostics')}_{branch}"
        if 'WP40' in fn:
             ax.set_xticklabels([0.0, 0.40, 0.84, 0.96, 1.0])
             ax.set_xlabel('X34b WP40', loc='right')
        elif 'WP60' in fn:
            ax.set_xticklabels([0.0, 0.40,0.66,0.93, 1.0])
            ax.set_xlabel('X34b WP60', loc='right')
        elif 'WP80' in fn:
            ax.set_xticklabels([0.0, 0.10,0.40,0.84, 1.0])
            ax.set_xlabel('X34b WP80', loc='right')

        ax.set_title(pltname, y=1.1)
        # fig.savefig(f'plots/v2/pre_post_Fits/prefit_{pltname}.png', bbox_inches='tight')
        #fig.savefig(f'plots/v2/combinedbkg_test/prefit_{pltname}.png', bbox_inches='tight')
        fig.savefig(f'tmp/prefit_{pltname}.png', bbox_inches='tight')


        dc_sr = fitDiagnostics[f'shapes_fit_s/{branch}']
        fig, ax = make_plots(dc_sr)
        pltname = f"{fn.removesuffix('.root').removeprefix('fitDiagnostics')}_{branch}"
        if 'WP40' in fn:
             ax.set_xticklabels([0.0, 0.40, 0.84, 0.96, 1.0])
             ax.set_xlabel('X34b WP40', loc='right')
        elif 'WP60' in fn:
            ax.set_xticklabels([0.0, 0.40,0.66,0.93, 1.0])
            ax.set_xlabel('X34b WP60', loc='right')
        elif 'WP80' in fn:
            ax.set_xticklabels([0.0, 0.10,0.40,0.84, 1.0])
            ax.set_xlabel('X34b WP80', loc='right')

        ax.set_title(pltname, y=1.1)
        # fig.savefig(f'plots/v2/pre_post_Fits/postfit_{pltname}.png', bbox_inches='tight')
        # fig.savefig(f'plots/v2/combinedbkg_test/postfit_{pltname}.png', bbox_inches='tight')
        fig.savefig(f'tmp/postfit_{pltname}.png', bbox_inches='tight')



        plt.close('all')
import sys
sys.exit()

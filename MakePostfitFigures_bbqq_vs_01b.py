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
    processes = ['Sum01B', 'SumBB', 'SumBQQ', 'Sum2B2Q']

    fig, ax = plt.subplots(figsize=(9,6))
    hep.cms.label(
        "Preliminary",
        data=True,
        # lumi=59.83, #2018
        # lumi = 41.48, #2017
        # lumi = 16.8,  # 2016 post vfp
        # lumi = 19.5  #2016 pre vfp
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


    return fig,ax


fns = {
    # 'fitDiagnosticsbbqq_vs_01b_WP60_sf.root' : ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],
    #'fitDiagnosticsbbqq_vs_01b_2017_WP40.root' : ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],
    #'fitDiagnosticsbbqq_vs_01b_2017_WP60.root' : ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],


    #'fitDiagnosticsbbqq_vs_01b_2016_WP40.root' : ['preVFP_mu_zerob_bdtHi', 'preVFP_mu_zerob_bdtMed', 'preVFP_mu_zerob_bdtLo', 'preVFP_mu_zerob_bdtVeto', 'preVFP_mu_oneb','preVFP_eg_zerob_bdtHi', 'preVFP_eg_zerob_bdtMed', 'preVFP_eg_zerob_bdtLo', 'preVFP_eg_zerob_bdtVeto', 'preVFP_eg_oneb', 'postVFP_mu_zerob_bdtHi', 'postVFP_mu_zerob_bdtMed', 'postVFP_mu_zerob_bdtLo', 'postVFP_mu_zerob_bdtVeto', 'postVFP_mu_oneb','postVFP_eg_zerob_bdtHi', 'postVFP_eg_zerob_bdtMed', 'postVFP_eg_zerob_bdtLo', 'postVFP_eg_zerob_bdtVeto', 'postVFP_eg_oneb'],
    #'fitDiagnosticsbbqq_vs_01b_2016_WP60.root' : ['preVFP_mu_zerob_bdtHi', 'preVFP_mu_zerob_bdtMed', 'preVFP_mu_zerob_bdtLo', 'preVFP_mu_zerob_bdtVeto', 'preVFP_mu_oneb','preVFP_eg_zerob_bdtHi', 'preVFP_eg_zerob_bdtMed', 'preVFP_eg_zerob_bdtLo', 'preVFP_eg_zerob_bdtVeto', 'preVFP_eg_oneb', 'postVFP_mu_zerob_bdtHi', 'postVFP_mu_zerob_bdtMed', 'postVFP_mu_zerob_bdtLo', 'postVFP_mu_zerob_bdtVeto', 'postVFP_mu_oneb','postVFP_eg_zerob_bdtHi', 'postVFP_eg_zerob_bdtMed', 'postVFP_eg_zerob_bdtLo', 'postVFP_eg_zerob_bdtVeto', 'postVFP_eg_oneb'],

    'fitDiagnosticsbbqq_vs_01b_2016_WP40_preVFP.root' : ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],
    'fitDiagnosticsbbqq_vs_01b_2016_WP60_preVFP.root' : ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],

    'fitDiagnosticsbbqq_vs_01b_2016_WP40_postVFP.root' : ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],
    'fitDiagnosticsbbqq_vs_01b_2016_WP60_postVFP.root' : ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],

    ## the dictionary is in the form of
    # '<path to fitDiagnostics output.root' : ['combine channel1', 'channel 2', 'channel 3'...]
}

for fn in fns:
    for branch in fns[fn]:

        fitDiagnostics = uproot.open(fn)


        dc_sr = fitDiagnostics[f'shapes_prefit/{branch}']
        fig, ax = make_plots(dc_sr)
        pltname = f"{fn.removesuffix('.root').removeprefix('fitDiagnostics')}_{branch}"
        if 'WP40' in fn:
             ax.set_xticklabels([0.0, 0.2, 0.5, 0.9, 1.0]) # bbqq_vs_01b WP40
             ax.set_xlabel('bbqq_vs_01b WP40', loc='right')
        elif 'WP60' in fn:
            ax.set_xticklabels([0.0, 0.2, 0.5, 0.8, 1.0]) # bbqq_vs_01b WP60
            ax.set_xlabel('bbqq_vs_01b WP60', loc='right')
        ax.set_title(pltname, y=1.1)
        fig.savefig(f'tmp/prefit_{pltname}.png', bbox_inches='tight')


        dc_sr = fitDiagnostics[f'shapes_fit_s/{branch}']
        fig, ax = make_plots(dc_sr)
        pltname = f"{fn.removesuffix('.root').removeprefix('fitDiagnostics')}_{branch}"
        if 'WP40' in fn:
             ax.set_xticklabels([0.0, 0.2, 0.5, 0.9, 1.0]) # bbqq_vs_01b WP40
             ax.set_xlabel('bbqq_vs_01b WP40', loc='right')
        elif 'WP60' in fn:
            ax.set_xticklabels([0.0, 0.2, 0.5, 0.8, 1.0]) # bbqq_vs_01b WP60
            ax.set_xlabel('bbqq_vs_01b WP60', loc='right')

        ax.set_title(pltname, y=1.1)
        fig.savefig(f'tmp/postfit_{pltname}.png', bbox_inches='tight')
        print('saved', pltname)



        plt.close('all')
import sys
sys.exit()

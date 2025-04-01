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
    # processes = ['Sum01B', 'SumBB', 'SumBQQ', 'Sum2B2Q']
    processes = ['Sum4B', 'Sum3B', 'Sum012B', 'SumTWZ']
    fig, ax = plt.subplots(figsize=(9,6))
    hep.cms.label(
        "Preliminary",
        data=True,
        lumi=59.83,
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
        #w2=dc_sr['data'].values()[1],
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

    ax.set_xticks(range(0,5)) # to avoid this error: UserWarning: FixedFormatter should only be used together with FixedLocator

    ax.set_xticklabels([0.0, 0.40, 0.66, 0.93, 1.0]) # for 60
    #ax.set_xticklabels([0.0, 0.40, 0.84, 0.96, 1.0]) # for 40
    ax.set_xlabel('X4b WP60', loc='right')
    return fig,ax

#fitDiagnostics = uproot.open('fitDiagnosticsSM+EG_Xbb_0b+1b_BBQQ.root')
#branches = ['SM_zerob_bdtHi', 'EG_zerob_bdtHi']

#fitDiagnostics = uproot.open('fitDiagnosticsSingleMuon_Xbb_0b+1b_BBQQ.root')
#fitDiagnostics = uproot.open('fitDiagnosticsEGamma_Xbb_0b+1b_BBQQ.root')
#branches = ['zerob_bdtHi']


fns = {
    #'fitDiagnosticssBQQ_sBB_1p00.root' : ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],
    'fitDiagnosticsX4b_WP60.root' : [ 'c3M2T', 'c3M3T', 'c4M3T', 'c4M4T']
    #'fitDiagnosticsmu_0b+1b_TT_bbqq_vs_01b.root' : ['zerob_bdtHi', 'zerob_bdtMed', 'zerob_bdtLo', 'zerob_bdtVeto', 'oneb'],
    #'fitDiagnosticseg_0b+1b_TT_bbqq_vs_01b.root' : ['zerob_bdtHi', 'zerob_bdtMed', 'zerob_bdtLo', 'zerob_bdtVeto', 'oneb']
}

for fn in fns:
    for branch in fns[fn]:
        fitDiagnostics = uproot.open(fn)
        dc_sr = fitDiagnostics[f'shapes_fit_s/{branch}']
        fig, ax = make_plots(dc_sr)
        pltname = f"{fn.removesuffix('.root').removeprefix('fitDiagnostics')}_{branch}"
        ax.set_title(pltname, y=1.1)
        # fig.savefig(f'plots/v2/pre_post_Fits/postfit_{pltname}.png', bbox_inches='tight')
        # fig.savefig(f'plots/v2/combinedbkg_test/postfit_{pltname}.png', bbox_inches='tight')
        fig.savefig(f'tmp/postfit_{pltname}_WP60.png', bbox_inches='tight')

        dc_sr = fitDiagnostics[f'shapes_prefit/{branch}']

        print(branch)
        processes = ['Sum4B']#['Sum4B', 'Sum3B', 'Sum012B', 'SumTWZ']
        print('counts: ', [ dc_sr[x].counts() for x in processes ])
        print('values: ', [ dc_sr[x].counts() for x in processes ])
        print('----------------------------------')

        fig, ax = make_plots(dc_sr)
        pltname = f"{fn.removesuffix('.root').removeprefix('fitDiagnostics')}_{branch}"
        ax.set_title(pltname, y=1.1)
        # fig.savefig(f'plots/v2/pre_post_Fits/prefit_{pltname}.png', bbox_inches='tight')

        #fig.savefig(f'plots/v2/combinedbkg_test/prefit_{pltname}.png', bbox_inches='tight')
        fig.savefig(f'tmp/prefit_{pltname}_WP60.png', bbox_inches='tight')

        plt.close('all')
import sys
sys.exit()

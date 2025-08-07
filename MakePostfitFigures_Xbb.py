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
    processes = ['Sum0b', 'Sum1B', 'Sum2B']
    # processes = ['Sum01B', 'SumBB', 'SumBQQ', 'Sum2B2Q']
    #processes = ['Sum4B', 'Sum3B', 'Sum012B', 'SumTWZ']

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

    ax.set_xlabel('Xbb', loc='right')

    ax.set_xticklabels([0.0, 0.1, 0.5, 0.75, 1.0]) ## v1 Xbb axis label and tick label
    #ax.set_xlabel('ParticleNet Xbb vs. QCD')

    return fig,ax


fns = {
    'fitDiagnosticsXbb_TTbar_sf.root' : ['Mu_zerob_bdtHi', 'Mu_zerob_bdtMed', 'Mu_zerob_bdtLo', 'Mu_zerob_bdtVeto', 'Mu_oneb','EG_zerob_bdtHi', 'EG_zerob_bdtMed', 'EG_zerob_bdtLo', 'EG_zerob_bdtVeto', 'EG_oneb'],
}

for fn in fns:
    for branch in fns[fn]:

        fitDiagnostics = uproot.open(fn)


        dc_sr = fitDiagnostics[f'shapes_prefit/{branch}']
        fig, ax = make_plots(dc_sr)
        pltname = f"{fn.removesuffix('.root').removeprefix('fitDiagnostics')}_{branch}"
        ax.set_title(pltname, y=1.1)
        # fig.savefig(f'plots/v2/pre_post_Fits/prefit_{pltname}.png', bbox_inches='tight')
        #fig.savefig(f'plots/v2/combinedbkg_test/prefit_{pltname}.png', bbox_inches='tight')
        fig.savefig(f'tmp/prefit_{pltname}.png', bbox_inches='tight')


        dc_sr = fitDiagnostics[f'shapes_fit_s/{branch}']
        fig, ax = make_plots(dc_sr)
        pltname = f"{fn.removesuffix('.root').removeprefix('fitDiagnostics')}_{branch}"
        ax.set_title(pltname, y=1.1)
        # fig.savefig(f'plots/v2/pre_post_Fits/postfit_{pltname}.png', bbox_inches='tight')
        # fig.savefig(f'plots/v2/combinedbkg_test/postfit_{pltname}.png', bbox_inches='tight')
        fig.savefig(f'tmp/postfit_{pltname}.png', bbox_inches='tight')



        plt.close('all')
import sys
sys.exit()

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
    processes = ['Sum01B', 'Sum2B', 'Sum2B2Q']
    fig, ax = plt.subplots(figsize=(9,6))
    hep.cms.label(
        "Preliminary",
        data=True,
        lumi=35.9,
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

    ax.set_xticks(range(0,5)) # to avoid this error: UserWarning: FixedFormatter should only be used together with FixedLocator
    ax.set_xticklabels([0, 0.2, 0.5, 0.8, 1])
    ax.set_xlabel('TT_bbqq_vs_01b', loc='right')
    return fig,ax

#fitDiagnostics = uproot.open('fitDiagnosticsSM+EG_Xbb_0b+1b_BBQQ.root')
#branches = ['SM_zerob_bdtHi', 'EG_zerob_bdtHi']

#fitDiagnostics = uproot.open('fitDiagnosticsSingleMuon_Xbb_0b+1b_BBQQ.root')
#fitDiagnostics = uproot.open('fitDiagnosticsEGamma_Xbb_0b+1b_BBQQ.root')
#branches = ['zerob_bdtHi']


fns = {'fitDiagnosticsmu+eg_0b+1b_TT_bbqq_vs_01b.root' : ['mu_zerob_bdtHi', 'mu_zerob_bdtMed', 'mu_zerob_bdtLo', 'mu_zerob_bdtVeto', 'mu_oneb','eg_zerob_bdtHi', 'eg_zerob_bdtMed', 'eg_zerob_bdtLo', 'eg_zerob_bdtVeto', 'eg_oneb'],
       'fitDiagnosticsmu_0b+1b_TT_bbqq_vs_01b.root' : ['zerob_bdtHi', 'zerob_bdtMed', 'zerob_bdtLo', 'zerob_bdtVeto', 'oneb'],
       'fitDiagnosticseg_0b+1b_TT_bbqq_vs_01b.root' : ['zerob_bdtHi', 'zerob_bdtMed', 'zerob_bdtLo', 'zerob_bdtVeto', 'oneb']}

for fn in fns:
    for branch in fns[fn]:
        fitDiagnostics = uproot.open(fn)
        dc_sr = fitDiagnostics[f'shapes_fit_s/{branch}']
        fig, ax = make_plots(dc_sr)
        pltname = f"{fn.removesuffix('.root').removeprefix('fitDiagnostics')}_{branch}"
        ax.set_title(pltname, y=1.1)
        fig.savefig(f'plots/v2/pre_post_Fits/postfit_{pltname}.png', bbox_inches='tight')

        dc_sr = fitDiagnostics[f'shapes_prefit/{branch}']
        fig, ax = make_plots(dc_sr)
        pltname = f"{fn.removesuffix('.root').removeprefix('fitDiagnostics')}_{branch}"
        ax.set_title(pltname, y=1.1)
        fig.savefig(f'plots/v2/pre_post_Fits/prefit_{pltname}.png', bbox_inches='tight')

        plt.close('all')
import sys
sys.exit()

for branch in branches:
    ## post fit
    dc_sr = fitDiagnostics[f'shapes_fit_s/{branch}']
    h = dc_sr['data']
    processes = ['Sum0b', 'Sum1B', 'Sum2B']
    # fig, (ax, rax) = plt.subplots(2,1,figsize=(10,10), gridspec_kw={"height_ratios": (3, 1), "hspace": 0.05}, sharex=True)
    fig, ax = plt.subplots(figsize=(9,6))
    hep.cms.label(
        "Preliminary",
        data=True,
        lumi=35.9,
        loc=0,
        ax=ax,
    )
    hep.histplot(
        [ dc_sr[x].counts() for x in processes ],
        dc_sr['total'].axes[0].edges(),
        #w2=[ dc_sr[x].errors() for x in processes ],  # not needed
        histtype="fill",
        stack=True,
        label=processes, #[labels[x] for x in processes],
        #color=['red', 'green'],
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

    #ratio_val = dc_sr['data'].values()[1]/dc_sr['total'].counts()
    #ratio_err_hep = np.sqrt(dc_sr['data'].values()[1])/dc_sr['data'].values()[1]

    #rax.set_ylim(0,1.99)
    #rax.set_xlabel('Signal Region')
    #rax.set_ylabel(r'Data/Pred.')
    ax.set_ylabel(r'Events')

    add_uncertainty(dc_sr['total'],  ax)
    #add_uncertainty(dc_sr['total'], rax, ratio=True)

    ax.legend()

    plt.savefig(f'plots/pre_post_Fits/EGamma_{branch}_postfit.png')

    ## prefit
    dc_sr = fitDiagnostics[f'shapes_prefit/{branch}']
    h = dc_sr['data']
    processes = ['Sum0b', 'Sum1B', 'Sum2B']
    # fig, (ax, rax) = plt.subplots(2,1,figsize=(10,10), gridspec_kw={"height_ratios": (3, 1), "hspace": 0.05}, sharex=True)
    fig, ax = plt.subplots(figsize=(9,6))
    hep.cms.label(
        "Preliminary",
        data=True,
        lumi=35.9,
        loc=0,
        ax=ax,
    )
    hep.histplot(
        [ dc_sr[x].counts() for x in processes ],
        dc_sr['total'].axes[0].edges(),
        #w2=[ dc_sr[x].errors() for x in processes ],  # not needed
        histtype="fill",
        stack=True,
        label=processes, #[labels[x] for x in processes],
        #color=['red', 'green'],
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


    #ratio_val = dc_sr['data'].values()[1]/dc_sr['total'].counts()
    #ratio_err_hep = np.sqrt(dc_sr['data'].values()[1])/dc_sr['data'].values()[1]

    #rax.set_ylim(0,1.99)
    #rax.set_xlabel('Signal Region')
    #rax.set_ylabel(r'Data/Pred.')
    ax.set_ylabel(r'Events')


    add_uncertainty(dc_sr['total'],  ax)
    #add_uncertainty(dc_sr['total'], rax, ratio=True)

    ax.legend()

    plt.savefig(f'plots/pre_post_Fits/EGamma_{branch}_prefit.png')

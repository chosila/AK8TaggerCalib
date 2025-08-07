## conda activate ana_SS
## python plot_nll.py <link to combineoutput root  file to plot>
import uproot
import matplotlib.pyplot as plt
import numpy as np

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('pltname')
args = parser.parse_args()

f = uproot.open(args.filename)

g = f['limit']

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

s2b = np.array(g['s2B2Q_4bin'])
nll = np.array(g['deltaNLL'])
fig, ax = plt.subplots(figsize=(9,6.5))
ax.plot(s2b, nll, '.')
ax.set_xlabel('s2B2Q_4bin', loc='right', fontsize=16)
ax.set_ylabel('-deltaNLL', loc='top', fontsize=16)

ax.set_title(f'{args.pltname}', loc='right', fontsize=18)

minpoint = s2b[np.argmin(nll)]
low05 = s2b[find_nearest(nll[s2b<minpoint], 0.5)]
tmp = nll
tmp[s2b < minpoint ] = 10
high05 = s2b[find_nearest(tmp, 0.5)]

print('low 05', low05)
print('high 05', high05)
print('x minpoint', minpoint)
print('y minpoint', np.min(nll))

ax.axhline(y=0.5, color='r')
ax.vlines(x=low05,  ymin=-0.5, ymax=0.5, color='r')
ax.vlines(x=high05, ymin=-0.5, ymax=0.5, color='r')
ax.set_ylim(-0.06, 0.7)


txtstr = '\n'.join((
    r'µ = %.2f' % (minpoint),
    r'[%.2f,%.2f]' % (low05, high05),
))

props = dict(boxstyle='round', facecolor='white')
ax.text(0.05, 0.95, txtstr, transform=ax.transAxes, fontsize=20,
        verticalalignment='top', bbox=props)

#ax.set_xlim([-2,2])
fig.savefig(f'{args.pltname}_deltanll.png')

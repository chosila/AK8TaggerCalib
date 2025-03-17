## conda activate ana_SS
## python plot_nll.py <link to combineoutput root  file to plot>
import uproot
import matplotlib.pyplot as plt
import numpy as np

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', default='higgsCombineTest.MultiDimFit.mH120.root')
args = parser.parse_args()

f = uproot.open(args.filename)

g = f['limit']

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

s2b = np.array(g['s2B_4bin'])
nll = np.array(g['deltaNLL'])
fig, ax = plt.subplots(figsize=(9,6.5))
ax.plot(s2b, nll, '.')
ax.set_xlabel('x2B_4bin')
ax.set_ylabel('deltaNLL')
#pltname = args.filename.split('/')[1].replace('.root','')
pltname = args.filename.split('.')[0].removeprefix('output_root/v2/higgsCombine')
ax.set_title(f'{pltname} deltaNLL vs x2B_4bin')

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
ax.set_ylim(-0.06, 1.1)

ax.text(0.7,    0.5, 'y=0.5')
ax.text(low05,  0.02, low05)
ax.text(high05, 0.02, high05)
ax.text(minpoint, 0.02, f'min={minpoint:.4f}')

print(pltname)
fig.savefig(f'plots/v2/{pltname}.png', bbox_inches='tight')

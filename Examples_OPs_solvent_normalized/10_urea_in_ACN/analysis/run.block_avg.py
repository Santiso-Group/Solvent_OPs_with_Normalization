import numpy as np
import pandas as pd

f = pd.read_csv('summary.ETOT.block1', sep='      ', names=['time', 'energy'])
energy = f['energy']
avg = str(np.mean(energy))
with open('summary_avg.ETOT.blocks','a') as x:
	x.write(avg + "\n")

f = pd.read_csv('summary.ETOT.block2', sep='      ', names=['time', 'energy'])
energy = f['energy']
avg = str(np.mean(energy))
with open('summary_avg.ETOT.blocks','a') as x:
	x.write(avg + "\n")

f = pd.read_csv('summary.ETOT.block3', sep='      ', names=['time', 'energy'])

energy = f['energy']
avg = str(np.mean(energy))

with open('summary_avg.ETOT.blocks','a') as x:
   x.write(avg + "\n")

f = pd.read_csv('summary.ETOT.block4', sep='      ', names=['time', 'energy'])

energy = f['energy']
avg = str(np.mean(energy))

with open('summary_avg.ETOT.blocks','a') as x:
   x.write(avg + "\n")

f = pd.read_csv('summary.ETOT.block5', sep='      ', names=['time', 'energy'])

energy = f['energy']
avg = str(np.mean(energy))

with open('summary_avg.ETOT.blocks','a') as x:
   x.write(avg + "\n")

f = pd.read_csv('summary.ETOT.block6', sep='      ', names=['time', 'energy'])

energy = f['energy']
avg = str(np.mean(energy))

with open('summary_avg.ETOT.blocks','a') as x:
   x.write(avg + "\n")

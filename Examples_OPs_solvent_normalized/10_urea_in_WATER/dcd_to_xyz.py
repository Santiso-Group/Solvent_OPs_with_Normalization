import mdtraj as md
import numpy as np

# Load trajectory and topology
#t = md.load('trimmed_solvent.dcd', top='geometry_solvent.pdb')
#t.save('trimmed_solvent.xyz')

t = md.load('equil.nc', top='simbox.prmtop')
t[1:6000:100].save('trimmed_solvent.xyz')

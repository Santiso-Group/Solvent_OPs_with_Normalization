import mdtraj as md
import numpy as np

# Load trajectory and topology
t = md.load('trimmed.dcd', top='geometry.pdb')

# Select residue to keep in DCD file
atoms_to_keep = [atom.index for atom in t.topology.atoms\
                if (atom.residue.name == 'URE')]
t.restrict_atoms(atoms_to_keep)  # this acts inplace on the trajectory

# Save trimmed dcd only with desired residue
t.save('trimmed_urea.dcd')
# Save geometry only with desired residue
t[-1].save('geometry_urea.pdb')
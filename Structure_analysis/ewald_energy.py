
from pymatgen.analysis.bond_valence import BVAnalyzer
from pymatgen import Specie
from pymatgen.analysis.ewald import EwaldSummation
import os
from pymatgen.io.vasp import Poscar
import numpy as np

bva = BVAnalyzer()
def get_I_mads(struc):
    # Add oxidation states
    try:
        struc = bva.get_oxi_state_decorated_structure(struc)
        #print (struc)
    except:
        struc.add_oxidation_state_by_guess()
    
	# Check if a specific species is present 
    if (Specie('I',-1) in struc.species):
        ews = EwaldSummation(struc)
        print (ews)
        I_indices = [n  for n,site in enumerate(struc) if 
                             site.specie.symbol == 'I']
        I_mads = np.array([ews.get_site_energy(n) for n in I_indices])
        print (I_indices)
        print (I_mads)
        return I_mads
        return ews.total_energy
        print (ews.total_energy)

filepath = os.path.join('../Structure_collections/', 'POSCAR_3C')
p = Poscar.from_file(filepath)
original_s = p.structure
struc = original_s.copy() 
get_I_mads(struc)

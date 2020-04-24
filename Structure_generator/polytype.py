import numpy as np

# list [a,b,c] -> str(a) + ' ' + str(b) + ' ' + str(c) + '\n'
def list2str(inputList):
	return str("%.15f" % inputList[0]) + '    ' + str("%.15f" % inputList[1]) + '    ' + str("%.15f" % inputList[2]) + '\n'	

# Generate atoms in the supercell using 
# (1) the position of atoms at the origin, 
# (2) a unit vector, and 
# (3) displacement vector for each layer.
# Displacement vectors are defined as how the atoms are displaced from the perfect cubic structure (3C).
def generateAtoms(atomAtOrigin,unitVector,displacementCoefficients):
    tempStr =''
    for i in range(NoLayer):
        temp = list2str(atomAtOrigin + unitVector * i + displacementUnitVector * displacementCoefficients[i] )
        tempStr += temp	
    return(tempStr)

# Displacement vectors are calculated by multiplying the coefficients (in the disp file) and the unit vector.
# This file contains the coefficients for atoms at B sites and the other atoms (A and 3 X sites).
# Sequence - The coefficient for AX3 and B
def readDisplacements():
    a = open('disp')
    b = a.readlines()
    data = []
    for i in range(len(b)):
        if '#' in b[i]: # Ignore a line if there is "#"
            pass
        elif len(b[i].split()) == 0:
            pass
        else:
            temp = list(map(int,b[i].split()[:-1])) 
            data.append(temp)
    AX3 = data[0]
    B   = data[1]
    NoLayer = len(AX3) # Now the number of layers is defined.
    return(NoLayer,AX3,B)

#------------------------------------------------------------
LC = 6.2904720703589856        # The lattice constant. Here we assume the cubic ABX3.
savefilename = 'POSCAR'        # The output file of the code.
strA = 'Cs'                    # Atomic species at A site
strB = 'Sn'                    # Atomic species at B site
strX = 'I'                     # Atomic species at X site
#------------------------------------------------------------

NoLayer, sAX3, sB = readDisplacements()

# The number of each atomic species.
noAtom  = np.asarray([1,1,3]) * NoLayer

# The unit vector of the displacements
displacementUnitVector = np.asarray([1.0/3,1.0/3,0.0])

# Lattice vectors of a supercell
lat1 = LC * np.asarray([np.sqrt(2)  ,              0,                          0])
lat2 = LC * np.asarray([np.sqrt(2)/2,   np.sqrt(6)/2,                          0])
lat3 = LC * np.asarray([           0,              0,     np.sqrt(3)/3 * NoLayer]) 

# b is a string, which will be used to make the POSCAR file
b  = 'A polytype of perovskites\n'                          # Name of the system
b += '1.000000000000000\n'                                  # A universal scaling factor
b += '    ' + list2str(lat1)                                # Lattice vector 1
b += '    ' + list2str(lat2)                                # Lattice vector 2
b += '    ' + list2str(lat3)                                # Lattice vector 3
b += '    ' + strA  + '   ' + strB + '      ' + strX +'\n'  # Atomic species
b += '    ' +  '    '.join(list(map(str,noAtom)))   +'\n'   # The number of each atomic species
b += 'direct\n'                                             #direct coordinate will be used

# Define atoms at the origin
A = np.asarray([0,0,0])
B = np.asarray([2.0/3,2.0/3,1.0/NoLayer/2])
X1 = np.asarray([0.5,0.0,0.0])
X2 = np.asarray([0.0,0.5,0.0])
X3 = np.asarray([0.5,0.5,0.0])

# Define the unit vector.
unitVector = np.asarray([1.0/3,1.0/3,1.0/NoLayer])

# Generate atoms in the supercell
b += generateAtoms(A ,unitVector,sAX3)
b += generateAtoms(B ,unitVector,sB  )
b += generateAtoms(X1,unitVector,sAX3)
b += generateAtoms(X2,unitVector,sAX3)
b += generateAtoms(X3,unitVector,sAX3)

# Save the output POSCAR file
a = open(savefilename,'w')
a.write(b)
a.close()

#------------------------------------------------------------
############################################################
LC = 6.2904720703589856 #lattice constant (cubic)
savefilename = 'POSCAR_TEST'
############################################################

############################################################
import numpy as np

def list2str(inputList):
	return str("%.15f" % inputList[0]) + '    ' + str("%.15f" % inputList[1]) + '    ' + str("%.15f" % inputList[2]) + '\n'	

def generateAtoms(atom,vector,sAtom):
    tempStr =''
    for i in range(NoLayer):
        temp = list2str(atom + vector * i + shift * sAtom[i] )
        tempStr += temp	
    return(tempStr)


def readPOS():
    a = open('POS')
    b = a.readlines()
    data = []
    for i in range(len(b)):
        if '#' in b[i]:
            pass
        elif len(b[i].split()) == 0:
            pass
        else:
            #print(b[i].split()[:-1])
            temp = list(map(int,b[i].split()[:-1]))
            data.append(temp)
    Cs = data[0]
    Sn = data[1]
    I1 = data[2]
    I2 = data[3]
    I3 = data[4]
    NoLayer = len(Cs)
    #print(NoLayer)
    return(NoLayer,Cs,Sn,I1,I2,I3)

############################################################
NoLayer, sCs, sSn, sI1, sI2, sI3 = readPOS()
noAtom  = np.asarray([1,1,3]) * NoLayer

shift = np.asarray([1.0/3,1.0/3,0.0])
lat1 = LC * np.asarray([np.sqrt(2)  ,              0,                          0])
lat2 = LC * np.asarray([np.sqrt(2)/2,   np.sqrt(6)/2,                          0])
lat3 = LC * np.asarray([           0,              0,     np.sqrt(3)/3 * NoLayer]) 

b  = 'Perovskite Stacking Fault\n'
b += '1.000000000000000\n' 
b += '    ' + list2str(lat1)
b += '    ' + list2str(lat2)
b += '    ' + list2str(lat3)
b += '   Cs   Sn    I\n' #You may change this line
b += '    ' +  '    '.join(list(map(str,noAtom))) + '\n'
b += 'direct\n'

Cs = np.asarray([0,0,0])
Sn = np.asarray([2.0/3,2.0/3,1.0/NoLayer/2])
I1 = np.asarray([0.5,0.0,0.0])
I2 = np.asarray([0.0,0.5,0.0])
I3 = np.asarray([0.5,0.5,0.0])
vector = np.asarray([1.0/3,1.0/3,1.0/NoLayer])

b += generateAtoms(Cs,vector,sCs)
b += generateAtoms(Sn,vector,sSn)
b += generateAtoms(I1,vector,sI1)
b += generateAtoms(I2,vector,sI2)
b += generateAtoms(I3,vector,sI3)

a = open(savefilename,'w')
a.write(b)
a.close()
############################################################

#spin2H = [1,-1]
#spin3C = [1,1,1]
#spin4H = [1,-1,-1,1]
#spin6H = [1,-1,-1,-1,1,1]
#spin9R = [1,-1,1,1,-1,1,1,-1,1]
#spin12R = [1,-1,1,1,1,-1,1,1,1,-1,1,1]

spin2H = [1,1]
spin3C = [-1,-1,-1]
spin4H = [1,-1,1,-1]
spin6H = [1,-1,-1,1,-1,-1]
spin9R = [1,1,-1,1,1,-1,1,1,-1]
spin12R = [1,1,-1,-1,1,1,-1,-1,1,1,-1,-1]
spin12H = [1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1]
spin2C9H11 = [1,1,1,1,1,1,1,1,-1,-1,-1]
spin2H9C11 = [1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
spin2C9H18 = [1,1,1,1,1,1,1,-1,-1,1,1,1,1,1,1,1,-1,-1]
spin2H9C18 = [1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1]


def coefficients(spin,nnn):
    length = len(spin)
    temp = 0
    for i in range(length):
        j = (i+nnn) % length
        temp += spin[i] * spin[j]
    print(temp)

def generalCoefficients(spin,nnn):
    length = len(spin)
    temp = 0
    for i in range(length):
        tempi = spin[i]
        for j in range(len(nnn)):
            if nnn == [0]:
                tempi = tempi
            else:
                k = (i+nnn[j]) % length
                tempi = tempi * spin[k]
        temp += tempi
    print(temp)

def getAll(spin):
    generalCoefficients(spin,[0])
    generalCoefficients(spin,[1])
    generalCoefficients(spin,[2])
    generalCoefficients(spin,[3])
    generalCoefficients(spin,[1,2])
    generalCoefficients(spin,[2,3])
    generalCoefficients(spin,[1,3])
    generalCoefficients(spin,[1,2,3])

#getAll(spin2H)
#getAll(spin3C)
#getAll(spin4H)
#getAll(spin6H)
#getAll(spin9R)
#getAll(spin12R)
#getAll(spin12H)
#getAll(spin2H9C11)
getAll(spin2C9H11)
#getAll(spin2H9C18)
#getAll(spin2C9H18)
#the K' = 1/2([2,3]+[1,3])
nucleo = raw_input('Enter DNA Nucleotides: ')
nA = 0
nC = 0
nG = 0
nT = 0
s = ' '
for i in nucleo:
	if i == "A":
		nA = nA + 1
	if i == "C":
		nC = nC + 1
	if i == "G":
		nG = nG + 1
	if i == "T":
		nT = nT + 1

print ('A    C    G    T')
print nA,s,nC,s,nG,s,nT
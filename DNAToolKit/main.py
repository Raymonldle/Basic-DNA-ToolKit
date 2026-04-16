from DNAToolKit import *
import random

#generates a random DNA string using the nucleotide bases given the length of X 
randDNAStr = ''.join([random.choice(Nucleotides) for i in range(10)]) 

DNAStr = validateSequence(randDNAStr)
print(DNAStr)
print(countNucleotideFrequency(DNAStr))
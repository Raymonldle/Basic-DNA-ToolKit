from DNAToolKit import *
from Structures import *
from Utilities import colored
import random

#generates a random DNA string using the nucleotide bases given the length of X 
randDNAStr = ''.join([random.choice(Nucleotides) for i in range(50)])

DNAStr = validateSequence(randDNAStr) 

print(f'Sequence: {colored(DNAStr)}')
print(f'[1] Sequence Length: {len(DNAStr)}')
print(f'[2] Nucleotide Frequency: {countNucleotideFrequency(DNAStr)}')
print(f'[3] Transcribed RNA String: {colored(transcribeDNAStr(DNAStr))}')

print(f"[4] DNA String + Reverse Complement:\n\n5' {colored(DNAStr)} 3' ")
print(f'   {''.join(['|' for i in range(len(DNAStr))])} ')
print(f"3' {colored(reverseComplement(DNAStr)[::-1])} 5' [Complement]\n")
print(f"5' {colored(reverseComplement(DNAStr))} 3' [Reverse Complement]\n")
print(f"[5] Pairing Contents:\n GC Content: {GC_content(DNAStr)}%\n")
print(f"[6] GC Content in Subsection k = 5: \n {GC_content_subsection(DNAStr, k=5)}\n")
print(f"[7] Amino Acid Sequence: \n {translateSequence(DNAStr)}")



from Structures import *


#check the sequence to make sure it is a DNA String
def validateSequence(dna_sequence): 
    """checks if the given sequence is a valid DNA sequence with the correct nucleotide bases. Returns the sequence in uppercase if valid, otherwise returns False"""
    tmpSeq = dna_sequence.upper()

    for i in tmpSeq:
        if i not in Nucleotides:
            return False
    return tmpSeq

def countNucleotideFrequency(sequence):
    """Counts the frequency of each nucleotide in a given sequence. Returns a dictionary with the count of each nucleotide."""
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    
    for i in sequence: #for every index inside the sequence list, run the following code
        tmpFreqDict[i] += 1 #add 1 to the value of the key that matches the index of the sequence

    return tmpFreqDict

def transcribeDNAStr(dna_sequence):
    """transcribes DNA --> RNA by replacing all occurences of Thymine w/ Uracil. Returns the transcribed RNA string."""
    clean_seq = validateSequence(dna_sequence)
    clean_seq = clean_seq.replace("T", "U")
    return clean_seq

def reverseComplement(dna_sequence):
    mapping = str.maketrans("ACGT", "TGCA")
    return dna_sequence.translate(mapping)[::-1]

def GC_content(seq):
    return round(((seq.count("G") + seq.count("C")) / len(seq)) * 100)

def GC_content_subsection(seq, k=20):
    """GC Content in DNA/RNA sub-sequence length k. k = 20 by default."""

    result = []

    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        gc = GC_content(subseq)
        result.append(str(gc) + "%")

    return result

def translateSequence(seq, initPos=0):
    """Translates the DNA sequence into an amino acid sequence"""

    return [DNA_Codons[seq[pos:pos + 3]] for pos in range(initPos, len(seq) - 2, 3)]

    
    

#     res = []
#     for i in range(0, len(seq) - k + 1, k):
#         subseq = seq[i:i + k]
#         res.append(GC_content(subseq))
#     return res





# # def translateDNAtoRNA(dna_sequence):
# #     clean_seq = validateSequence(dna_sequence)
# #     clean_seq = clean_seq.upper()
    
# #     if clean_seq:
# #         nav_table = str.maketrans("ATGC", "UACG")
# #         return clean_seq.translate(nav_table)
# #     else:
# #         return "Invalid DNA Sequence"

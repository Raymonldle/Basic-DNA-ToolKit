Nucleotides = ["A", "C", "G", "T"]

#check the sequence to make sure it is a DNA String
def validateSequence(dna_sequence): 
    tmpSeq = dna_sequence.upper() #uppercases the given input

    for i in tmpSeq:
        if i not in Nucleotides:
            return False
    return tmpSeq

def countNucleotideFrequency(sequence):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    
    for i in sequence: #for every index inside the sequence list, run the following code
        tmpFreqDict[i] += 1 #add 1 to the value of the key that matches the index of the sequence

    return tmpFreqDict

# def translateDNAtoRNA(dna_sequence):
#     clean_seq = validateSequence(dna_sequence)
#     clean_seq = clean_seq.upper()
    
#     if clean_seq:
#         nav_table = str.maketrans("ATGC", "UACG")
#         return clean_seq.translate(nav_table)
#     else:
#         return "Invalid DNA Sequence"


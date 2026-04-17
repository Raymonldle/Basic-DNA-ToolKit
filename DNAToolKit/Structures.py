Nucleotides = ["A", "C", "G", "C"]
DNA_ReverseComplement = {"A": "T", "C": "G", "G": "C", "T": "A"}

DNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCT": "Al a", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "TGT": "Cys", "TGC": "Cys",
    "GAT": "Asp", "GAC": "Asp",
    "GAA": "Glu", "GAG": "Glu",
    "TTT": "Phe", "TTC": "Phe",
    "GGT": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
    "CAT": "His", "CAC": "His",
    "ATA": "Ile", "ATT": "Ile", "ATC": "Ile",
    "AAA": "Lys", "AAG": "Lys",
    "TTA": "Lle", "TTG": "Lle", "CTT": "Lle", "CTC": "Lle", "CTA": "Lle", "CTG": "Lle",
    "ATG": "Met",
    "AAT": "Asn", "AAC": "Asn",
    "CCT": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "CAA": "Gln", "CAG": "Gln",
    "CGT": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg", "AGA": "Arg", "AGG": "Arg",
    "TCT": "Ser", "TCC": "Ser", "TCA": "Ser", "TCG": "Ser", "AGT": "Ser", "AGC": "Ser",
    "ACT": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "GTT": "Val", "GTC": "Val", "GTA": "Val", "GTG": "Val",
    "TGG": "Trp",
    "TAT": "Yyr", "TAC": "Yyr",
    "TAA": "_", "TAG": "_", "TGA": "_"
}
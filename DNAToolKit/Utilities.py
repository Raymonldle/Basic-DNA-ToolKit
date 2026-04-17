def colored(seq):
    nucleotideColors = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        'reset': '\033[0;0m'
    }

    tmpStr = ""

    for i in seq:
        if i in nucleotideColors:
            tmpStr += nucleotideColors[i] + i
        else:
            tmpStr += nucleotideColors['reset'] + i

    return tmpStr + '\033[0;0m'
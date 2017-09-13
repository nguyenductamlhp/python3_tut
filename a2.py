def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for nu in dna:
        if nu == nucleotide:
            count += 1
    return count

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna1.find(dna2) == -1:
        return False
    return True

def is_valid_sequence(dna):
    """ (str) -> bool
    Return turn True if DNA sequence contain valid nucleotide, which in A, T,
    G, C
    >>> is_valid_sequence('ATGCTGC')
    True
    >>> is_valid_sequence('ATGCX')
    False
    """
    is_valid = True
    for nu in dna:
        if 'ATGC'.find(nu) == -1:
            is_valid = False
    return is_valid
    
def insert_sequence(dna1, dna2, pos):
    """ (str, str, int) -> str
    Return DNA sequence which is result of inserting dna2 into dna1 from pos
    >>>insert_sequence('ATTGA', 'CTA', 1)
    'ACTATTGA'
    >>>insert_sequence('GATTGA', 'CTA', 3)
    'GATCTATGA'
    """
    re = ''
    re = dna1[0:pos]
    re += dna2
    re += dna1[pos:]
    return re

def get_complement(nucleotide):
    """ (str) -> str
    Return complement of nucleotide
    >>> get_complement('A')
    T
    >>> get_complement('G')
    C
    """
    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'G':
        return 'C'
    if nucleotide == 'C':
        return 'G'

def get_complementary_sequence(dna):
    """ (str) -> str
    Return DNA sequence that is complementary with given DNA sequence
    >>> get_complementary_sequence('ATGCGTA')
    TACGCAT
    >>> get_complementary_sequence('TTACGAC')
    AATGCTG
    """
    result = ''
    for nu in dna:
        result += get_complement(nu)
    return result

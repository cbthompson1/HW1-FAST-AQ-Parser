# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Test correct functionality of Fasta parser.
    """
    fasta = FastaParser('tests/test_data/test.fa')
    res = []
    res_5_expected = (
        # 0
        'seq5',
        # 1
        'TAAGTAGTGCACTCCTGCGCGTCTCTTCCCAGAATCGTACTCTCAGAGCTAGAGAGGCGCGTTTGCCGT'
        'TCTACTCACCCCAGCCTCTGAAGAGGGATGC'
    )
    res_98_expected = (
        # 0
        'seq98',
        # 1
        'CGAGCGAGAAACGCGCTAACTAGCAACCGGAACAACAATGCTGGGTTGAATTTGATTCGCACCCGACGA'
        'TCACTAGAGAGTTTATCTGGGACTCCGGGAC'
    )

    for seq in fasta:
        res.append(seq)
    assert len(res) == 100

    # Check two positions of the parser and confirm they match.
    assert res[5] == res_5_expected
    assert res[98] == res_98_expected

def test_FastaParser_blank():
    """
    Test error handling of Fasta parser when input file is blank.
    """
    fasta = FastaParser('tests/test_data/blank.fa')
    res = []
    with pytest.raises(ValueError):
            for seq in fasta:
                res.append(seq)

def test_FastaParser_bad():
    """
    Test error handling of Fasta parser when input file is bad.
    """
    fasta = FastaParser('tests/test_data/bad.fa')
    res = []
    with pytest.raises(ValueError):
            for seq in fasta:
                res.append(seq)

def test_FastaFormat():
    """
    Test to make sure that if a fastq file is inputted into the fasta parser,
    the first result is 'None'
    """
    fasta_parser_fastq_file = FastaParser('tests/test_data/test.fq')
    res = []
    for line in fasta_parser_fastq_file:
         res.append(line)
    assert res[0] == (None, '@seq0')


def test_FastqParser():
    """
    Test correct functionality of Fastq parser.
    """
    fastq = FastqParser('tests/test_data/test.fq')
    res = []
    res_5_expected = (
        # 0
        'seq5',
        # 1
        'CGCGATGAAGAAGACCTATCCCAACTTGCTCTGGCTAGCCTCGCCAAGTATGATAGGATCCATCGTCTA'
        'TCATGCATGCGTTAGACACTTGCTGGAGTAC',
        # 2
        ':+;!5\'&.";$+/2;!##<\'!9+&4#3"2>,=*%)""<&=*2,$651/&01#*%.:=5-:&,:(%>/'
        ';0!0%#4/-807+5"6;&::>;&.9+((!5\'&5'

    )
    res_98_expected = (
        # 0
        'seq98',
        # 1
        'AACCTGCCCGTAGCCTTTAGGTAGCCCGTCTACATGTCCTCCAGTACAGTGGAAGCTCCTACATCAACT'
        'GATCAAATAACATCGCAGCACTATATGTCAC',
        # 2
        '39$$8\'\':7:0;0%/7$89-<3\',:)1"0\'=2\'!#5><>+6/=99#>8-$76(6$2\'+=;$-)'
        ')753#99,=+4+1=:5.08*$*:4=,>)/)\':8,<48'
    )

    for seq in fastq:
        res.append(seq)

    # Check overall length is good.
    assert len(res) == 100

    # Check two positions of the parser and confirm they match.
    assert res[5] == res_5_expected
    assert res[98] == res_98_expected

def test_FastqParser_blank():
    """
    Test error handling of Fastq parser when input file is blank.
    """
    fastq = FastqParser('tests/test_data/blank.fq')
    res = []
    with pytest.raises(ValueError):
            for seq in fastq:
                res.append(seq)

def test_FastqParser_bad():
    """
    Test error handling of Fastq parser when input file is bad.
    """
    fastq = FastqParser('tests/test_data/bad.fq')
    res = []
    with pytest.raises(ValueError):
            for seq in fastq:
                res.append(seq)

def test_FastqFormat():
    """
    Test to make sure if a fastq parser is provided a fasta file, the first
    result includes None as its first element.
    """
    fastq_parser_fasta_file = FastqParser('tests/test_data/test.fa')
    res = []
    for line in fastq_parser_fasta_file:
         res.append(line)
    assert res[0][0] == None
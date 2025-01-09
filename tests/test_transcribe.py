# write tests for transcribe functions

import pytest
from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Transcribe function correctly outputs for all nucleotides expected.
    """
    test_seq = 'ATCG'
    res = transcribe(test_seq)
    assert res == 'UAGC'

def test_transcribe_bad_input():
    """
    Transcribe function throws KeyError if unexpected char is in the input.
    """
    test_seq = 'ATCGX'
    with pytest.raises(KeyError):
        res = transcribe(test_seq)

def test_reverse_transcribe():
    """
    Reverse transcribe correctly reverses the test sequence after transcribing.
    """
    test_seq = 'ATCG'
    res = reverse_transcribe(test_seq)
    assert res == 'CGAU'
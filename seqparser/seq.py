# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Transcribes a sequence of DNA nucleotides into their RNA transcription
    equivalent.

    Inputs:
        seq (str): sequence of nucleotides. Should only contain chars 'ATCG'.
        reverse (bool): flag to determine whether to reverse output.
    Output:
        (Potentially reversed) RNA nucleotide sequence.
    """

    transcription_result = []
    for nucleotide in seq:
        new_nucleotide = TRANSCRIPTION_MAPPING[nucleotide]
        transcription_result.append(new_nucleotide)
    if reverse:
        transcription_result = transcription_result[::-1]
    return ''.join(transcription_result)

def reverse_transcribe(seq: str) -> str:
    """
    Reverse transcribes a DNA nucleotide sequence.

    Input:
        seq (str): sequence of nucleotides. Should only contain chars 'ATCG'.
    Output:
        Reversed RNA nucleotide sequence.
    """
    return transcribe(seq, reverse=True)
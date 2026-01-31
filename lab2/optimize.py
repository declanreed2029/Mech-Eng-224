"""
Author(s): Declan Reed
Creation Date: Jan 28, 2026

Initial creation by Dietrich Geisler on 10/12/2025
Reviewed by Anastasia Kurdia on 1/22/2026

An implementation of the dna_optimize function

My thoughts: I think the problem with the code lies in line 27. 
    That attempt assignment was overwriting attempt and only assigning starting[index:] so attempt would only be that.
    I changed this to attempt + starting[index:] so it would be appended onto out existing attempt and not overiding it and it appears to have worked.

"""

def dna_optimize(starting, insertion, target):
    """
    Returns the index to insert the sequence "insertion" 
      to "starting" to perfectly match "target"
    If multiple such indices exist, return the earliest one
    If no such index exists, instead returns -1
    """
    # Try every index of the starting string
    for index in range(len(starting) + 1):
        # Slice the starting sequence _through_ index,
        #   insert our extra sequence,
        #   then add the rest of the starting sequence
        attempt = starting[:index]
        attempt = attempt + insertion
        attempt = attempt + starting[index:]

        # If it's a perfect match, return this index!
        if attempt == target:
            return index

    return -1


def test_dna_optimize():
    # Test cases for dna_optimize
    # These may be useful when debugging!

    expected = 3
    result = dna_optimize('TTT', 'G', 'TTTG')
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 1
    result = dna_optimize('ACTG', 'TG', 'ATGCTG')
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = -1
    result = dna_optimize('ATGT', 'GGT', 'ATGCGGTT')
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message


if __name__ == "__main__":
    test_dna_optimize()
    print('All tests passed!')

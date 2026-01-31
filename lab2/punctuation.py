"""
Author(s): Declan Reed
Creation Date: Jan 28, 2026

Initial creation by Dietrich Geisler on 10/12/2025
Reviewed by Anastasia Kurdia on 1/22/2026

An implementation of the remove_punctuation function

My thoughts: I believe that the problem was in line 23, the if statment that ultimatly decides what gets added to result. 
    It was checking if is_punctuation is true, and then adding that char to result. 
    This is problematic as that means result would be comprised of only punctuation, the exact opposite of what we want. 
    I changed this parameter to only when it is false so everything besides punctuation is included and it seemed to work.
"""

def remove_punctuation(s):
    """
    Returns the string s with punctuation removed
    Only the characters . , ? and ! are considered punctuation for this function
    """

    result = ''
    for char in s:
        # Check if our specific char is one of '.,?!'
        is_punctuation = char in '.,?!'
        if is_punctuation == False:
            result = result + char
    return result


def test_remove_punctuation():
    # Test cases for remove_punctuation
    # These may be useful when debugging!

    expected = 'hey there'
    result = remove_punctuation('hey, there')
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 'so great'
    result = remove_punctuation('so, great!')
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 'cat'
    result = remove_punctuation('c.,?!a,?t')
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message


if __name__ == "__main__":
    test_remove_punctuation()
    print('All tests passed!')

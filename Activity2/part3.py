import math

def count_lowercase(s):
    """Calculates the number of lowercase letters in a string

    Args:
        s (str): the string to search

    Returns:
        int: the number of lowercase letters
    """
    # Implement me!
    count = 0
    if s == '':
        return 0
    else:
        for char in s:
            if char.islower():
                count += 1
        return count


def test_count_lowercase():
    # Implement me!
    assert 1 == count_lowercase('Ab')
    assert 3 == count_lowercase('abc')
    assert 0 == count_lowercase('')


def are_all_evens(lst):
    """Returns whether all integers in a list are even

    Args:
        lst (list[int]): the list to search

    Returns:
        bool: True if all integers in the list are even and False otherwise
    """
    # Implement me!
    even = True
    if lst == []:
        return True
    else:
        for i in lst:
            if i % 2 != 0:
                even = False
        return even


def test_are_all_evens():
    # Implement me!
    assert True == are_all_evens([2, 2, 4])
    assert True == are_all_evens([])
    assert False == are_all_evens([0, 1, 4])


def is_perfect_square(x):
    """Returns whether x is a perfect square

    For example, 4 is a perfect square, and 5 is not

    Args:
        x (int): the number we check is a perfect square

    Returns:
        bool: True if x is a perfect square and False otherwise
    """
    sr = int(math.sqrt(x))
    if x == 0:
        return False
    elif sr * sr == x:
        return True
    else:
        return False


def test_is_perfect_square():
    # implement me!
    assert True == is_perfect_square(4)
    assert False == is_perfect_square(5)
    assert False == is_perfect_square(0)


def sum_negatives(lst):
    """Calculates the sum of all negative numbers in a list

    Positive numbers are ignored entirely in this calculation

    Args:
        lst (list[int]): the list to search

    Returns:
        int: the sum of all negative numbers in the list
    """
    count = 0
    if lst == 0:
        return 0
    else:
        for i in lst:
            if i < 0:
                count += i
        return count


def test_sum_negatives():
    # implement me!
    assert 0 == sum_negatives([1, 2, 3])
    assert 0 == sum_negatives([])
    assert -1 == sum_negatives([2, -1])


def is_prime(num):
    """Returns whether or not num is prime

    A prime number is any number that is only divided by 1 and itself

    For this function, negative numbers and 0 are not prime
    Additionally, 1 is considered a prime number

    Args:
        x (int): the number we check to be prime

    Returns:
        bool: True if x is a prime and False otherwise
    """
    if num == 0:
        return False
    elif num < 0:
        return False
    for i in range(1, num):
        if (i != 1) & (1 != num) & (num % i == 0):
            return False
    return True


def test_is_prime():
    # implement me!
    assert True == is_prime(7)
    assert False == is_prime(4)


def count_vowels(lst):
    """Calculates the number of vowels in all strings in a list

    Assumes that all strings in lst must consist only of lowercase letters

    A vowel is any letter a, e, i, o, or u
    Additionally, y is considered a vowel so long as it's not the first letter of a string

    Args:
        lst (list[str]): the list to search

    Returns:
        int: the number of vowels in all strings of lst
    """
    count = 0
    if lst == []:
        return 0
    else:
        for item in lst:
            i = 0
            for char in item:
                if (char == 'a') | (char == 'e') | (char == 'i') | (char == 'o') | (char == 'u'):
                    count += 1
                elif (char == 'y') & (i > 0):
                    count += 1
                i += 1
        return count
            


def test_count_vowels():
    # implement me!
    assert 0 == count_vowels([])
    assert 1 == count_vowels(['w', 'e'])
    assert 0 == count_vowels(['y'])
    assert 1 == count_vowels(['wy'])


# we'll explain what this __name__ == "__main__" means in lecture
# the short of it is that it says to only run this code when we run this file directly
if __name__ == "__main__":
    # run all of our tests (one at a time)
    test_count_lowercase()
    test_are_all_evens()
    test_is_perfect_square()
    test_sum_negatives()
    test_is_prime()
    test_count_vowels()
    print('All tests passed!')

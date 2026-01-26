def adjacent_duplicate(lst):
    """Calculates the number of adjacent_duplicates in a list of numbers

    An adjacent duplicate is a number with the same number next to it in the list
    Note that each number with an adjacent duplicate is counted separately

    Args:
        lst (list[int]): the list to search

    Returns:
        int: the number of duplicates
    """

    # Implement me!
    amt = 0
    for i in range(len(lst)):
        if i == 0:
            if lst[i] == lst[i + 1]:
                amt += 1
        elif i == (len(lst) - 1):
            if lst[i] == lst[i - 1]:
                amt += 1
        else:
            if lst[i] == lst[i + 1]:
                amt += 1
            elif lst[i] == lst[i - 1]:
                amt += 1
    return amt
print(adjacent_duplicate([4, 4]))
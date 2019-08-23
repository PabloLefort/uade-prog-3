"""
Given a list of numbers a peak its the number that its bigger than his inmediate neighbours.
"""


def PeakSearch(search_list, low, high):
    """
    Args:
        search_list (int): List of numbers
        low (int): low number of where it starts to compare
        high (int): high number of where it stops to compare
    """
    size = len(search_list)
    half = int(low + (high - low) / 2)

    # Base case when his neighbours are lower
    if((half == 0 or search_list[half - 1] <= search_list[half]) and (half == size - 1 or search_list[half + 1] <= search_list[half])):
        return search_list[half]

    # Call to the left part because the left neighbour its greater and must have a peak
    elif(half > 0 and search_list[half - 1] > search_list[half]):
        return PeakSearch(search_list, low, half - 1)
    
    # Call to the right
    else:
        return PeakSearch(search_list, half + 1, high)


if __name__ == "__main__":
    a = [0, 2, 3, 2, 5, 1, 0]
    assert PeakSearch(a, 0, len(a)), 3

    b = [7, 2, 3, 4, 5, 6, 1]
    assert PeakSearch(b, 0, len(b)), 7

    c = [7, 2, 3, 4, 5, 6, 1, 2]
    assert PeakSearch(c, 0, len(c)), 6

    d = [7, 2, 4, 4, 4, 6, 1]
    assert PeakSearch(d, 0, len(d)), 4
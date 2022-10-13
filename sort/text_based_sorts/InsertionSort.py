from Swap import _swap


def insertion_sort(unsorted, start, end):
    """
    Does an insertion sort on a Python list given a range of indicies
    Expected Complexity: O(n^2) (time) and O(1) (space)

    :param unsorted: unsorted Python list to be sorted
    :param start: integer of the starting index to be sorted
    :param end: integer of the ending index to be sorted
    """

    for i in range(1, end + 1):
        j = i

        # pulls the smallest of the remaining values and inserts it back in the list
        while (j > 0) and (unsorted[j] < unsorted[j - 1]):
            _swap(unsorted, j, j - 1)
            j -= 1

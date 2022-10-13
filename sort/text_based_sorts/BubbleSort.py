from Swap import _swap


def bubble_sort(unsorted):
    """
    Does a bubble sort given a Python list
    Expected Complexity: O(n^2) (time) and O(1) (space)

    :param unsorted: unsorted Python list to be sorted
    """
    for i in range(len(unsorted) - 1):
        for j in range(0, len(unsorted) - i - 1):

            # bubbles up the largest value through the list
            if unsorted[j] > unsorted[j + 1]:
                _swap(unsorted, j, j + 1)

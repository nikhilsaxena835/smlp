from Swap import _swap


def find_pivot(unsorted, start, end):
    """
    Find the pivot value using the Median of Three method in a Python list
    Expected Complexity: O(1) (time and space)

    :param unsorted: an unsorted Python list to find the pivot value in
    :param start: integer of starting index to find the pivot value in
    :param end: integer of ending index to find the pivot value in

    :return: the value of the pivot found using the Median of Three method
    """

    # pull the first, middle, and last values in the list 
    first = unsorted[start]
    middle = unsorted[(start + end) // 2]
    last = unsorted[end]
    
    # this method is done so that it can be done in constant time
    if (middle <= first <= last) or (last <= first <= middle):
        return first
    elif (first <= middle <= last) or (last <= middle <= first):
        return middle
    elif (first <= last <= middle) or (middle <= last <= first):
        return last


def partition(unsorted, start, end):
    """
    Will partition a list given a certain range for values greater and
    less than the pivot to be a certain side
    Expected complexity: O(n) (time) and O(1) (space)

    :param unsorted: an unsorted Python list to be partitioned
    :param start: integer of starting index within the list
    :param end: integer of ending index within the list

    :return: index of where hte pivot value ends in the list
    """
    pivot_value = find_pivot(unsorted, start, end)

    i = start - 1
    
    # pu all of the values that are less than the pivot on the left side 
    for j in range(start, end + 1):
        if unsorted[j] < pivot_value:
            i += 1
            _swap(unsorted, i, j)

    # moves the pivot value to the right spot after moving all of the values
    i += 1
    _swap(unsorted, i, unsorted.index(pivot_value))

    return i


def quick_sort(unsorted, start, end):
    """
    Performs a quick sort given a range of indicies to sort
    Expected Complexity: O(n*log(n)) (time) and O(log(n)) (space)
        - This function has a space complexity of O(log(n)) because of
          of the the recursive calls done within this function

    :param unsorted: an unsorted Python list to be sorted
    :param start: integer of the starting index to be sorted
    :param end: integer of the ending index to be sorted
    """
    if start >= end:
        return

    # find the middle index of the list and partition it 
    pivot_index = partition(unsorted, start, end)

    # sorting the first half
    quick_sort(unsorted, start, pivot_index)

    # sorting the second half
    quick_sort(unsorted, pivot_index + 1, end)

def merge(list1, list2, unsorted):
    """
    Merges two Python lists into the original list
    Expected Complexity: O(n) (time and space)

    :param list1: Python list of values to be used in the merge
    :param list2: Python list of values to be used in the merge
    :param unsorted: unsorted Python list of values where the values from list1
                     and list2 will be placed into
    """
    i = 0
    j = 0

    # compares the each value in both lists
    while i + j < len(unsorted):

        # does the comparison to add it back into the original list
        if (j == len(list2)) or (i < len(list1) and list1[i] < list2[j]):
            unsorted[i + j] = list1[i]
            i += 1
        else:
            unsorted[i + j] = list2[j]
            j += 1


def merge_sort(unsorted):
    """
    Does a merge sort on an unsorted Python list
    Expected Complexity: O(n*log(n)) (time) and O(n) (space)

    :param unsorted: unsorted Python list of values to be sorted
    """
    # stop sorting if the list size is less than 2
    if len(unsorted) < 2:
        return

    middle_index = len(unsorted) // 2

    # create two lists that are the halfs of the original list
    list1 = unsorted[0:middle_index]
    list2 = unsorted[middle_index : len(unsorted)]

    # sort both seperately
    merge_sort(list1)
    merge_sort(list2)

    # then combine the two halves
    merge(list1, list2, unsorted)

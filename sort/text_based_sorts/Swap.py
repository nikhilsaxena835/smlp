def _swap(test_list, x, y):
    """
    Conducts a Pythonic swap within a list between two indicies
        - Note: the order of x and y do not matter as long as both are in an
                acceptable range [0, len(test_list)]
    Expected Complexity: O(1) (time and space)

    :param some_list: Python list of integers where the swap will be done
    :param x: integer of the first index to be swapped with
    :param y: integer of the second index to be swapped with
    """
    test_list[x], test_list[y] = test_list[y], test_list[x]

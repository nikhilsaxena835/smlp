import time
from Swap import _swap


def find_pivot(data_list, start, end):
    """
    Finds the pivot value with in the sub list using the median of three method
    Expected Complexity: O(1) (time and space)

    :param data_list: Python list to find the pivot value in
    :param start: Integer for the starting index within the list
    :param end: Integer for the ending index within the list

    :return: Integer for the pivot value found using the median of three method
    """

    # pull the first, middle, and last values in the sublist
    first = data_list[start]
    middle = data_list[(start + end) // 2]
    last = data_list[end]

    # this was done so that it could be done in constant time
    if (middle <= first <= last) or (last <= first <= middle):
        return first

    elif (first <= middle <= last) or (last <= middle <= first):
        return middle

    elif (first <= last <= middle) or (middle <= last <= first):
        return last


def partition(data_list, start, end, draw_data, time_value):
    """
    Partitions the sub list and visualizes the steps
    Expected Complexity: O(n) (time) and O(1) (space)

    :param data_list: Python list to be partitioned
    :param start: Integer for the starting index in the list
    :param end: Integer for the ending index in the list
    :param draw_data: Function written in main.py that visualizes the list
    :param time_value: Float based on the input for time between steps

    :return: Integer for the index of the pivot value after the partition
    """
    pivot_value = find_pivot(data_list, start, end)

    i = start - 1

    for j in range(start, end + 1):

        # moves each value that is less than the pivot to the left
        if data_list[j] < pivot_value:
            i += 1
            _swap(data_list, i, j)

            # generate the color list to be visualized
            color_list = ["red" for x in range(len(data_list))]

            # color the values being swapped green
            for x in range(len(color_list)):
                if (x == i) or (x == j):
                    color_list[x] = "green"

            # visualizes the list and wait for the specified amount of time
            draw_data(data_list, color_list)
            time.sleep(time_value)

    i += 1

    # does one last swap to move the pivot value in the right spot
    swap_index = data_list.index(pivot_value)
    _swap(data_list, i, swap_index)

    # generate the color list to be visualized
    color_list = ["red" for x in range(len(data_list))]

    # color the values being swapped green
    for x in range(len(color_list)):
        if (x == i) or (x == swap_index):
            color_list[x] = "green"

    # visualizes the list and wait for the specified amount of time
    draw_data(data_list, color_list)
    time.sleep(time_value)

    return i


def quick_sort(data_list, start, end, draw_data, time_value):
    """
    Does a quick sort on the list and visualizes the steps
    Expected Complexity (Sort only): O(n*log(n)) (time) and O(1) (space)

    :param data_list: Python list to be sorted
    :param start: Integer of the starting index in the list
    :param end: Integer of the ending index in the list
    :param draw_data: Function written in main.py to visualize the list
    :param time_value: Float based on the input for the time between steps
    """
    # stop when the start and end index are equal (or when start > end)
    if start >= end:
        return

    pivot_index = partition(data_list, start, end, draw_data, time_value)

    # sorting the first half of the data
    quick_sort(data_list, start, pivot_index, draw_data, time_value)

    # sorting the second half of the data
    quick_sort(data_list, pivot_index + 1, end, draw_data, time_value)

    # color the whole list green after the sort
    draw_data(data_list, ["green" for i in range(len(data_list))])

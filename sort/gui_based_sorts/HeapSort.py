import time
from Swap import _swap


def heapify(data_list, size, root_index, draw_data, time_value):
    """
    Heapifies the list and visualizes the steps
    Expected Complexity (heapify only): O(log(n)) (time) and O(1) (space)

    :param data_list: Python list to be heapified
    :param size: Integer of the size of the list to be heapified
    :param root_index: Integer of the index in the list of the root
    :param draw_data: Function written in main.py that visualizes the list
    :param time_value: Float based on the input for time between each step
    """

    # declare and locate the largest index and the children of the root
    largest_index = root_index
    left_index = (2 * root_index) + 1
    right_index = (2 * root_index) + 2

    # change the largest if the root is smaller than the left child
    if (left_index < size) and (data_list[root_index] < data_list[left_index]):
        largest_index = left_index

    # change the largest if the largest is smaller than the right child
    if (right_index < size) and (data_list[largest_index] < data_list[right_index]):
        largest_index = right_index

    # only changes if either the left or right child is larger than the root
    if largest_index != root_index:
        _swap(data_list, root_index, largest_index)

        # generate the color list to be visualized
        color_list = ["red" for x in range(len(data_list))]

        # color the two elements being swapped as blue
        for x in range(len(color_list)):
            if (x == root_index) or (x == largest_index):
                color_list[x] = "blue"

        # visualize the step and wait for the specified amount of time
        draw_data(data_list, color_list)
        time.sleep(time_value)

        # recurse again so that it is a complete heap
        heapify(data_list, size, largest_index, draw_data, time_value)


def heap_sort(data_list, draw_data, time_value):
    """
    Does a heap sort on a list and visualizes the steps
    Expected Complexity (Sort only): O(n*log(n)) (time) and O(1) (space)

    :param data_list: Python list to be sorted
    :param draw_data: Function written in main.py that visualizes the list
    :param time_value: Float based on the input for time between each step
    """

    # heapifies the list
    for i in range((len(data_list) // 2) - 1, -1, -1):
        heapify(data_list, len(data_list), i, draw_data, time_value)

    # draw the heapified list as blue before starting the popping from the heap
    draw_data(data_list, ["blue" for i in range(len(data_list))])
    time.sleep(time_value)

    for i in range(len(data_list) - 1, 0, -1):
        _swap(data_list, i, 0)

        # generate the color list to be visualized
        color_list = ["red" for x in range(len(data_list))]

        # color the two elements being swapped green
        for x in range(len(color_list)):
            if (x == i) or (x == 0):
                color_list[x] = "green"

        # visualize the swap and wait the specified amount of time
        draw_data(data_list, color_list)
        time.sleep(time_value)

        # heapify the remaining portion of the list
        heapify(data_list, i, 0, draw_data, time_value)

    # color the whole list as green after the sort
    draw_data(data_list, ["green" for i in range(len(data_list))])

import time
from Swap import _swap


def insertion_sort(data_list, draw_data, time_value):
    """
    Does an insertion list and visualizes the steps
    Expected Complexity (Sort only): O(n^2) (time) and O(1) (space)

    :param data_list: Python list to be sorted
    :param draw_data: Function written in main.py that visualizes the list
    :param time_value: Float based on the input for time between each step
    """
    for i in range(1, len(data_list)):
        j = i

        # takes one of the remaining values and inserts it back in the list
        while (j > 0) and (data_list[j] < data_list[j - 1]):
            _swap(data_list, j, j - 1)

            # generate the color list to be visualized
            color_list = ["red" for x in range(len(data_list))]

            # color the values being swapped green
            for x in range(len(color_list)):
                if (x == j) or (x == j - 1):
                    color_list[x] = "green"

            # visualize the step and wait for the specified amount of time
            draw_data(data_list, color_list)
            time.sleep(time_value)

            j -= 1

    # color the whole list green after the sort
    draw_data(data_list, ["green" for i in range(len(data_list))])

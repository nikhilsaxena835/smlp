import time
from Swap import _swap


def selection_sort(data_list, draw_data, time_value):
    """
    Does a selection sort on a list and visualizes it
    Expected Complexity (Sort only): O(n^2) (time) and O(1) (space)

    :param data_list: Python list to be sorted
    :param draw_data: Function written in main.py to visualize the list
    :param time_value: Float based on the input for the time between steps
    """
    for i in range(len(data_list)):
        min_index = i

        # locates the min in the remaining elements and move it to the bottom
        for j in range(i + 1, len(data_list)):
            if data_list[min_index] > data_list[j]:
                min_index = j

                # generate the color list to be visualized
                color_list = ["red" for x in range(len(data_list))]

                # color the min index blue
                for x in range(len(data_list)):
                    if x == min_index:
                        color_list[x] = "blue"

                # visualize the list and wait for the specified amount of time
                draw_data(data_list, color_list)
                time.sleep(time_value)

        _swap(data_list, i, min_index)

        # generate the color list to be visualized
        color_list = ["red" for x in range(len(data_list))]

        # color the values being swapped green
        for x in range(len(color_list)):
            if (x == i) or (x == min_index):
                color_list[x] = "green"

        # visualize the list and wait for the specified amount of time
        draw_data(data_list, color_list)
        time.sleep(time_value)

    # color the whole list green after the sort
    draw_data(data_list, ["green" for i in range(len(data_list))])

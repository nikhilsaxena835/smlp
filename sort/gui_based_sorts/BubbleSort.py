import time
from Swap import _swap


def bubble_sort(data_list, draw_data, time_value):
    """
    Does a bubble sort on a list and visualize the sort
    Expected Complexity (Sort Only): O(n^2) (time) and O(1) (space)

    :param data_list: Python list to be sorted
    :param draw_data: Function written in main.py that visualizes the list
    :param time_value: Float based on the input for time between each step
    """
    for i in range(len(data_list) - 1):

        for j in range(0, len(data_list) - i - 1):

            # bubble up the largets value to the top of the list
            if data_list[j] > data_list[j + 1]:
                _swap(data_list, j, j + 1)

                # generate a color list for the visualization function
                color_list = ["red" for x in range(len(data_list))]

                # color the two elements being swapped green
                for x in range(len(color_list)):
                    if (x == j) or (x == j + 1):
                        color_list[x] = "green"

                # visualize the step and wait for the time specified
                draw_data(data_list, color_list)
                time.sleep(time_value)

    # finally color all of the elements in the list green after the sort
    draw_data(data_list, ["green" for i in range(len(data_list))])

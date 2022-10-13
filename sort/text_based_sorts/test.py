# import the sorts here
from InsertionSort import insertion_sort
from SelectionSort import selection_sort
from BubbleSort import bubble_sort
from QuickSort import quick_sort
from MergeSort import merge_sort

# used to generate the rules
import random
import time


def generate_results(test_list, total_time, sort_type):
    """
    Takes the information from the test functions and builds the results
    into a string for readability

    :param test_list: Python list that is ideally sorted
    :param total_time: Time object that is total time of the sort
    :param sort_type: String of the done to get the result
    """

    # create an empty string
    result_str = ""

    # add the appropriate string based on if the list is sorted
    if test_list == sorted(test_list):
        result_str += "Test: Successful\t"
    else:
        result_str += "Test: Fail\t"

    # build the final string with the sort type given
    result_str += "{} sort time: {:5f} seconds".format(sort_type, total_time)

    return result_str


def test_bubble(user_int):

    # build the test list
    test_list = [i for i in range(user_int)]
    random.shuffle(test_list)

    # time tracking of the sort
    start_time = time.time()
    bubble_sort(test_list)
    final_time = time.time()

    # generate and print results
    total_time = final_time - start_time
    result_str = generate_results(test_list, total_time, "   Bubble")

    print(result_str)

    return None


def test_insertion(user_int):

    # build the test list
    test_list = [i for i in range(user_int)]
    random.shuffle(test_list)

    # time tracking of the sort
    start_time = time.time()
    insertion_sort(test_list, 0, len(test_list) - 1)
    final_time = time.time()

    # generate and print results
    total_time = final_time - start_time
    result_str = generate_results(test_list, total_time, "Insertion")

    print(result_str)

    return None


def test_selection(user_int):

    # build the test list
    test_list = [i for i in range(user_int)]
    random.shuffle(test_list)

    # time tracking of the sort
    start_time = time.time()
    selection_sort(test_list)
    final_time = time.time()

    # generate and print results
    total_time = final_time - start_time
    result_str = generate_results(test_list, total_time, "Selection")

    print(result_str)

    return None


def test_quick(user_int):

    # build the test list
    test_list = [i for i in range(user_int)]
    random.shuffle(test_list)

    # time tracking of the sort
    start_time = time.time()
    quick_sort(test_list, 0, len(test_list) - 1)
    final_time = time.time()

    # generate and print results
    total_time = final_time - start_time
    result_str = generate_results(test_list, total_time, "    Quick")

    print(result_str)

    return None


def test_merge(user_int):

    # build the test list
    test_list = [i for i in range(user_int)]
    random.shuffle(test_list)

    # time tracking of the sort
    start_time = time.time()
    merge_sort(test_list)
    final_time = time.time()

    # generate and print results
    total_time = final_time - start_time
    result_str = generate_results(test_list, total_time, "    Merge")

    print(result_str)

    return None


def main():

    # print a warning for the user about the O(n^2) algorithms
    warning_str = """
    The first 3 sorts in this program (bubble, insertion, and selection)
    will take a significant amount of time if you input something greater
    than 20,000.
                  """

    print(warning_str)

    # take input for the size
    try:
        user_int = int(input("\nInput the size of the list to be generated: "))

        if user_int < 0:
            user_int *= -1

    except ValueError:

        # sets a default size as exception handling
        user_int = 1000

    # run the test suite
    print("\n")

    test_bubble(user_int)
    test_insertion(user_int)
    test_selection(user_int)
    test_quick(user_int)
    test_merge(user_int)

    print("\n")

    return None


if __name__ == "__main__":
    main()

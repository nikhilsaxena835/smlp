# Selection sort in Python
# time complexity O(n*n)
# sorting by finding min_index
def selectionSort(array, size):
    sort_list = [[]]
    n = len(array)
    for ind in range(n):
        min_index = ind

        for j in range(ind + 1, n):
            sort_list.append(array.copy())
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])

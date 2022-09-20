import sbase


def insertionSort(self, arr):
    sort_list = [[]]
    swaplist = [[]]
    swap_larger = 0
    swap_smaller = 0
    swapped = 0
    print(arr)

    for i in range(1, len(arr)):
        swapped = 0
        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            swapped = 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    # Traverse through 1 to len(arr)

        arr[j + 1] = key
        print("sorted arr", sort_list)
        sbase.Ui_MainWindow.anim_store(self, sort_list, swaplist)





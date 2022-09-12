
import sbase


class bubble:
    def bubbleSort(self, arr):
        sort_list = [[]]
        n = len(arr)
        swap_larger = 0
        swap_smaller = 0
        # optimize code, so if the array is already sorted, it doesn't need
        # to go through the entire process
        swapped = False
        print(arr)
        # Traverse through all array elements
        for i in range(n - 1):
            print("arr", arr)

            # range(n) also work but outer loop will
            # repeat one time more than needed.
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                print("j arr", arr)
                sort_list.append(arr.copy())
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j + 1]:

                    swap_larger = arr[j]
                    swap_smaller = arr[j+1]
                    swapped = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

            if not swapped:
                # if we haven't needed to make a single swap, we
                # can just exit the main loop.
                return
        print("sorted arr", sort_list)
        sbase.Ui_MainWindow.anim_store(self, sort_list, swap_smaller, swap_larger)

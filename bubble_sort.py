
import sbase


class bubble:
    def bubbleSort(self, arr):
        sort_list = [[]]
        swaplist = [[]]
        n = len(arr)
        swap_larger = 0
        swap_smaller = 0
        # optimize code, so if the array is already sorted, it doesn't need
        # to go through the entire process
        swapped = 0
        print(arr)
        # Traverse through all array elements
        for i in range(n - 1):
            print("arr", arr)

            # range(n) also work but outer loop will
            # repeat one time more than needed.
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                swapped = 0
                print("j arr", arr)
                sort_list.append(arr.copy())
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j + 1]:

                    swap_larger = arr[j]
                    swap_smaller = arr[j+1]
                    swapped = 1
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    lst = [swap_smaller, swap_larger, swapped]
                    swaplist.append(lst)
                    print("swap list", swaplist)

                else:
                    lst = [swap_smaller, swap_larger, swapped]
                    swaplist.append(lst)
                    print("swap list", swaplist)

        print("sorted arr", sort_list)
        sbase.Ui_MainWindow.anim_store(self, sort_list, swaplist)
'''
sort_list is to maintain the array at each step. This will help in the animation. Even if the array elements do no get 
swapped a list is appended to the sort_list. swaplist is used to identify if a swap was done in the step and if swap
is done then which two elements were swapped. This helps to avoid manually figuring out the swapped elements during
the animation
'''
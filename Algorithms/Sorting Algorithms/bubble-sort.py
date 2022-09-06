from swap import swap


def bubble_sort(A):
    for i in range(len(A) - 1, -1, -1):
        swapped = False
        for j in range(i):
            if(A[j] > A[j + 1]):
                swap(A, j, j + 1)
                swapped = True
        # If no swaps done, array is sorted
        if not swapped:
            break
    return A


my_arr = [31, 12, 2, 25, 17]

print(bubble_sort(my_arr))

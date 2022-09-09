def merge(A, start, mid, end):
    left = A[start:mid + 1]
    right = A[mid + 1:end + 1]
    i = 0 # left array loop variable
    j = 0 # right array loop variable
    k = start # A array loop variable
    
    # Go through both left and right arrays and assign the values
    # to A based on which has lower value
    while (i < len(left) and j < len(right)):
        if (left[i] <= right[j]):
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    
    # If there are values left in the left array
    # (For example, all values in right are less than values in left)
    while (i < len(left)):
        A[k] = left[i]
        i += 1
        k += 1

    # If there are values left in the right array
    while (j < len(right)):
        A[k] = right[j]
        j += 1
        k += 1

def merge_sort(A, start, end):
    if (start < end):
        mid = start + ((end - start) // 2)
        merge_sort(A, start, mid)
        merge_sort(A, mid + 1, end)
        merge(A, start, mid, end)
    return A

my_arr = [31, 12, 2, 25, 17]

print(merge_sort(my_arr, 0, len(my_arr) - 1))

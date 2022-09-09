from swap import swap


def partition(A, p, r):
    '''
    Partitioning function which chooses the last element of array `A`
    as a pivot `p`, places numbers less than `p` at the left and numbers
    greater at the right. And then return the correct(sorted) position
    of `p`
    '''
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if (A[j] <= pivot):
            i += 1
            swap(A, i, j)
    i += 1
    swap(A, i, r)
    return i


def quick_sort(A, p, r):
    if (p < r):
        pivot = partition(A, p, r)
        quick_sort(A, p, pivot - 1)
        quick_sort(A, pivot + 1, r)
    return A


my_arr = [31, 12, 2, 25, 17]

print(quick_sort(my_arr, 0, len(my_arr) - 1))
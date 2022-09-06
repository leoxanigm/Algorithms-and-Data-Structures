def insertion_sort(A):
    '''
    Works by picking the next number in the array and picking a new
    position to insert it
    '''
    for i in range(1, len(A)):
        key = A[i]
        j = i
        while(j > 0 and key < A[j - 1]):
            A[j] = A[j - 1]
            j -= 1
        A[j] = key
    return A


my_arr = [31, 12, 2, 25, 17]

print(insertion_sort(my_arr))

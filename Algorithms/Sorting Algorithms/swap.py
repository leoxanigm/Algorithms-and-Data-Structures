def swap(A, i, j):
    '''
    Swaps two elements of array `A` based on their indexes `i` and `j`
    '''
    try:
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        return A
    except:
        return A
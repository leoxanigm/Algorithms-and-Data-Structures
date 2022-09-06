from swap import swap


def selection_sort(A):
    for i in range(len(A)):
        min = A[i]
        pos = i
        for j in range(i + 1, len(A)):
            if A[j] < min:
                min = A[j]
                pos = j
        swap(A, i, pos)
    return A


my_arr = [31, 12, 2, 25, 17]

print(selection_sort(my_arr))

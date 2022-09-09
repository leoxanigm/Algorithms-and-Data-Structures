def counting_sort(A, max_value):
    # Working array c of zeros with length of the maximum integer in A
    C = [0] * (max_value + 1)

    # Output array of sorted values in A
    B = [0] * len(A)

    for val in A:
        C[val] += 1

    for i in range(1, len(C)):
        C[i] = C[i - 1] + C[i]

    for i in range(len(B)):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]

    return B


my_arr = [31, 12, 2, 2, 17]
max_value = 31

print(counting_sort(my_arr, max_value))

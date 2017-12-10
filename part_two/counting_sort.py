def counting_sort(A, B, k):
    C = []
    for i in range(0, k):
        C.append(0)

    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1
    # print C

    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    # print C

    for j in range(0, len(A))[::-1]:
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]] - 1

A = [2, 5, 3, 0, 2, 3, 0, 3]
B = A[:]
counting_sort(A, B, 6)
print B
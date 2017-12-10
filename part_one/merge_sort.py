"""
@jetou
@date : 2017/12/9
@algorithms: merge-sort
"""
Max = 100000

def Merge_sort(A, p, r):
    if p < r:
        q = (p + r) / 2
        Merge_sort(A, p, q)
        Merge_sort(A, q+1, r)
        Merge(A, p, q, r)


def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(0, n1):
        L.append(A[p + i])

    for j in range(0, n2):
        R.append(A[q + j + 1])

    L.append(Max)
    R.append(Max)

    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

A = [2, 4, 5, 7, 1, 2, 3, 6]
A = [1, 9, 5, 2, 4, 6]
Merge_sort(A, 0, 5)
print A
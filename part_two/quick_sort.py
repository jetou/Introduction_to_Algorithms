"""
@jetou
@date : 2017/12/9
@algorithms: quick-sort
"""

import random

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q)
        quick_sort(A, q+1, r)

def partition(A, p, r):
    x = A[r-1]
    i = p - 1
    for j in range(p, r-1):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r-1] = A[r-1], A[i+1]
    return i + 1

A = []
for i in range(0, 8):
    A.append(random.randint(0, 1000))
print A

quick_sort(A, 0, len(A))

print A
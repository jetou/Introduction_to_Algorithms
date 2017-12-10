"""
@jetou
@date : 2017/12/9
@algorithms: heap-sort
"""

import random

def parent(i):
    return (i - 1) >> 1

def left(i):
    return (i << 1) + 1

def right(i):
    return (i << 1) + 2

def max_heapify(A, i, s):
    l, r = left(i), right(i)
    largest = i
    if l < s and A[l] > A[i]:
        largest = l
    if r < s and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, s)

def build_max_heap(A, s):
    for i in range(0, len(A) / 2)[::-1]:
        max_heapify(A, i, s)


def heap_sort(A):
    s = len(A)
    build_max_heap(A, s)
    for i in range(1, len(A))[::-1]:
        A[0], A[i] = A[i], A[0]
        s -= 1
        max_heapify(A, 0, s)


A = []
for i in range(0, 8):
    A.append(random.randint(0, 1000))
print A
s = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heap_sort(A)
print A
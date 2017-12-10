"""
@jetou
@date : 2017/12/9
@algorithms: insertion-sort
"""
def insertion_sort(A):
    A_length = len(A)
    for j in range(1, A_length):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i + 1] = key

a = [5, 2, 4, 6, 1, 3]
insertion_sort(a)
print a
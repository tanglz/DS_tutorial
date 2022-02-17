# Find the minimum value,
# swaps it with the value in the first position,
# and repeats these steps for the remainder of the list

arr = [8, 5, 2, 6, 9, 3, 1, 4, 7]


def min(array):
    i = 0
    min_num = array[i]
    while i < len(array):
        if array[i] < min_num:
            min_num = array[i]
        i = i + 1
    return min_num


def sort(A):
    for i in range(len(A)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        A[i], A[min_idx] = A[min_idx], A[i]
    print(A)


sort(arr)

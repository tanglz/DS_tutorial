# 1. Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
# 2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.
# https://www.educative.io/edpresso/merge-sort-in-python
# Basic info of binary recursion or tree recursion : https://www.geeksforgeeks.org/types-of-recursions/
# TOP-down
# recursively splits the list into sublists until sublist size is 1
# then merges those sublists to produce a sorted list

def split(arr):
    print('arr=', arr)
    if len(arr) <= 1:
        print('=====================================')
        return
    mid = int(round(len(arr) / 2))
    # Dividing the array elements
    L = arr[:mid]
    # into 2 halves
    R = arr[mid:]
    print('L=', L)
    print('R=', R)
    print('-----------------------------------')
    split(L)
    split(R)

# A = [38, 27, 43, 3, 9, 82, 10]
# split(A)


# merge two sorted list
def merge(left, right):
    print('left=', left)
    print('right=', right)
    arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    arr = arr + left[i:] + right[j:]
    return arr


l1 = [2, 5, 10]
r1 = [3, 4, 8]


# print(merge(l1, r1))


def sort(arr):
    if len(arr) <= 1:
        return
    # Finding the middle of the array  # // integer division
    # mid = len(arr) // 2
    mid = int(round(len(arr) / 2))

    # Dividing the array elements
    L = arr[:mid]

    # into 2 halves
    R = arr[mid:]

    # Sorting the first half
    sort(L)

    # Sorting the second half
    sort(R)

    i = j = 0
    k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k = k + 1
    # For all the remaining values
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


A = [38, 27, 43, 3, 9, 82, 10]
sort(A)
print(A)


# Bottom-up

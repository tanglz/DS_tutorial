#  Select a 'pivot' element from the array
#  Partition the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.

# Select a 'pivot'
# There are many different versions of quickSort that pick pivot in different ways.
# #  Always pick first element as pivot.
# #  Always pick last element as pivot
# #  Pick a random element as pivot.
# #  Pick median as pivot.

def pivot_first(array):
    return array[0]


def sort(array):
    less = []
    equal = []
    greater = []
    if len(array) <= 1:
        return array

    #  Always pick first element as pivot.
    pivot = array[0]
    # partition
    for x in array:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        elif x > pivot:
            greater.append(x)
    # tree recursion
    smaller = sort(less)
    greater = sort(greater)
    array = smaller + equal + greater
    return array


# arr = [10, 7, 8, 9, 1, 5, 11, 100, 32,5]
# a = sort(arr)
# print(a)

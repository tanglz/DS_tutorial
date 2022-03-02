# Insertion sort in Python
# https://www.programiz.com/dsa/insertion-sort

def insertion_sort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [1, 5, 3, 11, 9, 7]
insertion_sort(data)
print('Sorted Array in Ascending Order:')
print(data)

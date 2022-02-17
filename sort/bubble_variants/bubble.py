# compares adjacent elements and swaps them if they are in the wrong order.
# This simple algorithm performs poorly in real world use and is used primarily as an educational tool

def sort(array):
    # Traverse through all array elements
    for k in range(len(array)):
        # Last k elements are already in place
        for i in range(len(array) - k):
            # compare with the next item
            temp = array[i]
            if i + 1 < len(array) and temp > array[i + 1]:
                # swap
                array[i] = array[i + 1]
                array[i + 1] = temp


A = [10, 2, 7, 9, 4]
sort(A)
print(A)

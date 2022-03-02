# insertion sort, example gif: https://en.wikipedia.org/wiki/Insertion_sort#/media/File:Insertion-sort-example-300px.gif
# Take elements from the list one by one
# Insert them in their correct position into a new sorted list
# # loop all the previous items.
# # if the previous item is greater than the current item, move the previous to the next position
# # put the current item to the position

def take_element(array):
    for num in array:
        print(num)


def take_element2(array):
    for i in range(len(array)):
        print(array[i])


def take_element3(array):
    i = 0
    while i < len(array):
        print(array[i])
        i = i + 1


def find_previous_items(array):
    i = 1
    while i < len(array):
        print('current item:', array[i])

        j = i - 1
        while j >= 0:
            print('previous items:', array[j])
            j = j - 1
        print('-----------------------------------------')

        i = i + 1


def sort(array):
    i = 1  # current item start from index=1, the second number
    while i < len(array):
        print('before sort,arr=', array)
        temp = array[i]  # the current item
        print('current item:', temp)
        j = i - 1
        while j >= 0 and array[j] > temp:  # increase
            # if the previous item is greater than current item,
            array[j + 1] = array[j]  # move to the next position
            j = j - 1

        array[j + 1] = temp  # put the current item to the position
        i = i + 1
        print('arr=', array)
        print('----------------------------------------')


arr = [6, 5, 3, 1, 8, 7, 2, 4]

sort(arr)

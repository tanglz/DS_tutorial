# 3.5

arr = [2, 2, 1, 2, 2, 2]  # n = 6
arr2 = [1, 2, 3, 2, 4, 2, 9, 2, 5, 2]  # n = 10, the item should from 1 to 9


def find_repeat_1(array):
    # validation check
    l = len(array)
    if l < 6:
        return
    for m in array:
        c = 0
        for n in array:
            if n == m:
                c = c + 1
        if c == 5:
            return m


# print(find_repeat_1(arr))


# count a particular number in a list
def cnt(lst, x):
    c = 0
    for item in lst:
        if item == x:
            c = c + 1
    return c


# print(cnt(arr, 3))
# print(arr.count(3))


def find_repeat_2(array):
    # validation check
    l = len(array)
    if l < 6:
        return
    repeated_count = 5
    for num in range(1, l - 1):
        if cnt(array, num) == repeated_count:
            return num


# num = find_repeat_2(arr)
# print(num)


from sort.efficient.quick import sort


def find_repeat_3(array):
    a = sort(array)
    print(a)
    num = None
    for i in range(len(a)):
        if a[i] == a[i + 4]:
            num = a[i]
            break
    return num


print(find_repeat_3(arr2))

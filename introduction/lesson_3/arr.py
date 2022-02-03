from array import array

# type code:https://docs.python.org/3/library/array.html
list_1 = [10, 20, 30]
list_1_unsigned = [10, 20, -30]
list_2 = [10, 20.2, 30.6]
list_3 = ['10', '20', '30']
list_4 = ['10', 20.2, '30.6']

arr_1 = array('I', list_1)
print(arr_1)
arr_1_unsigned = array('i', list_1_unsigned)

arr_2 = array('d', list_2)

arr_3 = array('I', [int(i) for i in list_3])

arr_4 = array('d', [float(i) for i in list_4])
print(arr_4)
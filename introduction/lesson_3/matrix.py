# Numpy : https://numpy.org/doc/stable/dev/
# provides a multidimensional array object, various derived objects (such as masked arrays and matrices)
# fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation
import numpy as np

multi_list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# create a ndarray from a list
nd_arr = np.array(multi_list_1)
# print(nd_arr)
# # print(type(nd_arr))
# # # the shape is a tuple
# print(nd_arr.shape)

# # other methods to create ndarray
# a = np.arange(15).reshape(3, 5)
# print(a)
# print(np.arange(2,9,2))
# print(np.linspace(0,10,num=5))
# b = np.zeros((2, 3), dtype=np.int8)
# print(b)
# #
# c = np.ones((3, 3), dtype=int)
# print(c)
#
# #  function empty creates an array whose initial content is random and depends on the state of the memory.
# d = np.empty((2, 4), dtype=int)
# print(d)

# # basic operations
# num_row = nd_arr.shape[0]
# print(num_row)
# num_col = nd_arr.shape[1]
# print(num_col)
# # # # access the ith row and col
# ith_row = nd_arr[0, :]
# print(ith_row)
# ith_col = nd_arr[:, 0]
# print(ith_col)
# # # # sum
# total_first_row = sum(nd_arr[0, :])
# print(total_first_row)
# #
# total_first_col = sum(nd_arr[:, 0])
# print(total_first_col)

# concatenate
arr_1 = np.array([1, 2, 3, 4])
arr_2 = np.array([5, 6, 7, 8])
# print(np.concatenate((arr_1, arr_2)))
#
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
# print(np.concatenate((x, y)))

# stack
# print(np.vstack((arr_1,arr_2)))
# print(np.hstack((arr_1,arr_2)))
# print(np.vstack((x,y)))

# reshape
arr_3 = np.arange(6)
arr_4 = arr_3.reshape(3, 2)
# print(arr_4)
arr_5 = np.reshape(arr_3, newshape=(2, 3))

# select by condition
# z = np.arange(2, 15, 2)
# print(z)
# con_1 = (z > 5)
# print(z[con_1])
# con_2 = (z % 4 == 0)
# print(z[con_2])
# con_3 = ((z > 5) & (z < 10))
# print(z[con_3])


########## Views are an important NumPy concept!
# NumPy functions, as well as operations like indexing and slicing, will return views whenever possible.
# This saves memory and is faster (no copy of the data has to be made).
# However it’s important to be aware of this - modifying data in a view also modifies the original array!
w = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(w)
# v = w[0,:]
# print(v)
# v[0] = 999
# print(v)
# print(w)

# p = w.copy()
# print(p)
# p[0][0] = 88
# print(p)
# print(w)

# operator
# a_1 = np.array([1,2,3])
# print(a_1+3)
# print(a_1*2)
# a_2 = np.array([4,5,6])
# print(a_1+a_2)
# a_3 = np.array([7,8,9])
# print(a_1+a_2+a_3)

# reverse
# arr_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(arr_2d)
# print(np.flip(arr_2d))
# print(np.flip(arr_2d, axis=0)) # only the rows

# rotate 90 degree
arr_2d_2 = np.array([[1,1,1],[2,2,2],[3,3,3]])
print(arr_2d_2)
print(np.rot90(arr_2d_2, k=1))
print(np.rot90(arr_2d_2, k=2))
print(np.rot90(arr_2d_2, k=3))
print(np.rot90(arr_2d_2, k=4))


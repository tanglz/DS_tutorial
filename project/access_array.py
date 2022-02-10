import numpy as np

# diagonal array
x = 4
arr = np.arange(16).reshape(x, x)
print(arr)
diagonal_c = []
diagonal_c_u_1 = []
diagonal_c_d_1 = []
for i in range(x):
    diagonal_c.append(arr[i][i])
    if i + 1 < x:
        diagonal_c_u_1.append(arr[i][i + 1])
        diagonal_c_d_1.append(arr[i + 1][i])
print('list diagonal:', diagonal_c)
print('sum_c=', sum(diagonal_c))
print('list diagonal offset 1', diagonal_c_u_1)
print('list diagonal offset -1', diagonal_c_d_1)

# diagonal array (method 2)
print('np array diagonal: ', np.diagonal(arr, 0, 0, 1))
print('np array diagonal, offset 1: ', np.diagonal(arr, 1, 0, 1))
print('np array diagonal, offset -1: ', np.diagonal(arr, -1, 0, 1))
print('np array diagonal, offset -2: ', np.diagonal(arr, -2, 0, 1))


# Threshold
def average_1(l):
    return sum(l) / len(l)


print(average_1(diagonal_c))
#
r_average = round(average_1(diagonal_c), 0)
print(r_average)


def average_2(l):
    a = np.asarray(l)
    return a.mean()


print(average_2(diagonal_c))


# C
def generate_c(p):
    c = []
    for item in p:
        if item > r_average:
            c.append(1)
        else:
            c.append(0)
    return c


#
#
c1 = generate_c(diagonal_c_u_1)
c2 = generate_c(diagonal_c_d_1)
print('c1:', c1)
print('c2:', c2)


#
#
# # hamming distance
# # The Hamming distance between two equal-length strings of symbols is the number of positions at which the corresponding symbols are different.
def hamming_distance(str1, str2):
    d = 0
    for c1, c2 in zip(str1, str2):  # zip() Iterate over several iterables in parallel
        if c1 != c2:
            d = d + 1
    return d


#
#
# # # List comprehensions : https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
string_c1 = [str(n) for n in c1]  # ['0','0','1']
string_c2 = [str(n) for n in c2]
# '001'
d1 = hamming_distance(''.join(string_c1), ''.join(string_c2))
print('d1=', d1)

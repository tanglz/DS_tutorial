from array import array

# type code:https://docs.python.org/3/library/array.html
l = [10, 20, 30, 40]
a = array('H', l)
print(a)
s = sum(a)
print(s)
b = a[1:3]
print(b)
nl = a.tolist()
print(nl)

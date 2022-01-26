# begin a string with f or F before the opening quotation mark.
# Inside this string, you can write a Python expression between { and } characters that can refer to variables or literal values.
# name = 'Bree'
# res = f'Hello {name}'
# print(res)

# str.format() method, using curly brackets { and }
# Further reading https://docs.python.org/3/library/string.html#formatspec
pos = 968
total = 1000
percentage = pos / total
print(percentage)
res2 = 'The accuracy is {:.2%}'.format(percentage)
print(res2)

# convert any value to a string with the repr() or str() functions
# s = 'Hello, world.'
# print(str(s))
# print(repr(s))
# n = 10
# print(str(n))
# print(repr(n))


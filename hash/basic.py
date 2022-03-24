# Dictionary in Python https://docs.python.org/3/tutorial/datastructures.html
dic = {'a':1,'b':2,'c':3,'d':4,'e':5}
# # access
print(dic['a'])
print(dic.get('a'))
if 'a' in dic:
    print(True)
else:
    print(False)

print('--------------------------------')
# # loop
for key, value in dic.items():
    print(key,value)
print('--------------------------------')
for index,item in enumerate(dic):
    print(index,item)

print('--------------------------------')

# # merge two lists to dic
a = ['name','age','class']
b = ['a',10,'112']
dic_t={}
for title,value in zip(a,b):
    dic_t[title] = value
print(dic_t)

# # key's Data types
dic_i={1:10,2:20,30:300}
print(dic_i[1])
dic_b={True:'s',False:'g'}
print(dic_b[True])


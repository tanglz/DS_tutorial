# Control flow tools

# # if statements
def check_status(s):
    if s ==0:
        print('ok')
    else:
        print('not ok')

# check_status(0)

# # for statements
# names =["Bree","Matt","Lisa","selena"]
# for item in names:
#     print("Hello",item)

# # while (Fibonacci series)
a = 0
b = 1
while a < 10:
    a  = b
    b = b+1
    # print(a)

# # built-in function range()
for i in range(5):
    for j in range(10):
        if i + j ==2:
            break
        else:
            print(i)
# # break : break out of the innermost enclosing for or while loop

# # pass

# # match



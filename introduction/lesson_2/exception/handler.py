# A High level text editor can help up find syntax errors.
# a = True
# Exception: Errors detected during execution

# a = 10 * (1/0)
#
# spam = '%'
# b = 4 + spam*3
#
# c = '2' + 2

# handling exceptions
def func_addition(x1, x2):
    try:
        y = x1 + x2
        return y
        print(y)
    except TypeError:
        print('ERROR! The arguments should be numbers.')
    finally:
        print("It's done!")


result = func_addition(4, 4)
print(result)
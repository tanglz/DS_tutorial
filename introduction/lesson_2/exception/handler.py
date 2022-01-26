# A High level text editor can help up find syntax errors.

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
        print(y)
    except TypeError:
        print('ERROR! The arguments should be numbers.')


func_addition(4, '0.4')

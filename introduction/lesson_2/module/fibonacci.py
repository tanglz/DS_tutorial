# A module is a file containing Python definitions and statements.
# The file name is the module name with the suffix .py appended.
# Within a module, the module’s name (as a string) is available as the value of the global variable __name__.

# # write Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    print('fib1:')
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


# # return Fibonacci series up to n
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    print('fib2',result)

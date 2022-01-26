def fib3(n):
    print('fib3:')
    a, b = 0, 1
    while a < n:
        print(b, end=' ')
        a, b = b, a + b
    print()
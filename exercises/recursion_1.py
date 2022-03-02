# 3.7

def product(n, m):
    if m == 1:
        return n
    return n + product(n, m - 1)


s = product(6, 4)
print(s)

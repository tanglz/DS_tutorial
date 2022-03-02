# 3.6

import numpy as np

n = 2000
M = np.zeros((n, n))

print(M)

C = np.ones(n)


def meet(i, j):
    if M[i, j] == 1:
        pass
    else:
        M[i, j] = 1
        C[i] = C[i] + 1
        C[j] = C[j] + 1


def check_winner(x):
    if C[x] == n:
        print(f'Player number {x} is the winner!')
    else:
        print(f'Player number {x}, you need keep going!')


check_winner(1)


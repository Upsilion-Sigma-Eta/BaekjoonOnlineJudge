import sys
import math

sys.setrecursionlimit(10 ** 9)

const_mod = 10 ** 9 + 7

def calc_target_D(D, k, c, p, c_powers):
    if (k in D):
        return D[k]

    for i in range(p, k + 1):
        current_index_D = 0
        for j in range(1, p):
            current_index_D += c_powers[j] * D[i - j]
            if (abs(current_index_D) > const_mod):
                current_index_D %= const_mod
        current_index_D *= -1
        D[i] = current_index_D

    return D[k]

def Solution():
    p, c, k = map(int, sys.stdin.readline().strip().split())

    M = list(map(int, sys.stdin.readline().strip().split()))

    D = {}

    for i in range(1, p):
        D[i] = (M[i] - M[i - 1])

    c_powers = [1] * p

    for i in range(1, p):
        c_powers[i] = (c_powers[i - 1] * c) % const_mod

    result = calc_target_D(D, k, c, p, c_powers)

    sys.stdout.write(str(abs(D[k])))

if __name__ == "__main__":
    Solution()
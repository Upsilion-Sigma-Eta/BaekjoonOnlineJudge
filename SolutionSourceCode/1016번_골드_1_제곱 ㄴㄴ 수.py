import sys
import math

def actual_code():
    min_val, max_val = map(int, sys.stdin.readline().split())

    is_square_nono = [True] * (max_val - min_val + 1)

    for i in range(2, math.isqrt(max_val) + 1):
        square = i * i
        start = ((min_val + square - 1) // square) * square
        for j in range(start, max_val + 1, square):
            is_square_nono[j - min_val] = False

    sys.stdout.write(str(is_square_nono.count(True)))

if __name__ == '__main__':
    actual_code()
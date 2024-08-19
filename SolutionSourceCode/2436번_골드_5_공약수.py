import sys
import math

def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def Solution():
    g, l = map(int, sys.stdin.readline().strip().split())

    condition_0 = (g * l) // (g * g)

    result = []

    for i in range(1, math.isqrt(condition_0) + 1, 1):
        if (condition_0 % i == 0):
            j = condition_0 // i
            if (euclidean_algorithm(i, j) == 1):
                result.append((i * g, j * g))

    result = sorted(result, key=lambda x: x[0] + x[1])

    sys.stdout.write(str(result[0][0]) + " " + str(result[0][1]) + "\n")


if __name__ == "__main__":
    Solution()
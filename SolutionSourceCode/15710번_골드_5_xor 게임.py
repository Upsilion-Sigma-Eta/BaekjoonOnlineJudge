import sys

const_mod = 10 ** 9 + 7

def power(x, n):
    result = 1

    while n > 0:
        if n % 2 == 1:
            result = (result * x) % const_mod
        x = (x * x) % const_mod
        n = n // 2

    return result

def Solution():
    a, b, n = map(int, sys.stdin.readline().strip().split())

    sys.stdout.write(str(power(2 ** 31, n - 1)))

if __name__ == "__main__":
    Solution()
import sys
import math

def fast_power_and_mod(a, b, m):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = result * a % m
        b //= 2
        a = (a * a) % m

    return result

def eratostenes_filter_checker(p):
    number_range = math.isqrt(p)

    sieve = [True] * (number_range + 1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, number_range + 1):
        if (sieve[i] == True):
            for j in range(i * i, number_range + 1, i):
                sieve[j] = False

    for i in range(2, number_range + 1):
        if (sieve[i] == True):
            if (p % i == 0):
                return False

    return True

def is_prime_checker(p):
    if (p == 1 or p == 0):
        return False

    for i in range(2, math.isqrt(p) + 1):
        if (p % i == 0):
            return False

    return True

def Solution():
    while True:
        p, a = map(int, sys.stdin.readline().strip().split())

        if (p == 0 and a == 0):
            break

        if (is_prime_checker(p) == False):
            if (fast_power_and_mod(a, p, p) == a):
                sys.stdout.write("yes\n")
            else:
                sys.stdout.write("no\n")
        else:
            sys.stdout.write("no\n")

if __name__ == "__main__":
    Solution()
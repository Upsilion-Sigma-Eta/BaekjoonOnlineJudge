import sys
from collections import Counter
import math

def sum_of_combinations(n, r):
    total = 0
    total += (1 << n)
    return total

def actual_code():
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))

    number_appear_counter = Counter(A)
    duplicated_appeared = [v for k, v in number_appear_counter.items() if v > 1]
    unique_appeared = [v for k, v in number_appear_counter.items() if v == 1]

    winning_case = 1
    for _ in range(len(duplicated_appeared)):
        winning_case *= math.comb(duplicated_appeared[_], 1) + math.comb(duplicated_appeared[_], 0)

    for _ in range(len(unique_appeared)):
        winning_case *= math.comb(unique_appeared[_], 1) + math.comb(unique_appeared[_], 0)

    sys.stdout.write(str((winning_case - 1) % (10 ** 9 + 7)))

if __name__ == '__main__':
    actual_code()

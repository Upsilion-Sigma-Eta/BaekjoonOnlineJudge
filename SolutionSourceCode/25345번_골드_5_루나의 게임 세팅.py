import sys
import math
import itertools

# need calculate 3 cases
# 1. ascending order
# 2. descending order
# 3. based on middle, front is ascending order and back is descending order
# but it's too slow to calculate all cases
# also case 3 includes case 1 and case 2
def actual_code():
    N, K = map(int, sys.stdin.readline().strip().split())

    A = list(map(int, sys.stdin.readline().strip().split()))

    counter = 0

    for mid in range(K):
        left = mid
        right = K - mid - 1
        counter += math.comb(N, K) * math.comb(K - 1, left)

    sys.stdout.write(str(counter % (10 ** 9 + 7)))

if __name__ == '__main__':
    actual_code()
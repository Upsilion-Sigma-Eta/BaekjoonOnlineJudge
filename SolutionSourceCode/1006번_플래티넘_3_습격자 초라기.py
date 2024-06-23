import sys
import copy


# 아인스트라세의 SW 블로그 백준 1006번 습격자 초라기 문제 풀이 referenced.
# https://casterian.net/ps/boj1006/ referenced

MAX_SIZE = 10000

# You should not check every tile via for loop.
# Yoy shouuld check 'what if previous steps taked this, and i moved this in current step, how many squad needed?'
# So basically, you should memorize on every possible filling options.
top = [float('inf')] * (MAX_SIZE + 1)
bottom = [float('inf')] * (MAX_SIZE + 1)
both = [float('inf')] * (MAX_SIZE + 1)

def smarter_grouping_method(sector, N, W, start):
    for i in range(start, N):
        both[i + 1] = min(top[i] + 1, bottom[i] + 1)
        if sector[0][i] + sector[1][i] <= W:
            both[i + 1] = min(both[i + 1], both[i] + 1)
        if i > 0 and sector[0][i - 1] + sector[0][i] <= W and sector[1][i - 1] + sector[1][i] <= W:
            both[i + 1] = min(both[i + 1], both[i - 1] + 2)
        if i < N - 1:
            top[i + 1] = both[i + 1] + 1
            if sector[0][i] + sector[0][i + 1] <= W:
                top[i + 1] = min(top[i + 1], bottom[i] + 1)
            bottom[i + 1] = both[i + 1] + 1
            if sector[1][i] + sector[1][i + 1] <= W:
                bottom[i + 1] = min(bottom[i + 1], top[i] + 1)

def actual_code():
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N, W = map(int, sys.stdin.readline().strip().split())
        CLEARED = W * 2

        inner_sector = list(map(int, sys.stdin.readline().strip().split())) # Inner circle

        outer_sector = list(map(int, sys.stdin.readline().strip().split())) # Outer circle

        sector = [outer_sector, inner_sector]

        both[0] = 0
        top[0] = bottom[0] = 1

        smarter_grouping_method(sector, N, W, 0)

        ans = float('inf')

        ans = min(ans, both[N])

        if N > 1 and sector[0][0] + sector[0][N - 1] <= W:
            both[1] = 1
            top[1] = 2
            if sector[1][0] + sector[1][1] <= W:
                bottom[1] = 1
            else:
                bottom[1] = 2
            smarter_grouping_method(sector, N, W, 1)
            ans = min(ans, bottom[N - 1] + 1)

        if N > 1 and sector[1][0] + sector[1][N - 1] <= W:
            both[1] = 1
            if sector[0][0] + sector[0][1] <= W:
                top[1] = 1
            else:
                top[1] = 2
            bottom[1] = 2
            smarter_grouping_method(sector, N, W, 1)
            ans = min(ans, top[N - 1] + 1)

        if N > 1 and sector[0][0] + sector[0][N - 1] <= W and sector[1][0] + sector[1][N - 1] <= W:
            both[1] = 0
            top[1] = bottom[1] = 1
            smarter_grouping_method(sector, N, W, 1)
            ans = min(ans, both[N - 1] + 2)

        sys.stdout.write(str(ans) + '\n')


if __name__ == '__main__':
    actual_code()
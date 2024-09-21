import sys
from collections import deque

CONST_MOD = (10 ** 9) + 9


def Solve(grid_map, N, M):
    dp = [[0] * M for _ in range(N)]

    # 목적지 X에 대해서 dp 초기 값 설정
    for i in range(N):
        for j in range(M):
            if grid_map[i][j] == 'X':
                dp[i][j] = 1

    # 목적지에서 시작점까지 역방향으로 탐색 진행
    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            if grid_map[i][j] == 'X':
                continue  # 'X' cells are already initialized
            if grid_map[i][j] in ('E', 'B') and j + 1 < M:
                dp[i][j] = (dp[i][j] + dp[i][j + 1]) % CONST_MOD
            if grid_map[i][j] in ('S', 'B') and i + 1 < N:
                dp[i][j] = (dp[i][j] + dp[i + 1][j]) % CONST_MOD

    # 총 경로 수 계산
    total = 0
    for i in range(N):
        for j in range(M):
            total = (total + dp[i][j]) % CONST_MOD

    return total

def Solution():
    N, M = map(int, sys.stdin.readline().strip().split())
    grid_map = []

    for _ in range(N):
        grid_map.append(sys.stdin.readline().strip())

    way = Solve(grid_map, N, M)

    sys.stdout.write(str(way))


if __name__ == "__main__":
    Solution()
import sys

def Solution():
    N, M = map(int, sys.stdin.readline().strip().split())

    fuel_grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    dp = [[[float('inf')] * M for _ in range(N)] for _ in range(3)]

    for j in range(M):
        for move in range(3):
            dp[move][0][j] = fuel_grid[0][j]

    # 차례대로 왼쪽 하단, 중앙 하단, 우측 하단
    moves = [-1, 0, 1]

    for i in range(1, N):
        for j in range(M):
            for move in range(3):
                prev_j = j - moves[move]
                if 0 <= prev_j < M:
                    for prev_move in range(3):
                        if move != prev_move:
                            dp[move][i][j] = min(dp[move][i][j], dp[prev_move][i - 1][prev_j] + fuel_grid[i][j])

    result = min(dp[move][N - 1][j] for move in range(3) for j in range(M))
    print(result)

if __name__ == "__main__":
    Solution()

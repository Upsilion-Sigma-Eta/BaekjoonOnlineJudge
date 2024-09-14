import sys

sys.setrecursionlimit(100000)

def max_score(N, M, board, match_string):
    dp = [[0] * M for _ in range(N)]

    for i in range(N):
        if board[i] == match_string[0]:
            dp[i][0] = 1

    for j in range(1, M):
        for i in range(N):
            if board[i] == match_string[j]:
                # 현재 문자와 일치하는 경우, 왼쪽이나 오른쪽에서 오는 최대 점수를 구하고 +1
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                if i < N - 1:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + 1)
            else:
                # 현재 문자가 일치하지 않는 경우, 최대 점수는 이전 상태에서의 최대값
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])
                if i < N - 1:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - 1])

    # 최대 점수 계산
    max_score = 0
    for i in range(N):
        max_score = max(max_score, dp[i][M - 1])

    return max_score

def Solution():
    N, M = map(int, sys.stdin.readline().strip().split())

    board = sys.stdin.readline().strip()
    match_string = sys.stdin.readline().strip()

    result = max_score(N, M, board, match_string)

    print(result)

if __name__ == "__main__":
    Solution()

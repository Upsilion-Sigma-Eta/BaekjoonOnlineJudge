import sys

def Solution():
    T, W = map(int, sys.stdin.readline().strip().split())

    tree_falling_order = []

    for i in range(T):
        tree_falling_order.append(int(sys.stdin.readline().strip()))

    dp = [[0] * (W + 1) for _ in range(T + 1)]
    
    for t in range(1, T + 1):
        for w in range(W + 1):
            if tree_falling_order[t - 1] == 1:
                # 현재 나무가 1번 나무일 때
                dp[t][w] = dp[t - 1][w] + 1 if w % 2 == 0 else dp[t - 1][w]
                if w > 0:
                    dp[t][w] = max(dp[t][w], dp[t - 1][w - 1] + 1 if w % 2 == 1 else dp[t - 1][w - 1])
            else:
                # 현재 나무가 2번 나무일 때
                dp[t][w] = dp[t - 1][w] + 1 if w % 2 == 1 else dp[t - 1][w]
                if w > 0:
                    dp[t][w] = max(dp[t][w], dp[t - 1][w - 1] + 1 if w % 2 == 0 else dp[t - 1][w - 1])


    sys.stdout.write(str(max(dp[T])))

Solution()
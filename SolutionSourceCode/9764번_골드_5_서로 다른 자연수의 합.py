import sys


def q_strict_partition(N, dp):
    for i in range(1, N + 1):
        for j in range(N, i - 1, -1):
            dp[j] += dp[j - i]

    return dp[N]


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N = int(sys.stdin.readline().strip())

        dp = [0] * (N + 1)
        dp[0] = 1

        result = q_strict_partition(N, dp)

        sys.stdout.write(str(result % 100999) + "\n")


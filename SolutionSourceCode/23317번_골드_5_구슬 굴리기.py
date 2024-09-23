import sys

def Solution():
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())

    must_pass_point = []

    for _ in range(m):
        row, col = map(int, sys.stdin.readline().strip().split())
        must_pass_point.append((row, col))

    must_pass_point = sorted(must_pass_point, key=lambda x: x[0])

    # dp 🠂 파스칼의 삼각형
    dp = [[1] * (i + 1) for i in range(n)]

    # 파스칼의 삼각형 초기화
    for i in range(2, n):
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    result = 1
    # (0, 0)에서 첫 번째 포인트까지의 경로를 고려
    start_point = (0, 0)
    points = [start_point] + must_pass_point

    for i in range(m):
        point_current = points[i]
        point_next = points[i + 1]

        point_coord_diff = (point_next[0] - point_current[0], point_next[1] - point_current[1])

        # 이동 불가능한 경우 (x 좌표가 더 크거나, 차이보다 더 멀리 갈 수 없을 때)
        if point_coord_diff[0] < 0 or point_coord_diff[1] < 0 or point_coord_diff[1] > point_coord_diff[0]:
            print(0)
            return

        binomial_value = dp[point_coord_diff[0]][point_coord_diff[1]]
        result *= binomial_value

    # 마지막 포인트에서 (n-1, x)로의 이동 가능 경로 고려
    result *= pow(2, (n - 1) - must_pass_point[-1][0])

    print(result)

if __name__ == "__main__":
    Solution()
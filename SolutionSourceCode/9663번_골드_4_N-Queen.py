import sys

# 1 = Queen 0 = Empty

def SafeChecker(grid, r, c, N):
    # 동일 행에 이미 다른 퀸이 배치되어 있는지 확인할 필요는 없음 (기본적으로 한 행씩 증가시키면서 확인하기 떄문에)

    # 동일 열에 이미 다른 퀸이 배치되어 있는지 확인
    for i in range(N):
        if grid[i][c] == 1:
            return False

    # 대각선으로 다른 퀸이 배치되어 있는지 확인
    # 왼쪽 위 대각선
    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if grid[i][j] == 1:
            return False

    # 오른쪽 아래 대각선
    for i, j in zip(range(r, N, 1), range(c, N, 1)):
        if grid[i][j] == 1:
            return False

    # 오른쪽 위 대각선
    for i, j in zip(range(r, -1, -1), range(c, N, 1)):
        if grid[i][j] == 1:
            return False

    # 왼쪽 아래 대각선
    for i, j in zip(range(r, N, 1), range(c, -1, -1)):
        if grid[i][j] == 1:
            return False

    return True

def Solver(N, row, columns, left_to_right_diag, right_to_left_diag):
    if row >= N:
        return 1

    counter = 0
    for col in range(N):
        if col in columns or (row + col) in left_to_right_diag or (row - col) in right_to_left_diag:
            continue

        columns.add(col)
        left_to_right_diag.add(row + col)
        right_to_left_diag.add(row - col)

        counter += Solver(N, row + 1, columns, left_to_right_diag, right_to_left_diag)

        columns.remove(col)
        left_to_right_diag.remove(row + col)
        right_to_left_diag.remove(row - col)

    return counter

def Solution():
    N = int(sys.stdin.readline())

    grid = [[0] * N for _ in range(N)]

    result = Solver(N, 0, set(), set(), set())

    sys.stdout.write(str(result) + "\n")

if __name__ == "__main__":
    Solution()
import sys

def actual_code():
    N, M = map(int, sys.stdin.readline().strip().split(' '))

    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    # if you want what tetrimino shape result best sum, change it to list
    sum_max = set()
    # 4x1 Sliding Window
    for i in range(N):
        for j in range(M):
            if (i) >= N or (j + 3) >= M:
                break
            sum_max.add(board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i][j + 3])

    # 1x4 Sliding Window
    for i in range(N):
        for j in range(M):
            if (i + 3) >= N or (j) >= M:
                break
            sum_max.add(board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 3][j])

    # 2x2 Sliding Window
    for i in range(N):
        for j in range(M):
            if (i + 1) >= N or (j + 1) >= M:
                break
            sum_max.add(board[i][j] + board[i + 1][j] + board[i][j + 1] + board[i + 1][j + 1])

    # 2x3 Sliding Window
    for i in range(N):
        for j in range(M):
            if (i + 2) >= N or (j + 1) >= M:
                break
            sum_max.add(board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 2][j + 1])
            sum_max.add(board[i][j + 1] + board[i + 1][j + 1] + board[i + 2][j + 1] + board[i + 2][j])
            sum_max.add(board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i + 2][j + 1])
            sum_max.add(board[i][j] + board[i][j + 1] + board[i + 1][j] + board[i + 2][j])

            sum_max.add(board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j + 1])
            sum_max.add(board[i][j + 1] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j])

            sum_max.add(board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j])
            sum_max.add(board[i][j + 1] + board[i + 1][j + 1] + board[i + 1][j] + board[i + 2][j + 1])

    # 3x2 Sliding Window
    for i in range(N):
        for j in range(M):
            if (i + 1) >= N or (j + 2) >= M:
                break
            sum_max.add(board[i][j + 2] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 1][j + 2])
            sum_max.add(board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 1][j + 2])
            sum_max.add(board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j])
            sum_max.add(board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j + 2])

            sum_max.add(board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i + 1][j + 2])
            sum_max.add(board[i][j + 1] + board[i][j + 2] + board[i + 1][j] + board[i + 1][j + 1])

            sum_max.add(board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j + 1])
            sum_max.add(board[i][j + 1] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 1][j + 2])

    sum_max_list = list(sum_max)
    sum_max_list.sort(reverse=True)

    sys.stdout.write(str(sum_max_list[0]) + "\n")


if __name__ == '__main__':
    actual_code()
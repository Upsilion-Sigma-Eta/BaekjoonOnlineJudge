import sys
import copy

def sliding_winodw(grid, k, a, b):
    window = []
    window_width = k * 3
    window_height = k * 3

    total_cost = set()
    # 슬라이딩 윈도우 크기만큼 전체 영역을 휩쓸면서 값을 계산
    cost = 0

    for i in range(len(grid) - window_height + 1):
        for j in range(len(grid[0]) - window_width + 1):
            cost = 0
            temp_grid = copy.deepcopy(grid)
            for i_i in range(window_height):
                for j_j in range(window_width):
                    if (0 <= i_i < k):
                        cost += 0 if grid[i + i_i][j + j_j] == '#' else a
                    elif (k <= i_i < k * 2 and 0 <= j_j < k):
                        cost += 0 if grid[i + i_i][j + j_j] == '#' else a
                    elif (k * 2 <= i_i < k * 3):
                        cost += 0 if grid[i + i_i][j + j_j] == '#' else a
                    else:
                        cost += 0 if grid[i + i_i][j + j_j] == '.' else b
                    temp_grid[i + i_i][j + j_j] = '@'

            for i_i in range(len(grid)):
                for j_j in range(len(grid[0])):
                    if temp_grid[i_i][j_j] != '@':
                        cost += 0 if grid[i_i][j_j] == '.' else b

            total_cost.add(cost)

    return total_cost

def actual_code():
    n, m = map(int, sys.stdin.readline().strip().split())
    a, b = map(int, sys.stdin.readline().strip().split())

    grid = []
    for _ in range(n):
        grid.append(list(sys.stdin.readline().strip()))

    total_cost = set()

    for i in range(1, min(n, m) // 3 + 1):
        total_cost.update(sliding_winodw(grid.copy(), i, a, b))

    sys.stdout.write(str(min(total_cost)))

if __name__ == '__main__':
    actual_code()

import sys
from collections import deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(grid, start, start_fire):
    rows = len(grid)
    cols = len(grid[0])

    queue = deque([start])
    fire_queue = deque(start_fire)

    visited = [[False] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = True

    counter = 1
    while queue:
        for _ in range(len(fire_queue)):
            f_x, f_y = fire_queue.popleft()

            grid[f_x][f_y] = 'F'

            if f_x == -1 and f_y == -1:
                continue

            for dx, dy in DIRECTIONS:
                nx = f_x + dx
                ny = f_y + dy

                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '.':
                    grid[nx][ny] = 'F'
                    fire_queue.append((nx, ny))

        for _ in range(len(queue)):
            row, col = queue.popleft()

            if (grid[row][col] == '.' or grid[row][col] == 'J') and ((row == 0 or row == rows - 1) or (col == 0 or col == cols - 1)):
                return counter

            for dx, dy in DIRECTIONS:
                nx = row + dx
                ny = col + dy

                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == '.':
                    visited[nx][ny] = True

                    if (grid[nx][ny] == '.' or grid[row][col] == 'J') and ((nx == 0 or nx == rows - 1) or (ny == 0 or ny == cols - 1)):
                        return counter + 1

                    queue.append((nx, ny))

        counter += 1

    return -1

def actual_code():
    R, C = map(int, sys.stdin.readline().strip().split())

    grid = []
    start_point = (-1, -1)
    fire_start_point = []
    for _ in range(R):
        grid.append(list(sys.stdin.readline().strip()))
        for c in range(C):
            if (grid[-1][c] == 'J'):
                start_point = (_, c)
            elif (grid[-1][c] == 'F'):
                fire_start_point.append((_, c))

    result_counter = bfs(grid, start_point, fire_start_point)

    if (result_counter == -1):
        sys.stdout.write("IMPOSSIBLE")
    else:
        sys.stdout.write(str(result_counter))



if __name__ == '__main__':
    actual_code()

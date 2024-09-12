import sys
from collections import deque

def BFS(grid, start_coord, end_coord, H, W, F):
    visited = [[False for _ in range(W)] for _ in range(H)]

    queue = deque([(start_coord[0], start_coord[1])])

    visited[start_coord[0]][start_coord[1]] = True

    while F >= 0:

        for _ in range(len(queue)):
            x, y = queue.popleft()

            if (x, y) == end_coord:
                return True

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny]:
                    move_cost = grid[nx][ny] - grid[x][y]

                    if move_cost <= F:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

        F -= 1


    return False

def Solution():
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        H, W, O, F, X_s, Y_s, X_e, Y_e = map(int, sys.stdin.readline().strip().split())

        start_coord = (X_s - 1, Y_s - 1)
        end_coord = (X_e - 1, Y_e - 1)

        grid = [[0 for _ in range(W)] for _ in range(H)]

        for i in range(O):
            X, Y, L = map(int, sys.stdin.readline().strip().split())
            grid[X - 1][Y - 1] = L

        result = BFS(grid, start_coord, end_coord, H, W, F)

        if result:
            print("잘했어!!")
        else:
            print("인성 문제있어??")

if __name__ == "__main__":
    Solution()

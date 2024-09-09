import sys
from collections import deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def BFS(tomato_box, M, N, start_points, total_tomato_count):
    visited = [[False for _ in range(M)] for _ in range(N)]
    queue = deque(start_points)

    # 시작지점이 있으면 무조건 하루가 걸린다고 계산하므로 (최초 토마토가 익는데 1일이 걸린다고) 보정값으로 -1 시작
    day_counter = -1
    while queue:
        for _ in range(len(queue)):
            t_row, t_col = queue.popleft()

            tomato_box[t_row][t_col] = 1

            if (t_row == -1 and t_col == -1):
                continue

            for dx, dy in DIRECTIONS:
                nx = t_row + dx
                ny = t_col + dy

                if 0 <= nx < N and 0 <= ny < M and tomato_box[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    tomato_box[nx][ny] = 1
                    total_tomato_count -= 1

        day_counter += 1

    if total_tomato_count <= 0:
        return day_counter
    else:
        return -1

def Solution():
    M, N = map(int, sys.stdin.readline().strip().split())

    tomato_box = []
    start_points = []
    total_tomato_count = M * N
    for row in range(N):
        tomato_box.append(list(map(int, sys.stdin.readline().strip().split())))
        for col in range(M):
            if tomato_box[row][col] == 1:
                start_points.append((row, col))
                total_tomato_count -= 1
            if (tomato_box[row][col] == -1):
                total_tomato_count -= 1

    result = BFS(tomato_box, M, N, start_points, total_tomato_count)

    print(result)

if __name__ == "__main__":
    Solution()

import copy
import sys
from collections import deque
from itertools import combinations


def BFS(grid, N, M, start):
    visited = [[False] * M for _ in range(N)]

    queue = deque(start)

    while queue:
        for _ in range(len(queue)):
            virus = queue.popleft()

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = dx + virus[0]
                ny = dy + virus[1]

                if 0 <= nx < N and 0 <= ny < M:
                    if not visited[nx][ny]:
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 2
                            queue.append((nx, ny))

                        visited[nx][ny] = True

def Solution():
    N, M = map(int, sys.stdin.readline().strip().split())

    virus_start_point = []
    possible_wall_pos = []
    grid = []
    for r in range(N):
        row = list(map(int, sys.stdin.readline().strip().split()))
        grid.append(row)

    for r in range(N):
        for c in range(M):
            if grid[r][c] == 2:
                virus_start_point.append((r, c))
            if grid[r][c] == 0:
                possible_wall_pos.append((r, c))

    maximum_safe_space_count = 0
    for possible_comb in combinations(possible_wall_pos, 3):
        test_grid = copy.deepcopy(grid)
        for wall_pos in possible_comb:
            test_grid[wall_pos[0]][wall_pos[1]] = 1

        BFS(test_grid, N, M, virus_start_point)

        safe_space_counter = 0
        for row in test_grid:
            safe_space_counter += row.count(0)

        maximum_safe_space_count = max(maximum_safe_space_count, safe_space_counter)

    sys.stdout.write(str(maximum_safe_space_count))

if __name__ == "__main__":
    Solution()
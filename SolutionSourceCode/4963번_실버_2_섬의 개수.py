import sys
from collections import deque

def actual_code():
    while True:
        map_size_string = sys.stdin.readline().strip().split()
        map_width = int(map_size_string[0])
        map_height = int(map_size_string[1])

        if (map_width == 0 and map_height == 0):
            break

        map_grid = []

        for i in range(map_height):
            map_grid.append(list(map(int, sys.stdin.readline().strip().split())))

        count = 0

        neighbor_direction = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

        for i in range(map_height):
            for j in range(map_width):
                if (map_grid[i][j] == 1):
                    count += 1

                    queue = deque([(i, j)])

                    map_grid[i][j] = -1

                    while queue:
                        current = queue.popleft()
                        x, y = current
                        for dx, dy in neighbor_direction:
                            nx, ny = x + dx, y + dy

                            if (0 <= nx < map_height and 0 <= ny < map_width and map_grid[nx][ny] == 1):
                                queue.append((nx, ny))
                                map_grid[nx][ny] = -1

        sys.stdout.write(str(count) + "\n")


if __name__ == '__main__':
    actual_code()

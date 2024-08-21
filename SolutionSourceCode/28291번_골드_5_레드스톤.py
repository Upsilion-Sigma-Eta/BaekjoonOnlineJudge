import sys
from collections import deque

const_redstone_block = 2
const_redstone_dust = 1
const_redstone_lamp = 3

def bfs(graph, start, W, H):
    visited_distance = []
    queue = deque([start])

    for _ in range(H):
        visited_distance.append([float('inf')] * W)

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    visited_distance[start[1]][start[0]] = 0

    while queue:
        current = queue.popleft()

        if graph[current[1]][current[0]] == 2 and visited_distance[current[1]][current[0]] <= 15:
            return True
        
        for direction in directions:
            nx = current[1] + direction[0]
            ny = current[0] + direction[1]

            if (0 <= nx < H and 0 <= ny < W) and visited_distance[nx][ny] == float('inf') and (graph[nx][ny] == 1 or graph[nx][ny] == 2):
                visited_distance[nx][ny] = visited_distance[current[1]][current[0]] + 1

                queue.append((ny, nx))
            elif (0 <= nx < H and 0 <= ny < W) and graph[nx][ny] != 3:
                visited_distance[nx][ny] = float('-inf')

    return False

            
    

def Solution():
    W, H = map(int, sys.stdin.readline().strip().split())
    N = int(sys.stdin.readline().strip())

    map_grid = []
    redstone_lamp = []

    for _ in range(H):
        map_grid.append([0] * W)

    for _ in range(N):
        block_type, coordinate_x, coordinate_y = sys.stdin.readline().strip().split()

        coordinate = (int(coordinate_x), int(coordinate_y))

        if (block_type == "redstone_block"):
            map_grid[coordinate[1]][coordinate[0]] = const_redstone_block
        elif (block_type == "redstone_dust"):
            map_grid[coordinate[1]][coordinate[0]] = const_redstone_dust
        elif (block_type == "redstone_lamp"):
            map_grid[coordinate[1]][coordinate[0]] = const_redstone_lamp
            redstone_lamp.append(coordinate)

    for lamp in redstone_lamp:
        if not bfs(map_grid, lamp, W, H):
            sys.stdout.write("failed" + "\n")
            return
    
    sys.stdout.write("success" + "\n")


if __name__ == "__main__":
    Solution()
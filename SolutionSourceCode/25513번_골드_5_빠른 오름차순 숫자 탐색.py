import sys

from collections import deque

def bfs(graph, start, counter, target):
    rows, cols = len(graph), len(graph[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()

            if graph[node[0]][node[1]] == target:
                if target == 6:
                    # 정점에서 정점 사이로 이동하는 것이 5번 나타나는데 중복으로 나타나는 것 처리
                    counter -= 5
                    return counter
                target += 1
                queue = deque([node])
                visited = [[False] * cols for _ in range(rows)]
                visited[node[0]][node[1]] = True
                break

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = node[0] + dx, node[1] + dy

                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and graph[nx][ny] != -1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

        counter += 1

    return -1

def Solution():
    graph = []

    for _ in range(5):
        graph.append(list(map(int, sys.stdin.readline().strip().split())))

    r, c = map(int, sys.stdin.readline().strip().split())

    result = bfs(graph, (r, c), 0, 1)

    sys.stdout.write(str(result) + "\n")

if __name__ == "__main__":
    Solution()
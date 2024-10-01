import sys
from collections import deque

def BFS(N, M, tree, start, end):
    visited = [False] * (N + 1)
    distnace = [0] * (N + 1)

    queue = deque([start])
    visited[start] = True

    while queue:
        current_node = queue.popleft()

        if current_node == end:
            return distnace[current_node]

        for neighbor, dist in tree[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distnace[neighbor] = distnace[current_node] + dist
                queue.append(neighbor)

def Solution():
    N, M = map(int, sys.stdin.readline().strip().split())

    tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        v1, v2, dist = map(int, sys.stdin.readline().strip().split())

        tree[v1].append((v2, dist))
        tree[v2].append((v1, dist))

    for i in range(M):
        start, end = map(int, sys.stdin.readline().strip().split())
        dist = BFS(N, M, tree, start, end)

        sys.stdout.write(str(dist) + "\n")

if __name__ == "__main__":
    Solution()
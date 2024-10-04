import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 4)

def Solution():
    def DFS(graph, visited, vertex, recursive_stack):
        visited.add(vertex)
        recursive_stack.add(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                if DFS(graph, visited, neighbour, recursive_stack):
                    return True
            elif neighbour in recursive_stack:
                return True

        recursive_stack.remove(vertex)
        return False

    N, M = map(int, sys.stdin.readline().strip().split())

    grid = []
    for _ in range(N):
        grid.append(sys.stdin.readline().strip())

    # 2차원 격자판을 인접 그래프로 표현
    graph = defaultdict(list)
    for row in range(N):
        for col in range(M):
            if grid[row][col] == "D" and row + 1 < N:
                graph[(row, col)].append((row + 1, col))
            elif grid[row][col] == "L" and col - 1 >= 0:
                graph[(row, col)].append((row, col - 1))
            elif grid[row][col] == "R" and col + 1 < M:
                graph[(row, col)].append((row, col + 1))
            elif grid[row][col] == "U" and row - 1 >= 0:
                graph[(row, col)].append((row - 1, col))

    visited = set()
    cycle_count = 0

    # 모든 노드에 대해 DFS를 수행하여 사이클 감지
    for row in range(N):
        for col in range(M):
            if (row, col) not in visited:
                recursive_stack = set()
                if DFS(graph, visited, (row, col), recursive_stack):
                    cycle_count += 1

    # 최종 사이클 개수 출력
    print(cycle_count)

if __name__ == "__main__":
    Solution()

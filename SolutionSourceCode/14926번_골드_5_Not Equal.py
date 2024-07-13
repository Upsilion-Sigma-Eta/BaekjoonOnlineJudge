import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

def remove_edge(graph, u, v):
    graph[u].remove(v)
    graph[v].remove(u)

def dfs(graph, path, v):
    while graph[v]:
        u = sorted(graph[v])[0]  # 사전순으로 가장 작은 정점을 선택
        remove_edge(graph, v, u)
        dfs(graph, path, u)
    path.append(v)

def hierholzer_algorithm(graph, start_vertex):
    path = []
    dfs(graph, path, start_vertex)
    return path[::-1]

def actual_code():
    N = int(sys.stdin.readline().strip())

    graph = defaultdict(list)

    for i in range(N):
        for j in range(N):
            if (j == i):
                continue
            graph[i].append(j)

    start_vertex = 0
    path = hierholzer_algorithm(graph, start_vertex)

    for i in path:
        sys.stdout.write('a' + str(i + 1) + ' ')


if __name__ == '__main__':
    actual_code()

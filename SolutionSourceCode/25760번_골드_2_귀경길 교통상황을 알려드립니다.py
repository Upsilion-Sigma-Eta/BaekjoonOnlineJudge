import sys
from collections import deque

def bfs(graph, traffic_info):
    distances = [-1] * (len(traffic_info) + 1)
    distances[1] = 0
    queue = deque([1])

    while queue:
        current = queue.popleft()
        for neighbor in graph.get(current, []):
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    arrival_time = []
    for i in range(1, len(traffic_info) + 1):
        if traffic_info[i] == 1:
            arrival_time.append(distances[i])

    arrival_time.sort()

    max_time = 0
    current_time = 0
    for time in arrival_time:
        current_time = max(current_time, time) + 1
        max_time = max(max_time, current_time)

    return max_time

def actual_code():
    N = int(sys.stdin.readline().strip())

    graph = {}
    for _ in range(N - 1):
        u, v = map(int, sys.stdin.readline().strip().split())
        if (u in graph.keys()):
            graph[u].append(v)
        else:
            graph[u] = [v]
        if (v in graph.keys()):
            graph[v].append(u)
        else:
            graph[v] = [u]

    traffic_info = {}
    index = 1
    for i in map(int, sys.stdin.readline().strip().split()):
        traffic_info[index] = i
        index += 1

    visited = {}
    counter = bfs(graph, traffic_info)

    sys.stdout.write(str(counter) + '\n')

if __name__ == '__main__':
    actual_code()
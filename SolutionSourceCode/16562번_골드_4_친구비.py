import sys
from collections import deque, defaultdict

def BFS(N, M, graph, k, start, visited):
    queue = deque([start])
    component = [start]
    visited[start] = True

    while queue:
        node = queue.popleft()
        for friend in graph[node]:
            if not visited[friend]:
                queue.append(friend)
                visited[friend] = True
                component.append(friend)

    return component

def separate_friend_group(N, M, graph, k):
    visited = {node: False for node in range(N)}
    components = []

    for node in graph:
        if not visited[node]:
            component = BFS(N, M, graph, k, node, visited)
            components.append(component)

    for node in range(N):
        if not visited[node]:
            components.append([node])
            visited[node] = True

    return components

def Solution():
    N, M, k = map(int, sys.stdin.readline().strip().split())

    friend_cost = list(map(int, sys.stdin.readline().strip().split()))

    graph = defaultdict(list)
    for _ in range(M):
        v1, v2 = map(int, sys.stdin.readline().strip().split())

        graph[v1 - 1].append(v2 - 1)
        graph[v2 - 1].append(v1 - 1)

    connected_set = separate_friend_group(N, M, graph, k)

    friend_cost_result = 0

    for each_set in connected_set:
        for i in range(len(each_set)):
            each_set[i] = friend_cost[each_set[i]]

    for each_set in connected_set:
        friend_cost_result += min(each_set)

    if friend_cost_result <= k:
        sys.stdout.write(str(friend_cost_result) + "\n")
    else:
        sys.stdout.write("Oh no\n")

if __name__ == "__main__":
    Solution()
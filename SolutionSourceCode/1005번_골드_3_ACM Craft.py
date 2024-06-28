import sys

def kahn_algorithm(graph, start):
    in_degree = {i : 0 for i in graph}

    for i in graph:
        for j in graph[i]:
            if (j in in_degree):
                in_degree[j] += 1

    in_degree_zero_queue = [start]

    ordered_stack = []

    while in_degree_zero_queue:
        node = in_degree_zero_queue.pop(0)
        ordered_stack.append(node)

        for i in graph[node]:
            if (i in in_degree):
                in_degree[i] -= 1
                if (in_degree[i] == 0):
                    in_degree_zero_queue.append(i)

    return ordered_stack

def find_start_point_candidate(graph):
    in_degree = {i : 0 for i in graph}

    for i in graph:
        for j in graph[i]:
            if (j in in_degree):
                in_degree[j] += 1

    in_degree_zero_queue = []
    for i in in_degree:
        if in_degree[i] == 0:
            in_degree_zero_queue.append(i)

    return in_degree_zero_queue

def actual_code():
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N, K = map(int, sys.stdin.readline().strip().split())

        D = list(map(int, sys.stdin.readline().strip().split()))

        result = 0

        graph = {}
        for i in range(K):
            key, value = map(int, sys.stdin.readline().strip().split())
            if (key in graph.keys()):
                graph[key].append(value)
            else:
                graph[key] = [value]

        if (N not in graph.keys()):
            graph[N] = []

        W = int(sys.stdin.readline().strip())

        start_points = find_start_point_candidate(graph)

        for start in start_points:
            ordered_stack = kahn_algorithm(graph, start)

            if (ordered_stack == []):
                continue

            critical_path = {node: float('-inf') for node in graph}
            critical_path[ordered_stack[0]] = D[ordered_stack[0] - 1]

            for index in ordered_stack:
                for i in graph[index]:
                    if (i in critical_path):
                        critical_path[i] = max(critical_path[i], critical_path[index] + D[i - 1])
                    else:
                        critical_path[i] = critical_path[index] + D[i - 1]

            # Processsing Building Critical Path that has no connection with other building
            for key in critical_path.keys():
                if (critical_path[key] == float('-inf')):
                    critical_path[key] = D[key - 1]

            result = max(result, critical_path[W])

        sys.stdout.write(str(result) + "\n")


if __name__ == '__main__':
    actual_code()
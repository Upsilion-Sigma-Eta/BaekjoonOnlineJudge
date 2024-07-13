import sys


def floyd_warshall_algorithm(graph):
    number_of_vertices = len(graph)

    distance = [[float('inf')] * number_of_vertices for _ in range(number_of_vertices)]

    for i in range(number_of_vertices):
        distance[i][i] = 0

    for u in range(number_of_vertices):
        for v in range(number_of_vertices):
            if graph[u][v] != float('inf'):
                distance[u][v] = graph[u][v]

    for k in range(number_of_vertices):
        for i in range(number_of_vertices):
            for j in range(number_of_vertices):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]


    return distance

def actual_code():
    N = int(sys.stdin.readline().strip())

    friend_graph = [[float('inf')] * N for _ in range(N)]
    while True:
        a, b = map(int, sys.stdin.readline().strip().split())
        if a == -1 and b == -1:
            break
        friend_graph[a - 1][b - 1] = 1
        friend_graph[b - 1][a - 1] = 1

    result_distance_graph = floyd_warshall_algorithm(friend_graph)

    individual_max_value = []
    for i in range(N):
        individual_max_value.append(max(result_distance_graph[i]))

    total_min_value = min(individual_max_value)

    candidate = []

    for i in range(N):
        if individual_max_value[i] == total_min_value:
            candidate.append(i + 1)

    sys.stdout.write(str(total_min_value) + ' ' + str(len(candidate)) + '\n')
    for i in range(len(candidate)):
        sys.stdout.write(str(candidate[i]) + ' ')

if __name__ == '__main__':
    actual_code()

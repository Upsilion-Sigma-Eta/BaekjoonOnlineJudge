import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def is_same_group(parent, x, y):
    return find(parent, x) == find(parent, y)

def Solution():
    while True:
        number_of_student, number_of_groups = map(int, sys.stdin.readline().strip().split())

        if (number_of_student == 0 and number_of_groups == 0):
            break

        groups = []

        for _ in range(number_of_groups):
            groups.append(list(map(int, sys.stdin.readline().strip().split()))[1:])

        parent = [i for i in range(number_of_student)]
        rank = [1] * number_of_student

        for group in groups:
            for i in range(len(group) - 1):
                union(parent, rank, group[i], group[i + 1])

        infected_suspect_count = 0

        for i in range(number_of_student):
            if is_same_group(parent, 0, i):
                infected_suspect_count += 1

        sys.stdout.write(f"{infected_suspect_count}\n")

if __name__ == "__main__":
    Solution()

import sys

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, e):
        if self.parent[e] != e:
            self.parent[e] = self.find(self.parent[e])
        return self.parent[e]

    def union(self, e1, e2):
        root_e1 = self.find(e1)
        root_e2 = self.find(e2)

        if (root_e1 != root_e2):
            if (self.rank[root_e1] > self.rank[root_e2]):
                self.parent[root_e2] = root_e1
            elif self.rank[root_e1] < self.rank[root_e2]:
                self.parent[root_e1] = root_e2
            else:
                self.parent[root_e2] = root_e1
                self.rank[root_e1] += 1

            return True
        return False

def MST_Kruskal(N, M, edge_adjacent_list):
    minimum_cost = 0
    MST = set()

    sorted_edges = sorted(edge_adjacent_list, key=lambda x: x[0][2])

    union_find = UnionFind(N)
    for i in range(M):
        edge = sorted_edges[i]

        u = edge[0][0]
        v = edge[0][1]
        w = edge[0][2]

        if union_find.union(u, v):
            union_find.union(u, v)
            MST.add((u, v))
            minimum_cost += w

    # 0 기반 인덱스이므로 MST는 N - 1개의 길이를 가짐
    if (len(MST) != N - 1):
        return -1
    else:
        return minimum_cost

def Solution():
    N, M = map(int, sys.stdin.readline().strip().split())

    adjacent_list = [[] for _ in range(M)]
    total_cost = 0
    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().strip().split())

        # 0 기반 인덱스로 변경
        adjacent_list[_].append((a - 1, b - 1, c))

        total_cost += c

    result = MST_Kruskal(N, M, adjacent_list)

    if (result == -1):
        print(-1)
    else:
        print(total_cost - result)


if __name__ == "__main__":
    Solution()

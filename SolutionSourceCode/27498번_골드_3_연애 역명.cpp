#include <iostream>
#include <algorithm>
#include <vector>

struct Edge {
    int v1, v2, weight;

    Edge(int a, int b, int c) : v1(a), v2(b), weight(c) {}
};

int find_parent(std::vector<int>& parent, int vertex) {
    if (parent[vertex] != vertex) {
        parent[vertex] = find_parent(parent, parent[vertex]); // 경로 압축
    }
    return parent[vertex];
}

void union_sets(std::vector<int>& parent, std::vector<int>& rank, int vertex_1, int vertex_2) {
    int root1 = find_parent(parent, vertex_1);
    int root2 = find_parent(parent, vertex_2);

    if (root1 != root2) {
        if (rank[root1] < rank[root2]) {
            parent[root1] = root2;
        } else {
            parent[root2] = root1;
            if (rank[root1] == rank[root2]) {
                rank[root1]++;
            }
        }
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int N, M;
    std::cin >> N >> M;

    std::vector<int> parent(N);
    std::vector<int> rank(N, 0);
    for (int i = 0; i < N; ++i) {
        parent[i] = i;
    }

    int total_unestablished_weight = 0;
    std::vector<Edge> edges;
    for (int i = 0; i < M; ++i) {
        int a, b, c, d;
        std::cin >> a >> b >> c >> d;

        if (d == 1) {
            union_sets(parent, rank, a - 1, b - 1);
        } else {
            edges.push_back(Edge(a - 1, b - 1, c));
            total_unestablished_weight += c;
        }
    }

    std::sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.weight > b.weight;
    });

    int total_included_weight = 0;
    for (const Edge& edge : edges) {
        if (find_parent(parent, edge.v1) != find_parent(parent, edge.v2)) {
            union_sets(parent, rank, edge.v1, edge.v2);
            total_included_weight += edge.weight;
        }
    }

    int result = total_unestablished_weight - total_included_weight;
    std::cout << result << "\n";

    return 0;
}

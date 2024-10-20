#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
#include <stdint.h>
#include <vector>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int n, k;

    std::cin >> n >> k;

    std::vector<std::vector<int>> dist = std::vector<std::vector<int>>(n, std::vector<int>(n, INT32_MAX));

    for (int i = 0; i < n; ++i) {
        dist[i][i] = 0;
    }

    for (int i = 0; i < k; ++i) {
        int v, u;
        std::cin >> v >> u;
        dist[v - 1][u - 1] = 1;
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            for (int l = 0; l < n; ++l) {
                if (dist[j][i] != INT32_MAX && dist[i][l] != INT32_MAX) {
                    dist[j][l] = std::min(dist[j][l], dist[j][i] + dist[i][l]);
                }
            }
        }
    }

    int s;
    std::cin >> s;

    for (int i = 0; i < s; ++i) {
        int u, v;
        std::cin >> v >> u;

        if (dist[v - 1][u - 1] != INT32_MAX) {
            std::cout << "-1\n";
        } else if (dist[u - 1][v - 1] != INT32_MAX) {
            std::cout << "1\n";
        } else {
            std::cout << "0\n";
        }
    }

    return 0;
}

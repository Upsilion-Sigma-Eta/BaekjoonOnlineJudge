#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdint>
#include <string>
#include <vector>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int N = 0;
    std::cin >> N;

    std::vector<std::pair<int, int>> work = std::vector<std::pair<int, int>>();

    for (int i = 0; i < N; ++i) {
        work.push_back(std::pair<int, int>());
        std::cin >> work[i].first;
        std::cin >> work[i].second;
    }

    std::stable_sort(work.begin(), work.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
        return a.second > b.second;
    });

    int current_time = INT32_MAX;

    for (int i = 0; i < N; ++i) {
        current_time = std::min(current_time, work[i].second);
        current_time -= work[i].first;

        if (current_time < 0) {
            std::cout << -1;

            return 0;
        }
    }

    std::cout << current_time;


    return 0;
}

#include <iostream>
#include <unordered_map>
#include <vector>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int n;
    std::cin >> n;

    std::vector<int> A = std::vector<int>(n);
    std::vector<int> B = std::vector<int>(n);
    std::vector<int> C = std::vector<int>(n);
    std::vector<int> D = std::vector<int>(n);

    for (int i = 0; i < n; ++i) {
        std::cin >> A[i] >> B[i] >> C[i] >> D[i];
    }

    std::unordered_map<int, int> sum_ab;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            sum_ab[A[i] + B[j]]++;
        }
    }

    long long int counter = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (sum_ab.find(-(C[i] + D[j])) != sum_ab.end()) {
                counter += sum_ab[-(C[i] + D[j])];
            }
        }
    }

    std::cout << counter << "\n";

    return 0;
}

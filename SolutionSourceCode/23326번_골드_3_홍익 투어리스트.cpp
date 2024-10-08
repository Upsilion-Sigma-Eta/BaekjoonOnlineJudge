#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdint>
#include <set>
#include <string>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int N = 0;
    int Q = 0;

    std::cin >> N;
    std::cin >> Q;

    std::set<int> A;

    for (int i = 0; i < N; ++i) {
        int value = 0;
        std::cin >> value;

        if (value == 1) {
            A.insert(i);
        }
    }

    // 1-based 인덱스임에 주의, 0-based 인덱스로 변환 필요함
    int current_pos = 0;
    for (int i = 0; i < Q; ++i) {
        int query_type = 0;
        std::cin >> query_type;

        if (query_type == 1) {
            int query_value = 0;
            std::cin >> query_value;

            // 0-based Index로 전환
            query_value--;

            if (A.find(query_value) != A.end()) {
                A.erase(query_value);
            } else {
                A.insert(query_value);
            }
        }
        else if (query_type == 2) {
            int query_value = 0;
            std::cin >> query_value;

            current_pos += query_value;
            current_pos %= N;
        }
        else if (query_type == 3) {
            if (A.empty()) {
                std::cout << -1 << "\n";
            } else {
                std::set<int>::iterator it = A.lower_bound(current_pos);

                if (it != A.end()) {
                    std::cout << *it - current_pos << "\n";
                } else {
                    std::cout << (N - current_pos) + *A.begin() << "\n";
                }
            }
        }
    }

    return 0;
}

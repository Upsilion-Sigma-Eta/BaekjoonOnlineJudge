#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    long long int N;
    std::cin >> N;

    long long int max_square_count = 0;
    long long int start_point = sqrt(N);

    for (long long int n = start_point - 2; n <= start_point + 2; ++n) {
        if (n <= 0) {
            continue;
        }
        for (long long int m = n; m <= n + 1; ++m) {
            long long int total_point = n * m;
            if (total_point > N) {
                continue;
            }

            long long int extra_point = N - total_point;

            long long int max_square_count_possibility = 0;
            long long int minimum_side = std::min(n, m);

            for (long long int i = 1; i < minimum_side; ++i) {
                max_square_count_possibility += (n - i) * (m - i);
            }

            if (extra_point < n || extra_point < m) {
                for (long long int i = extra_point - 1; i > 0; --i) {
                    max_square_count_possibility += i;
                }
            }

            if (max_square_count_possibility > max_square_count) {
                max_square_count = max_square_count_possibility;
            }
        }
    }

    std::cout << max_square_count << std::endl;

    return 0;
}

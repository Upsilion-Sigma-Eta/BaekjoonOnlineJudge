#include <iostream>
#include <cmath>
#include <cstdint>

int main() {
    // 입출력 Thread-Safe 기능을 해제, 다중 스레드 환경이나 실무에서는 사용 금지
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int T;
    std::cin >> T;

    for (int _ = 0; _ < T; ++_) {
        double yes_vote_ratio;

        std::cin >> yes_vote_ratio;

        double sample_low_ratio = yes_vote_ratio - 0.0005;
        double sample_high_ratio = yes_vote_ratio + 0.0005;

        double sample_number = ceil(100 / sample_high_ratio);

        while (true) {
            long long int lower_bound = ceil(sample_low_ratio * sample_number / 100);
            long long int upper_bound = ceil(sample_high_ratio * sample_number / 100);

            long long int valid_integer_count = upper_bound - lower_bound;

            if (valid_integer_count >= 1) {
                std::cout << sample_number << "\n";
                break;
            }

            ++sample_number;
        }

    }

    return 0;
}
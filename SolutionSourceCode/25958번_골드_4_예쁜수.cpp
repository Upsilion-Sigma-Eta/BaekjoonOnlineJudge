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

    int M = 0;
    int K = 0;

    std::cin >> M >> K;

    // 예쁜 수 계산
    std::vector<int> pretty_number = std::vector<int>();

    for (int num = 1; num < M + 1; ++num) {
        int original_num = num;
        int calc_num = num;
        int digit_sum = 0;
        while (calc_num > 0) {
            digit_sum += calc_num % 10;
            calc_num /= 10;
            calc_num = static_cast<int>(std::floor(calc_num));
        }

        if (original_num % digit_sum == 0) {
            pretty_number.push_back(original_num);
        }
    }

    // 다이나믹 프로그래밍으로 접근
    // M = A + B로 분해될 때, A와 B 또한 같은 방법으로 분해될 수 있음.
    std::vector<int> dp = std::vector<int>(M + 1);
    dp[0] = 1;

    for (int num : pretty_number) {
        for (int  i = num; i < M + 1; ++i) {
            dp[i] = (dp[i] + dp[i - num]) % K;
        }
    }

    std::cout << dp.back();

    return 0;
}

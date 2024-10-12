#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <climits>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int T;
    std::cin >> T;

    for (int test_case = 0; test_case < T; ++test_case) {
        std::string password;
        std::cin >> password;

        int N;
        std::cin >> N;

        std::vector<std::string> pass_key(N);
        for (int i = 0; i < N; ++i) {
            std::cin >> pass_key[i];
        }

        int length = password.length();
        std::vector<int> dp(length + 1, INT_MAX);
        dp[0] = 0;

        for (int i = 0; i < length; ++i) {
            if (dp[i] == INT_MAX) {
                continue;
            }
            for (const std::string& pass : pass_key) {
                int pass_len = pass.length();

                if (i + pass_len > length) {
                    continue;
                }

                std::string pass_sliced = password.substr(i, pass_len);
                std::string pass_sliced_sorted = pass_sliced;
                std::string pass_sorted = pass;

                std::sort(pass_sliced_sorted.begin(), pass_sliced_sorted.end());
                std::sort(pass_sorted.begin(), pass_sorted.end());

                if (pass_sorted != pass_sliced_sorted) {
                    continue;
                }

                int match_counter = 0;
                for (int k = 0; k < pass_len; ++k) {
                    if (pass[k] == pass_sliced[k]) {
                        ++match_counter;
                    }
                }

                int cost = pass_len - match_counter;

                if (dp[i + pass_len] > dp[i] + cost) {
                    dp[i + pass_len] = dp[i] + cost;
                }
            }
        }

        if (dp[length] == INT_MAX) {
            std::cout << -1 << "\n";
        } else {
            std::cout << dp[length] << "\n";
        }
    }

    return 0;
}

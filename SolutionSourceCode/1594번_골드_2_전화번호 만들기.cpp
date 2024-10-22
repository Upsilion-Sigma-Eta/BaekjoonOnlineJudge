#include <iostream>
#include <set>
#include <vector>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    std::string youngshik_phone_number = std::string();
    std::cin >> youngshik_phone_number;

    std::vector<std::pair<int, std::string>> dp = std::vector<std::pair<int, std::string>>(youngshik_phone_number.length() + 1, std::pair<int, std::string>(-1, std::string()));
    dp[youngshik_phone_number.length()] = std::pair(0, std::string());

    for (int i = youngshik_phone_number.length() - 1; i >= 0; --i) {
        for (int j = 2; j <= 3; ++j) {
            if (i + j <= youngshik_phone_number.length()) {
                std::string group = youngshik_phone_number.substr(i, j);

                std::set<int> unique_digits = std::set<int>(group.begin(), group.end());

                int quality = 0;
                if (unique_digits.size() == 1) {
                    quality = 2;
                } else if (j == 3 && unique_digits.size() == 2) {
                    quality = 1;
                } else {
                    quality = 0;
                }

                int rest_quality = 0;
                std::string rest_phone_number = std::string();
                if (dp[i + j].first >= 0) {
                    rest_quality = dp[i + j].first;
                    rest_phone_number = dp[i + j].second;
                }
                else {
                    continue;
                }

                int new_total_quality = quality + rest_quality;

                std::string new_phone_number = std::string();
                if (rest_phone_number == "") {
                    new_phone_number = group;
                } else {
                    new_phone_number = group + "-" + rest_phone_number;
                }

                if (new_total_quality > dp[i].first) {
                    dp[i] = std::pair(new_total_quality, new_phone_number);
                } else if (new_total_quality == dp[i].first) {
                    if (new_phone_number < dp[i].second || dp[i].second == "") {
                        dp[i] = std::pair<int, std::string>(new_total_quality, new_phone_number);
                    }
                }
            }
        }
    }

    std::cout << dp[0].second << std::endl;

    return 0;
}

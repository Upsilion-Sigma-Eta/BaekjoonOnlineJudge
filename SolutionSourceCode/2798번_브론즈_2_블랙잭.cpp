#include <iostream>
#include <vector>

int main(void) {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int N, M;
    std::cin >> N >> M;

    std::vector<int> cardNumber = std::vector<int>(N);

    for (int i = 0; i < N; ++i) {
        std::cin >> cardNumber[i];
    }

    int max_sum = 0;

    for (int i = 0; i < N - 2; ++i) {
        for (int j = i + 1; j < N - 1; ++j) {
            for (int k = j + 1; k < N; ++k) {
                int sum = cardNumber[i] + cardNumber[j] + cardNumber[k];

                if (sum > max_sum && sum <= M) {
                    max_sum = sum;
                }
            }
        }
    }

    std::cout << max_sum << std::endl;

    return 0;
}

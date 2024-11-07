#include <iostream>
#include <valarray>
#include <vector>

int main(void) {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int N;
    std::cin >> N;

    std::vector<double> scores = std::vector<double>(N);

    for (int i = 0; i < N; ++i) {
        std::cin >> scores[i];
    }

    double max = *std::max_element(scores.begin(), scores.end());
    double score_new_sum = 0;

    for (int i = 0; i < N; ++i) {
        score_new_sum += scores[i] / max * 100;
    }

    score_new_sum /= N;

    std::cout << score_new_sum;

    return 0;
}

#include <iostream>
#include <valarray>
#include <vector>

int main(void) {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    unsigned long long int L;
    std::cin >> L;

    std::string str = std::string();
    std::cin >> str;

    unsigned long long int r = 31;
    unsigned long long int M = 1234567891;

    unsigned long long int H = 0;
    unsigned long long int current_multiplier = 1;

    for (int i = 0; i < L; ++i) {
        unsigned long long int digit = ((str[i] - 'a' + 1) * current_multiplier);

        H += digit;
        H %= M;
        current_multiplier *= r;
        current_multiplier %= M;
    }

    std::cout << (H % M) << std::endl;

    return 0;
}

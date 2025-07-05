#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <cmath>
#include <climits>

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    const long long NUM = std::pow(10, 9);
    int T;
    std::cin >> T;

    while (T--)
    {
        long long N, S;
        std::cin >> N >> S;
        long long DEN = 2 * N;

        bool ok = false;
        for (long long a = 0; a <= N; ++a)
        {
            long long remaining = S - a;
            if (remaining < 0)
                break;

            long long low = (remaining * DEN + NUM - 1) / NUM;
            long long high = ((remaining + 1) * DEN - 1) / NUM;

            long long t_min = 2 * a;
            long long t_max = 2 * N;

            long long t = std::max(low, t_min);

            if (t <= high && t <= t_max)
            {
                std::cout << t << ' ' << a << '\n';
                ok = true;
                break;
            }
        }
        if (!ok)
            std::cout << -1 << '\n';
    }

    return 0;
}
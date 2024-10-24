#include <bits/stdc++.h>


// https://restudycafe.tistory.com/587 풀이 참조
int main(void) {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    long long int N;
    std::cin >> N;

    std::vector<long long int> v(30001), u(30001);

    long long int ans = 0;
    while(N--) {
        long long int x;
        std::cin >> x;

        // 현재 수 x로 끝나는 등차수열의 개수를 ans에 더함
        ans += u[x] + v[x] * (v[x] - 1) / 2;

        // 수 x의 빈도수를 증가시킴
        v[x]++;

        // x보다 작은 수 i에 대해
        for(long long int i = 1; i < x; ++i) {
            long long int Ak = x + (x - i); // Ak = 2x - i
            if(Ak <= 30000) {
                u[Ak] += v[i];
            }
        }

        // x보다 큰 수 i에 대해
        for(long long int i = 30000; i > x; --i) {
            long long int Ak = x - (i - x); // Ak = 2x - i
            if(Ak >= 1) {
                u[Ak] += v[i];
            }
        }
    }

    std::cout << ans << "\n";

    return 0;
}

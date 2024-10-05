#include <iostream>
#include <cmath>
#include <cstdint>
#include <algorithm>

int main() {
    // 입출력 Thread-Safe 기능을 해제, 다중 스레드 환경이나 실무에서는 사용 금지
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int N = 0;
    std::cin >> N;
    std::pair<int, int> arr[N];
    std::pair<int, int> arr_sorted[N];
    int arr_sorted_index[N] = { 0, };

    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i].first;
        arr[i].second = i;

        arr_sorted[i].first = arr[i].first;
        arr_sorted[i].second = arr[i].second;
    }

    std::stable_sort(arr_sorted, arr_sorted + N, [](std::pair<int, int> a, std::pair<int, int> b) {
        return a.first < b.first;
    });

    int cutting_required_counter = 0;
    for (int i = 0; i < N - 1; ++i) {
        if (abs(arr_sorted[i].second - arr_sorted[i + 1].second) != 1) {
            cutting_required_counter++;
        }
    }

    std::cout << cutting_required_counter;

    return 0;
}

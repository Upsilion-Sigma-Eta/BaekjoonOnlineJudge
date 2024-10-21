#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int N, M;
    std::cin >> N >> M;
    std::vector<int> A(N);
    for(int i = 0; i < N; ++i) {
        std::cin >> A[i];
    }

    std::vector<std::pair<long long, int>> events;
    long long max_E_i_plus1 = 0;
    for(int i = 0; i < M; ++i) {
        long long S_i, E_i;
        std::cin >> S_i >> E_i;
        events.push_back({S_i, +1});
        events.push_back({E_i + 1, -1});
        if (E_i + 1 > max_E_i_plus1) {
            max_E_i_plus1 = E_i + 1;
        }
    }

    std::sort(events.begin(), events.end());

    std::vector<int> A_asc = A;
    std::vector<int> A_desc = A;
    std::sort(A_asc.begin(), A_asc.end());
    std::sort(A_desc.rbegin(), A_desc.rend());

    std::vector<long long> pre_sum_asc(N + 1, 0);
    std::vector<long long> pre_sum_desc(N + 1, 0);
    for(int i = 0; i < N; ++i) {
        pre_sum_asc[i + 1] = pre_sum_asc[i] + A_asc[i];
        pre_sum_desc[i + 1] = pre_sum_desc[i] + A_desc[i];
    }

    long long current_num_customers = 0;
    long long total_revenue_min = 0;
    long long total_revenue_max = 0;
    size_t idx = 0;
    while(idx < events.size()) {
        long long day = events[idx].first;
        int delta = 0;
        while(idx < events.size() && events[idx].first == day) {
            delta += events[idx].second;
            ++idx;
        }
        current_num_customers += delta; // 고객 수를 먼저 업데이트
        long long duration = 0;
        if(idx < events.size()) {
            long long next_day = events[idx].first;
            duration = next_day - day;
        } else {
            // 마지막 이벤트 이후의 기간 처리
            duration = max_E_i_plus1 - day;
        }
        if(current_num_customers > 0 && duration > 0) {
            long long K = current_num_customers;
            if(K > N) K = N;
            long long sum_top_K = pre_sum_desc[K];
            total_revenue_max += duration * sum_top_K;
            long long sum_bottom_K = pre_sum_asc[K];
            total_revenue_min += duration * sum_bottom_K;
        }
    }

    std::cout << total_revenue_min << " " << total_revenue_max << std::endl;

    return 0;
}

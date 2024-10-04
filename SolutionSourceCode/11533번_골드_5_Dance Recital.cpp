#include <algorithm>
#include <iostream>
#include <vector>
#include <cstdint>
#include <unordered_set>

void BackTracking(std::vector<std::string>& routine, std::vector<bool>& used, int& minimumValue, int currentValue, int depth, int lastIndex, const std::vector<std::vector<int>>& overlapCache) {
    // 모든 루틴을 사용한 경우, 현재까지의 최소값 갱신
    if (depth == routine.size()) {
        minimumValue = std::min(minimumValue, currentValue);
        return;
    }

    // 가지치기: 현재까지의 교체 횟수가 이미 최소값 이상인 경우 더 이상 탐색하지 않음
    if (currentValue >= minimumValue) {
        return;
    }

    // 모든 루틴을 탐색하며 다음 루틴 선택
    for (int i = 0; i < routine.size(); ++i) {
        if (!used[i]) {
            used[i] = true;

            // 미리 루틴별로 겹치는 값들을 계산해 놓은것을 이용해서 비교에 걸리는 시간 단축
            int addedValue = 0;
            if (depth > 0) {
                addedValue = overlapCache[lastIndex][i];
            }

            BackTracking(routine, used, minimumValue, currentValue + addedValue, depth + 1, i, overlapCache);

            // 상태 복원
            used[i] = false;
        }
    }
}

int main() {
    // 입출력 Thread-Safe 기능을 해제, 다중 스레드 환경이나 실무에서는 사용 금지
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    short R = 0;
    std::cin >> R;

    std::vector<std::string> routine;

    for (int i = 0; i < R; ++i) {
        std::string routineData;
        std::cin >> routineData;
        routine.push_back(routineData);
    }

    // 미리 루틴 간의 겹치는 개수를 계산하여 캐싱
    std::vector<std::vector<int>> overlapCache(R, std::vector<int>(R, 0));
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < R; ++j) {
            if (i != j) {
                std::unordered_set<char> currentSet(routine[i].begin(), routine[i].end());
                for (char dancer : routine[j]) {
                    if (currentSet.find(dancer) != currentSet.end()) {
                        ++overlapCache[i][j];
                    }
                }
            }
        }
    }

    int minimumValue = INT32_MAX;
    std::vector<bool> used(R, false);

    BackTracking(routine, used, minimumValue, 0, 0, -1, overlapCache);

    std::cout << minimumValue << "\n";

    return 0;
}
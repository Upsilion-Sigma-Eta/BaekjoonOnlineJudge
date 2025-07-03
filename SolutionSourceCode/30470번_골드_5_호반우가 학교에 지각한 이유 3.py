import sys

def Solution():
    import sys
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline().strip())

    actions = []
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().strip().split())
        actions.append((a, b))

    # 통나무의 정보를 저장할 리스트
    # (시간 인덱스, 통나무 길이)
    logs = []
    # 각 쿼리 후의 최대 가능 길이
    log_after_query_max_length = []
    # 현재 통나무의 최대 가능 길이
    log_current_query_max_length = 0

    for idx, (action_type, power) in enumerate(actions):
        if action_type == 1:
            log_current_query_max_length = max(log_current_query_max_length, power)
            logs.append((idx, power))
            log_after_query_max_length.append(log_current_query_max_length)
        elif action_type == 2:
            log_current_query_max_length = max(log_current_query_max_length - power, 0)
            log_after_query_max_length.append(log_current_query_max_length)

    # 각 시점부터의 쿼리 이후의 최소 길이 값을 저장할 배열 생성
    INF = 10**18
    min_k_i = [0] * (N + 1)
    min_k_i[N] = INF
    for i in range(N - 1, -1, -1):
        min_k_i[i] = min(log_after_query_max_length[i], min_k_i[i + 1])

    # 각 통나무의 최종 길이를 계산하고 합산
    total_length = 0
    for time, length in logs:
        min_k = min_k_i[time]
        final_length = min(length, min_k)
        total_length += final_length

    sys.stdout.write(str(total_length))

if __name__ == "__main__":
    Solution()

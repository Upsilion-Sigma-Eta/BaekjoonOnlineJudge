import sys

# Richard Peng의 해설을 참조하였음
# Brian Dean의 코드를 참조하였음

def Solve(T, S, N, M, L, A, C, D):
    shortest_slope = [float('inf')] * (100 + 1)

    slopes = []
    for i in range(N):
        shortest_slope[C[i]] = min(shortest_slope[C[i]], D[i])

    for lev in range(1, 101):
        if lev > 1:
            shortest_slope[lev] = min(shortest_slope[lev], shortest_slope[lev - 1])

    lessons_by_time = [[] for _ in range(T + 1)]
    for i in range(S):
        if M[i] <= T:
            lessons_by_time[M[i]].append((L[i], A[i]))

    dp = [[-1] * (101) for _ in range(T + 2)]
    dp[0][1] = 0

    # DP 수행
    for time in range(T + 1):
        for skill in range(1, 101):
            if dp[time][skill] >= 0:
                current_runs = dp[time][skill]

                # 스키 타기
                slope_time = shortest_slope[skill]
                if slope_time < float('inf'):
                    new_time = time + slope_time
                    if new_time <= T:
                        if dp[new_time][skill] < current_runs + 1:
                            dp[new_time][skill] = current_runs + 1

                # 레슨 수강
                for L_i, A_i in lessons_by_time[time]:
                    new_time = time + L_i
                    if new_time <= T:
                        if dp[new_time][A_i] < current_runs:
                            dp[new_time][A_i] = current_runs

                # 아무것도 하지 않기
                if time + 1 <= T:
                    if dp[time + 1][skill] < current_runs:
                        dp[time + 1][skill] = current_runs

    return max(dp[T])

def Solution():
    T, S, N = map(int, sys.stdin.readline().strip().split())

    M = []
    L = []
    A = []
    for _ in range(S):
        M_i, L_i, A_i = map(int, sys.stdin.readline().strip().split())
        M.append(M_i)
        L.append(L_i)
        A.append(A_i)

    C = []
    D = []
    for _ in range(N):
        C_i, D_i = map(int, sys.stdin.readline().strip().split())
        C.append(C_i)
        D.append(D_i)

    max_slope_count = Solve(T, S, N, M, L, A, C, D)

    sys.stdout.write(str(max_slope_count) + "\n")

if __name__ == "__main__":
    Solution()
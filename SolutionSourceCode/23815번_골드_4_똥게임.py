import sys

def DynamicProgramming(N, choices):
    # dp[i][0]: i번째 턴까지 진행했을 때, 건너뛰기를 사용하지 않은 상태에서의 최대 사람 수
    # dp[i][1]: i번째 턴까지 진행했을 때, 건너뛰기를 사용한 상태에서의 최대 사람 수
    dp = [[-float('inf')] * 2 for _ in range(N + 1)]

    # 초기값 설정: 첫 번째 사람 수는 1명
    dp[0][0] = 1  # 첫 번째 턴, 건너뛰기 사용하지 않음
    dp[0][1] = -float('inf')  # 첫 번째 턴, 건너뛰기 사용 불가능

    # 모든 경우의 수를 계산
    for i in range(1, N + 1):
        # 첫 번째 선택지를 선택했을 때의 경우
        choice1_op, choice1_val = choices[i - 1][0][0], int(choices[i - 1][0][1])

        # 두 번째 선택지를 선택했을 때의 경우
        choice2_op, choice2_val = choices[i - 1][1][0], int(choices[i - 1][1][1])

        # 첫 번째 선택지를 선택했을 때
        if choice1_op == "+":
            if dp[i - 1][0] > 0:  # 이전에 사람 수가 0보다 큰 경우만 고려
                dp[i][0] = max(dp[i][0], dp[i - 1][0] + choice1_val)
            if dp[i - 1][1] > 0:
                dp[i][1] = max(dp[i][1], dp[i - 1][1] + choice1_val)
        elif choice1_op == "-":
            if dp[i - 1][0] > 0:
                dp[i][0] = max(dp[i][0], dp[i - 1][0] - choice1_val)
            if dp[i - 1][1] > 0:
                dp[i][1] = max(dp[i][1], dp[i - 1][1] - choice1_val)
        elif choice1_op == "*":
            if dp[i - 1][0] > 0:
                dp[i][0] = max(dp[i][0], dp[i - 1][0] * choice1_val)
            if dp[i - 1][1] > 0:
                dp[i][1] = max(dp[i][1], dp[i - 1][1] * choice1_val)
        elif choice1_op == "/":
            if dp[i - 1][0] > 0:
                dp[i][0] = max(dp[i][0], dp[i - 1][0] // choice1_val)
            if dp[i - 1][1] > 0:
                dp[i][1] = max(dp[i][1], dp[i - 1][1] // choice1_val)

        # 두 번째 선택지를 선택했을 때
        if choice2_op == "+":
            if dp[i - 1][0] > 0:
                dp[i][0] = max(dp[i][0], dp[i - 1][0] + choice2_val)
            if dp[i - 1][1] > 0:
                dp[i][1] = max(dp[i][1], dp[i - 1][1] + choice2_val)
        elif choice2_op == "-":
            if dp[i - 1][0] > 0:
                dp[i][0] = max(dp[i][0], dp[i - 1][0] - choice2_val)
            if dp[i - 1][1] > 0:
                dp[i][1] = max(dp[i][1], dp[i - 1][1] - choice2_val)
        elif choice2_op == "*":
            if dp[i - 1][0] > 0:
                dp[i][0] = max(dp[i][0], dp[i - 1][0] * choice2_val)
            if dp[i - 1][1] > 0:
                dp[i][1] = max(dp[i][1], dp[i - 1][1] * choice2_val)
        elif choice2_op == "/":
            if dp[i - 1][0] > 0:
                dp[i][0] = max(dp[i][0], dp[i - 1][0] // choice2_val)
            if dp[i - 1][1] > 0:
                dp[i][1] = max(dp[i][1], dp[i - 1][1] // choice2_val)

        # 현재 턴을 건너뛰는 경우 (한 번만 허용)
        if dp[i - 1][0] > 0:
            dp[i][1] = max(dp[i][1], dp[i - 1][0])

        # 모든 값이 음수인 경우 게임 종료
        if max(dp[i][0], dp[i][1]) <= 0:
            return 0

    # 마지막 턴에서의 최대 점수 반환
    return max(dp[N])

def Solution():
    N = int(sys.stdin.readline().strip())

    choices = []
    for i in range(N):
        choices.append(list(sys.stdin.readline().strip().split(" ")))

    result = DynamicProgramming(N, choices)

    if result <= 0:
        print("ddong game")
    else:
        print(result)


if __name__ == "__main__":
    Solution()

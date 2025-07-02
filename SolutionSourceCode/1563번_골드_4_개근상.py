D = int(input());


dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(D + 1)]

dp[0][0][0] = 1

for O in range(0, D, 1):
    for L in range(0, 2, 1):
        for A in range(0, 3, 1):
            last_day = dp[O][L][A];

            if not last_day:
                continue;

            dp[O + 1][L][0] = dp[O + 1][L][0] + last_day;

            if (A < 2):
                dp[O + 1][L][A + 1] = dp[O + 1][L][A + 1] + last_day;

            if (L < 1):
                dp[O + 1][L + 1][0] = dp[O + 1][L + 1][0] + last_day;

answer = 0;
for L in range(0, 2, 1):
    for A in range(0, 3, 1):
        answer += dp[D][L][A];

answer %= 1000000;

print(answer);
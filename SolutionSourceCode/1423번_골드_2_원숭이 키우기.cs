using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        long[] C = Console.ReadLine().Split().Select(long.Parse).ToArray();
        long[] P = Console.ReadLine().Split().Select(long.Parse).ToArray();
        int D = int.Parse(Console.ReadLine());

        // 초기 힘의 합을 계산
        long initial_sum = 0;
        for(int k = 0; k < N; k++)
        {
            initial_sum += C[k] * P[k];
        }

        // dp[j] → j일 동안 훈련시켜 얻을 수 있는 최대 추가 힘
        long[] dp = new long[D + 1];

        for(int k = 0; k < N; k++)
        {
            if (C[k] == 0)
            {
                continue;
            }

            long trainable = Math.Min(C[k], (long)D);
            if(trainable == 0)
                continue;

            for(long c = 0; c < trainable; c++)
            {
                long[] temp = new long[D +1];
                Array.Copy(dp, temp, D +1);

                for(int m =1; m <= N -k -1; m++)
                {
                    long gain = P[k + m] - P[k];
                    int cost = m;

                    if(gain <=0 || cost > D)
                        continue;

                    for(int j = D; j >= cost; j--)
                    {
                        if(temp[j - cost] + gain > dp[j])
                        {
                            dp[j] = temp[j - cost] + gain;
                        }
                    }
                }
            }
        }

        // 최종 힘의 합 계산: 초기 힘 + D일 동안 얻을 수 있는 최대 추가 힘
        long total_power = initial_sum + dp[D];
        Console.WriteLine(total_power);
    }
}
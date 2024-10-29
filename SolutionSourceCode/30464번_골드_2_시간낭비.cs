using System;
using System.Collections.Generic;
using System.Linq;

namespace CodingTest
{
    class Program
    {
        static int N;
        static int[] A;
        static int[][] dp;
        static int[][] state;  // 방문 상태를 나타내는 배열: 0=미방문, -1=방문 중, 1=방문 완료
        static bool[][] inCycle;  // 사이클에 포함된 상태를 표시

        static void Main(string[] args)
        {
            N = int.Parse(Console.ReadLine());
            A = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();

            dp = new int[N][];
            state = new int[N][];
            inCycle = new bool[N][];
            for (int i = 0; i < N; ++i)
            {
                dp[i] = new int[3];
                state[i] = new int[3];
                inCycle[i] = new bool[3];
                for (int j = 0; j < 3; ++j)
                {
                    dp[i][j] = -1;
                    state[i][j] = 0;  // 미방문 상태로 초기화
                    inCycle[i][j] = false;
                }
            }

            int result = Dfs(0, 0);
            Console.WriteLine(result == -2 ? "-1" : result.ToString());
        }

        static int Dfs(int pos, int reverse)
        {
            if (pos == N - 1)
            {
                return 0;  // 학교에 도착한 경우
            }

            if (state[pos][reverse] == -1)
            {
                // 사이클 발견
                inCycle[pos][reverse] = true;
                return -2;  // 사이클이 있는 경로로는 유효한 시간이 없음
            }

            if (state[pos][reverse] == 1)
            {
                // 이미 방문 완료된 상태
                if (inCycle[pos][reverse])
                {
                    return -2;  // 사이클에 포함된 상태면 -2 반환
                }
                else
                {
                    return dp[pos][reverse];
                }
            }

            state[pos][reverse] = -1;  // 방문 중 상태로 표시
            int maxTime = -1;

            int moveDistance = A[pos];
            if (moveDistance == 0)
            {
                state[pos][reverse] = 1;  // 방문 완료
                return -2;  // 이동할 수 없는 경우
            }

            // 현재 방향으로 이동
            int nextPos = (reverse % 2 == 0) ? pos + moveDistance : pos - moveDistance;
            if (nextPos >= 0 && nextPos < N)
            {
                int time = Dfs(nextPos, reverse);
                if (time >= 0)
                {
                    maxTime = Math.Max(maxTime, time + 1);
                }
            }

            // 방향을 반전하여 이동
            if (reverse < 2)
            {
                nextPos = (reverse % 2 == 0) ? pos - moveDistance : pos + moveDistance;
                if (nextPos >= 0 && nextPos < N)
                {
                    int time = Dfs(nextPos, reverse + 1);
                    if (time >= 0)
                    {
                        maxTime = Math.Max(maxTime, time + 1);
                    }
                }
            }

            state[pos][reverse] = 1;  // 방문 완료 상태로 변경
            dp[pos][reverse] = maxTime;

            // 사이클 여부 전달
            if (maxTime == -1)
            {
                return -2;  // 학교에 도달할 수 없는 경우
            }
            else
            {
                return dp[pos][reverse];
            }
        }
    }
}

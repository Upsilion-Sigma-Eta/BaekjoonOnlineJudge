using System;

namespace CodingTest
{
    class Program
    {
        static void Main(string[] args)
        {
            int N, K;
            string[] i_1 = Console.ReadLine().Split(" ");
            
            N = int.Parse(i_1[0]);
            K = int.Parse(i_1[1]);

            int[][] affection_grid = new int[N][];
            
            for (int i = 0; i < N; ++i)
            {
                string[] i_2 = Console.ReadLine().Split(" ");
                affection_grid[i] = new int[K];
                for (int j = 0; j < K; ++j)
                {
                    affection_grid[i][j] = int.Parse(i_2[j]);
                }
            }

            int[] prev = affection_grid[0];
            int prev_max = int.MinValue;
            int prev_max_index = -1;
            int prev_max_second = int.MinValue;

            for (int i = 0; i < K; ++i)
            {
                if (prev[i] > prev_max)
                {
                    prev_max_second = prev_max;
                    prev_max = prev[i];
                    prev_max_index = i;
                }
                else if (prev[i] > prev_max_second)
                {
                    prev_max_second = prev[i];
                }
            }

            for (int i = 1; i < N; ++i)
            {
                int[] affection_dp = new int[K];
                int new_max = int.MinValue;
                int new_max_index = -1;
                int new_max_second = int.MinValue;

                for (int j = 0; j < K; ++j)
                {
                    if (j == prev_max_index)
                    {
                        affection_dp[j] = affection_grid[i][j] + prev_max_second;
                    }
                    else
                    {
                        affection_dp[j] = affection_grid[i][j] + prev_max;
                    }

                    if (affection_dp[j] > new_max)
                    {
                        new_max_second = new_max;
                        new_max = affection_dp[j];
                        new_max_index = j;
                    }
                    else if (affection_dp[j] > new_max_second)
                    {
                        new_max_second = affection_dp[j];
                    }
                }

                prev = affection_dp;
                prev_max = new_max;
                prev_max_index = new_max_index;
                prev_max_second = new_max_second;
            }
            
            Console.WriteLine(prev_max.ToString());
        }
    }
}

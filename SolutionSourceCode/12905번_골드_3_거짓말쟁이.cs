using System;
using System.Collections.Generic;

namespace CodingTest
{
    // https://github.com/belowyoon/algorithm/blob/main/%EB%B0%B1%EC%A4%80/Gold/12905.%E2%80%85%EA%B1%B0%EC%A7%93%EB%A7%90%EC%9F%81%EC%9D%B4/%EA%B1%B0%EC%A7%93%EB%A7%90%EC%9F%81%EC%9D%B4.cc 참고
    class Program
    {
        static int n;
        static List<int> arr = new List<int>();
        static List<int> result = new List<int>();
        static int minLiar = int.MaxValue;

        static void Main(string[] args)
        {
            // 입력 받기
            n = int.Parse(Console.ReadLine());
            arr = new List<int>(new int[n]);
            result = new List<int>(new int[n]);

            string input = Console.ReadLine();
            for (int i = 0; i < n; i++)
            {
                char t = input[i];
                if (t == 'H') arr[i] = 1;
                else if (t == '?') arr[i] = -1;
            }

            // 두 가지 초기 상태로 DFS 호출
            result[0] = 1; // 첫 번째 사람이 정직한 경우
            DFS(1, 0);

            result[0] = 0; // 첫 번째 사람이 거짓말쟁이인 경우
            DFS(1, 1);

            // 결과 출력
            Console.WriteLine(minLiar == int.MaxValue ? -1 : minLiar);
        }

        static void DFS(int idx, int liarCount)
        {
            // 현재 거짓말쟁이 수가 이미 최소 거짓말쟁이 수 이상이면 탐색 중지
            if (liarCount >= minLiar) return;

            // 모든 사람을 탐색한 경우
            if (idx >= n)
            {
                bool isValid = (result[n - 1] == 1) ? (arr[n - 1] == result[0]) : (arr[n - 1] != result[0]);
                if (arr[n - 1] == -1 || isValid)
                {
                    minLiar = Math.Min(liarCount, minLiar);
                }
                return;
            }

            // 이전 사람에 대한 답변이 없는 경우(?)
            if (arr[idx - 1] == -1)
            {
                // 현재 사람을 정직한 사람으로 가정하고 DFS
                result[idx] = 1;
                DFS(idx + 1, liarCount);

                // 현재 사람을 거짓말쟁이로 가정하고 DFS
                result[idx] = 0;
                DFS(idx + 1, liarCount + 1);
            }
            else
            {
                // 이전 사람의 답변이 있는 경우
                result[idx] = (result[idx - 1] == 1) ? arr[idx - 1] : 1 - arr[idx - 1];
                
                int newLiarCount = liarCount + (result[idx] == 0 ? 1 : 0);
                DFS(idx + 1, newLiarCount);
            }
        }
    }
}

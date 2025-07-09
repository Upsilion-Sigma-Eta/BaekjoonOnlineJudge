#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <climits>

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int N, K;
    std::cin >> N >> K;

    long **pascal_triangle = new long *[N + 1];

    // 파스칼의 삼각형 생성
    // 초기값 생성
    for (int i = 0; i < N + 1; i++)
    {
        pascal_triangle[i] = new long[K + 1]{
            1,
        };
    }

    // 파스칼의 삼각형 계산
    for (int i = 1; i < N + 1; i++)
    {
        for (int j = 1; j < K + 1; j++)
        {
            pascal_triangle[i][j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j];
        }
    }

    std::cout << pascal_triangle[N][K];

    return 0;
}

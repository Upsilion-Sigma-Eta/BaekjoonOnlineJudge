#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

unsigned long long NumberOfCombination(int n, int m)
{
	if (m > n / 2) m = n - m; // 조합의 성질을 이용해서 최솟값 계산을 위한 최적화

	unsigned long long result = 1;
	for (int i = 0; i < m; ++i)
	{
		result *= (n - i);
	}
	for (int i = 1; i <= m; ++i)
	{
		result /= i;
	}

	return result;
}

int main(int argc, char* argv[])
{
	int totalCaseCount = 0;

	std::cin >> totalCaseCount;

	for (int i = 0; i < totalCaseCount; ++i)
	{
		int n = 0;
		int m = 0;

		std::cin >> n;
		std::cin >> m;

		printf("%llu\n", NumberOfCombination(m, n));
	}
	

	return 0;
}
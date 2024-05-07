#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

int main(int argc, char* argv[])
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);	std::cin.tie(nullptr);
	std::cout.tie(nullptr);

	int totalNumberCount = 0;

	std::cin >> totalNumberCount;

	std::vector<int> inputVector = std::vector<int>();

	for (int i = 0; i < totalNumberCount; ++i)
	{
		int temp = 0;
		std::cin >> temp;
		inputVector.push_back(temp);
	}

	std::sort(inputVector.begin(), inputVector.end());

	for (int i = 0; i < totalNumberCount; ++i)
	{
		std::cout << inputVector[i] << '\n';
	}


	return 0;
}
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iostream>

void ActualProcess(std::istream& input)
{
    long long G = 0;
    long long T = 0;
    long long A = 0;
    long long D = 0;

    long long X = 0;
    long long Y = 0;

    while (true)
    {
        input >> G >> T >> A >> D;

        if (G == -1 && T == -1 && A == -1 && D == -1)
        {
            return;
        }

        long long totalTeams = G * A + D;
        long long nextPowerOfTwo = 1;
        while (nextPowerOfTwo < totalTeams) {
            nextPowerOfTwo <<= 1;
        }
        Y = nextPowerOfTwo - totalTeams;

        X = G * T * (T - 1) / 2 + nextPowerOfTwo - 1;

        std::cout << G << '*' << A << '/' << T << '+' << D << '=' << X << '+' << Y << std::endl;
    }
}

int main() {
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);	std::cin.tie(nullptr);
	std::cout.tie(nullptr);

	ActualProcess(std::cin);

    return 0;
}

#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

static int count = 0;

static int N = 0;
static int Q = 0;
static int K = 0;
static int* A = nullptr;
static int* ResultA = nullptr;

void Swap(int* a, int* b)
{
	int temp = *a;
	*a = *b;
	*b = temp;

	++count;

	if (count == K)
	{
		ResultA = new int[N];
		for (int i = 0; i < N; ++i)
		{
			ResultA[i] = A[i];
		}
	}
}

int Partition(int* A, int p, int r)
{
	int x = A[r];
	int i = p - 1;

	for (int j = p; j <= r - 1; ++j)
	{
		if (A[j] <= x)
		{
			Swap(&A[++i], &A[j]);
		}
	}

	if (i + 1 != r)
	{
		Swap(&A[i + 1], &A[r]);
	}

	return i + 1;
}

int Select(int* A, int p, int r, int q)
{
	if (p == r)
	{
		return A[p];
	}

	int t = Partition(A, p, r);
	int k = t - p + 1;

	if (q < k)
	{
		return Select(A, p, t - 1, q);
	}
	else if (q == k)
	{
		return A[t];
	}
	else
	{
		return Select(A, t + 1, r, q - k);
	}
}

void ActualProcess(std::istream& input)
{
	input >> N >> Q >> K;
	count = 0;

	A = new int[N];
	for (int i = 0; i < N; ++i)
	{
		input >> A[i];
	}

	Select(A, 0, N - 1, Q);

	if (ResultA != nullptr)
	{
		for (int i = 0; i < N - 1; ++i)
		{
			std::cout << ResultA[i] << ' ';
		}

		std::cout << ResultA[N - 1];

		delete[] A;
		delete[] ResultA;
		ResultA = nullptr;
		A = nullptr;
	}
	else
	{
		delete[] A;
		A = nullptr;

		std::cout << -1;
	}
}

int main() {
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);	std::cin.tie(nullptr);
	std::cout.tie(nullptr);

	ActualProcess(std::cin);

    return 0;
}

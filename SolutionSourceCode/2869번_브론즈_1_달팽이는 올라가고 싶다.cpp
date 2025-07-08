#include <iostream>
#include <cmath>

int main()
{
    long A;
    long B;
    long V;

    std::cin >> A >> B >> V;

    if (V > A)
    {
        std::cout << static_cast<long>(::ceil(static_cast<double>((V - A)) / static_cast<double>((A - B)))) + 1 << "\n";
    }
    else
    {
        std::cout << 1 << "\n";
    }

    return 0;
}

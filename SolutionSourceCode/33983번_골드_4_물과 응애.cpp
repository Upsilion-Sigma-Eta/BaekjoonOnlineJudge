#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <cmath>
#include <climits>

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;

    std::string s;
    std::cin >> s;

    std::stack<char> stk_front = std::stack<char>();
    std::stack<char> stk_back = std::stack<char>();

    // 1) 길이와 개수 조건
    int cntH = 0, cntO = 0;
    for (char c : s)
        (c == 'H' ? cntH : cntO)++;
    if (N % 3 || cntH != 2 * cntO)
    {
        std::cout << "mix";
        return 0;
    }

    // 2) 앞에서부터 접두사 검사
    int h = 0, o = 0;
    for (char c : s)
    {
        if (c == 'H')
            ++h;
        else
            ++o;
        if (o > h)
        { // O 가 더 많아지면 불가능
            std::cout << "mix";
            return 0;
        }
    }

    // 3) 뒤에서부터 접미사 검사
    h = o = 0;
    for (int i = N - 1; i >= 0; --i)
    {
        if (s[i] == 'H')
            ++h;
        else
            ++o;
        if (o > h)
        { // 뒤 기준으로도 O 가 더 많아지면 불가능
            std::cout << "mix";
            return 0;
        }
    }

    if (stk_front.empty() || stk_back.empty())
    {
        std::cout << "pure";
    }
    else
    {
        std::cout << "mix";
    }

    return 0;
}
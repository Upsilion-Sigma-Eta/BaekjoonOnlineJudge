#include <iostream>
#include <valarray>
#include <vector>

int main(void) {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    std::string str;
    std::cin >> str;

    while (str != "0") {

        int front = 0;
        int back = str.length() - 1;
        bool isPalendrome = true;

        while (front <= back) {
            if (str[front] != str[back]) {
                isPalendrome = false;
                break;
            }
            front++;
            back--;
        }

        if (isPalendrome) {
            std::cout << "yes\n";
        } else {
            std::cout << "no\n";
        }

        std::cin >> str;
    }


    return 0;
}

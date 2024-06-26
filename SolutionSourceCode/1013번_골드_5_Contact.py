import sys
import re

def actual_code():
    T = int(sys.stdin.readline())

    regex_pattern = r'(100+1+|01)+'

    signal_string = []
    for _ in range(T):
        signal_string.append(sys.stdin.readline().strip())

    for singal in signal_string:
        if (re.fullmatch(regex_pattern, singal)):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    actual_code()
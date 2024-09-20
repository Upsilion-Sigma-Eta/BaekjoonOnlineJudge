import sys
import math

# https://codio.tistory.com/119 참고하였음
def Solution():
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        l, r = map(int, sys.stdin.readline().strip().split())

        if (r >= 4):
            sys.stdout.write(str(r) + "\n")
        else:
            number_string = "".join([str(2 ** i) for i in range(l, r + 1)])
            number = int(number_string)
            result = (number & -number).bit_length() - 1

            sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
    Solution()
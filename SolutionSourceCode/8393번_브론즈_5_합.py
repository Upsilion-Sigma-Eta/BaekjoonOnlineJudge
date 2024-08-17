import sys

def Solution():
    sum = 0
    for i in range(int(sys.stdin.readline().strip()) + 1):
        sum += i

    print(sum)


if __name__ == "__main__":
    Solution()
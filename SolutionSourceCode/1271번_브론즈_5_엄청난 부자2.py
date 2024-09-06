import sys

def Solution():
    m, n = map(int, sys.stdin.readline().strip().split())

    sys.stdout.write(str(m // n) + "\n")
    sys.stdout.write(str(m - (n * (m // n))) + "\n")


if __name__ == "__main__":
    Solution()

import sys

def Solution():
    N = int(sys.stdin.readline().strip())

    for i in range(1, N + 1):
        sys.stdout.write(str(i) + "\n")

if __name__ == "__main__":
    Solution()
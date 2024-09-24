import sys

def Solution():
    S = sys.stdin.readline().strip()
    N = int(sys.stdin.readline().strip())

    sys.stdout.write(S[N - 1])

if __name__ == "__main__":
    Solution()
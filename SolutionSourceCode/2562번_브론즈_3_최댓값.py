import sys

def Solution():
    N = []
    for _ in range(9):
        N.append(int(sys.stdin.readline().strip()))

    sys.stdout.write(str(max(N)) + "\n" + str(N.index(max(N)) + 1))

if __name__ == "__main__":
    Solution()
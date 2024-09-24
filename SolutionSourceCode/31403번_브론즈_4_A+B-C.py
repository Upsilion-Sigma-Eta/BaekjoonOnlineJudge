import sys

def Solution():
    A = int(sys.stdin.readline().strip())
    B = int(sys.stdin.readline().strip())
    C = int(sys.stdin.readline().strip())

    sys.stdout.write(str(A + B - C) + "\n")
    sys.stdout.write(str(int(str(A) + str(B)) - C) + "\n")

if __name__ == "__main__":
    Solution()
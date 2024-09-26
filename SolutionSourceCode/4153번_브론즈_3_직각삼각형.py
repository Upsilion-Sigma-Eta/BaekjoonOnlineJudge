import sys

def Solution():
    while True:
        A, B, C = map(int, sys.stdin.readline().strip().split())

        if (A == 0 and B == 0 and C == 0):
            break

        if (pow(C, 2) == pow(A, 2) + pow(B, 2) or
        pow(A, 2) == pow(C, 2) + pow(B, 2) or
        pow(B, 2) == pow(A, 2) + pow(C, 2)):
            sys.stdout.write("right\n")
        else:
            sys.stdout.write("wrong\n")

if __name__ == "__main__":
    Solution()
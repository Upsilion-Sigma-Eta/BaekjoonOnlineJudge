import sys

def Solution():
    T = int(sys.stdin.readline().strip())

    for i in range(1, T + 1):
        A, B = map(int, sys.stdin.readline().strip().split())

        sys.stdout.write("Case #" + str(i) + ": " + str(A) + " + " + str(B) + " = " + str(A + B) + "\n")

Solution()
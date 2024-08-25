import sys

T = int(sys.stdin.readline().strip())
for i in range(T):
    A, B = map(int, sys.stdin.readline().strip().split())
    sys.stdout.write(str(A + B) + "\n")
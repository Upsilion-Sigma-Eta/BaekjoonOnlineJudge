import sys

def actual_code():
    A, B, C = map(int, sys.stdin.readline().strip().split())

    sys.stdout.write(str(A + B + C))

if __name__ == '__main__':
    actual_code()

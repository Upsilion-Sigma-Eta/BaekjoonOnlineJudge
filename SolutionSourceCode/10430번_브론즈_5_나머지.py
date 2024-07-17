import sys
from collections import deque

def actual_code():
    A, B, C = map(int, sys.stdin.readline().strip().split())

    sys.stdout.write(str((A + B) % C) + "\n")
    sys.stdout.write(str(((A % C) + (B % C)) %C) + "\n")
    sys.stdout.write(str((A * B) % C) + "\n")
    sys.stdout.write(str(((A % C) * (B % C)) %C))

if __name__ == '__main__':
    actual_code()

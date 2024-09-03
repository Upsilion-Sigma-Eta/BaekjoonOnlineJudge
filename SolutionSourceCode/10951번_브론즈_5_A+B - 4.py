import sys

A, B = map(int, sys.stdin.readline().strip().split())
while A != None and B != None:
    sys.stdout.write(str(A + B) + "\n")

    try:
        A, B = map(int, sys.stdin.readline().strip().split())
    except:
        break
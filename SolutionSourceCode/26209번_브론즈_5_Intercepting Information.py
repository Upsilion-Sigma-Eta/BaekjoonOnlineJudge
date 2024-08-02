import sys

info = list(map(int, sys.stdin.readline().split()))

if (max(info) == 9):
    sys.stdout.write("F")
else:
    sys.stdout.write("S")
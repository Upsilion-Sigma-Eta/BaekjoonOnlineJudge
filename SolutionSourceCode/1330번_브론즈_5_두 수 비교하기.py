import sys

a, b = map(int, sys.stdin.readline().strip().split())

if a < b:
    sys.stdout.write('<')
elif a > b:
    sys.stdout.write('>')
elif a == b:
    sys.stdout.write('==')
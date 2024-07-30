import sys

year = int(sys.stdin.readline().strip())

if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    sys.stdout.write("1")
else:
    sys.stdout.write("0")
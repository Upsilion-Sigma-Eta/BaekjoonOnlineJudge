import sys

X = int(sys.stdin.readline().strip())
Y = int(sys.stdin.readline().strip())

if X > 0 and Y > 0:
    sys.stdout.write("1")
elif X < 0 and Y > 0:
    sys.stdout.write("2")
elif X < 0 and Y < 0:
    sys.stdout.write("3")
elif X > 0 and Y < 0:
    sys.stdout.write("4")

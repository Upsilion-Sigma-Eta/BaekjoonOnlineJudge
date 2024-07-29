import sys

def actual_code():
    score = int(sys.stdin.readline().strip())

    if (90 <= score <= 100):
        sys.stdout.write('A')
    elif (80 <= score < 90):
        sys.stdout.write('B')
    elif (70 <= score < 80):
        sys.stdout.write('C')
    elif (60 <= score < 70):
        sys.stdout.write('D')
    else:
        sys.stdout.write('F')


if __name__ == '__main__':
    actual_code()
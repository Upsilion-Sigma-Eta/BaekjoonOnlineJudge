import sys

def actual_code():
    N = int(sys.stdin.readline().strip())

    house_location = []

    house_location = list(map(int, sys.stdin.readline().strip().split()))

    house_location.sort()

    sys.stdout.write(str(house_location[(N - 1) // 2]))

if __name__ == '__main__':
    actual_code()

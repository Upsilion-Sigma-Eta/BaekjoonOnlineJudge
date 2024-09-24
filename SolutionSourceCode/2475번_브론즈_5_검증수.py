import sys

def Solution():
    id = list(map(int, sys.stdin.readline().strip().split()))

    validation_number = 0
    for i in id:
        validation_number += pow(i, 2)

    validation_number %= 10

    sys.stdout.write(str(validation_number))

if __name__ == "__main__":
    Solution()
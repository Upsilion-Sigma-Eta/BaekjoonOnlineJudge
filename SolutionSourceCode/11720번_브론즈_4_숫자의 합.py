import sys

def Solution():
    N = int(sys.stdin.readline().strip())
    S = sys.stdin.readline().strip()

    sum_of_digits = 0
    for digit in S:
        sum_of_digits += int(digit)

    sys.stdout.write(str(sum_of_digits))

if __name__ == "__main__":
    Solution()
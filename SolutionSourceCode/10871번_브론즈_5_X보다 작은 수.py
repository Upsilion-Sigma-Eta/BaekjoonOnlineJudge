import sys

def Solution():
    N, X = map(int, sys.stdin.readline().strip().split())

    number_arr = list(map(int, sys.stdin.readline().strip().split()))
    number_arr = filter(lambda x: x < X, number_arr)

    for i in number_arr:
        sys.stdout.write(str(i) + " ")

if __name__ == "__main__":
    Solution()
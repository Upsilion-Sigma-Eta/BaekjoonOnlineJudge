import sys

def Solution():
    N = int(input())

    for j in range(1, 10, 1):
        print(str(N) + " * " + str(j) + " = " + str(N * j))

if __name__ == "__main__":
    Solution()
import sys

CONST_MOD = (10 ** 9) + 7

# https://memoacmicpc.tistory.com/entry/%EB%B0%B1%EC%A4%80-26035%EB%B2%88-0101 참조
def Solution():
    N, M = map(int, sys.stdin.readline().strip().split())

    print((pow(2, M, CONST_MOD) + pow(2, N, CONST_MOD) - 2) % CONST_MOD)

if __name__ == "__main__":
    Solution()

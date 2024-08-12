import sys

def Solution():
    dice = list(map(int, sys.stdin.readline().strip().split()))

    if (dice[0] == dice[1] == dice[2]):
        print(10000 + dice[0] * 1000)
    elif (dice[0] == dice[1]):
        print(1000 + dice[0] * 100)
    elif (dice[1] == dice[2]):
        print(1000 + dice[1] * 100)
    elif (dice[0] == dice[2]):
        print(1000 + dice[0] * 100)
    elif (dice[0] != dice[1] != dice[2]):
        print(max(dice) * 100)

if __name__ == "__main__":
    Solution()
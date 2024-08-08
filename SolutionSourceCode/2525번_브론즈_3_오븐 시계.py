import sys

def Solution():
    hour, minute = map(int, sys.stdin.readline().strip().split())
    pass_minute = int(sys.stdin.readline().strip())

    result_minute = (minute + pass_minute)
    result_hour = hour

    if (result_minute >= 60):
        result_hour += result_minute // 60
        result_minute %= 60
    if (result_hour >= 24):
        result_hour %= 24

    sys.stdout.write(str(result_hour) + " " + str(result_minute) + "\n")


if __name__ == "__main__":
    Solution()
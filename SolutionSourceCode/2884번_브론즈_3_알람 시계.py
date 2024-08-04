import sys

hour, minute = map(int, sys.stdin.readline().strip().split())
targetMinute = 45

new_minute = minute - targetMinute
new_hour = hour

if (new_minute < 0):
    new_minute = 60 + new_minute
    new_hour -= 1

    if (new_hour < 0):
        new_hour = 24 + new_hour

sys.stdout.write(str(new_hour) + " " + str(new_minute))
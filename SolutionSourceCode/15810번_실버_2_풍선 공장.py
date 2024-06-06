
import sys

def checkBallonCount(ballonBlowTimes, ballonNumber, minutes):
    ballonBlowCount = 0
    for time in ballonBlowTimes:
        ballonBlowCount += minutes // time
        if (ballonBlowCount >= ballonNumber):
            break

    return ballonBlowCount >= ballonNumber

def ActualCode():
    firstInput = sys.stdin.readline().strip().split(' ')
    ballonBlowTime = sys.stdin.readline().strip().split(' ')

    balloonNumber = int(firstInput[1])

    ballonBlowTimeOriginal = list(map(int, ballonBlowTime))

    ballonBlowTimeOriginal.sort()

    minutes = 0

    left = min(ballonBlowTimeOriginal)
    right = max(ballonBlowTimeOriginal) * balloonNumber

    while left <= right:
        mid = (left + right) // 2
        if checkBallonCount(ballonBlowTimeOriginal, balloonNumber, mid):
            right = mid - 1
            minutes = mid
        else:
            left = mid + 1

    sys.stdout.write(str(minutes))

if __name__ == '__main__':
    ActualCode()

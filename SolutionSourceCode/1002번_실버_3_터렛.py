import sys

def calculateDistance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def actualCode():
    testCaseNumber = int(sys.stdin.readline().strip())

    for i in range(testCaseNumber):
        testCaseString = list(map(int, sys.stdin.readline().strip().split(' ')))

        x1 = testCaseString[0]
        y1 = testCaseString[1]
        r1 = testCaseString[2]

        x2 = testCaseString[3]
        y2 = testCaseString[4]
        r2 = testCaseString[5]

        centerToCenterDistance = calculateDistance(x1, y1, x2, y2)

        if (centerToCenterDistance == abs(r1 + r2)) or (centerToCenterDistance == abs(r1 - r2) and centerToCenterDistance != 0):
            sys.stdout.write('1\n')
        elif (centerToCenterDistance > abs(r1 - r2) and centerToCenterDistance < abs(r1 + r2)):
            sys.stdout.write('2\n')
        elif (centerToCenterDistance == 0 and r1 == r2):
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write('0\n')


if __name__ == '__main__':
    actualCode()

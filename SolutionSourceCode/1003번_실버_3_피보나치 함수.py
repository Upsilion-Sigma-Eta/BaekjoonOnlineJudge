import sys

def calcMemo(n, memo):
    if (n in memo.keys()):
        return memo[n]

    previous = calcMemo(n - 1, memo)
    previousTwoStep = calcMemo(n - 2, memo)

    tempReturnValue = [previous[0] + previousTwoStep[0], previous[1] + previousTwoStep[1]]

    memo[n] = tempReturnValue

    return tempReturnValue

def actualCode():
    testCaseNumber = int(sys.stdin.readline().strip())

    memo = {0: [1, 0], 1: [0, 1], 2: [1, 1], 3: [1, 2]}

    calcMemo(40, memo)

    for i in range(testCaseNumber):
        testCaseInput = int(sys.stdin.readline().strip())

        onePrintedCount = 0
        zeroPrintedCount = 0

        sys.stdout.write(str(memo[testCaseInput][0]) + ' ' + str(memo[testCaseInput][1]) + '\n')



if __name__ == '__main__':
    actualCode()

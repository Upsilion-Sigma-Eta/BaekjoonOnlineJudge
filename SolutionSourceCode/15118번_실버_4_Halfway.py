import sys

def binary_search(numbers, target):
    left = 1
    right = numbers - 1
    mid = 0
    current_sum = 0

    while left < right:
        mid = (left + right) // 2
        current_sum = (mid * (2 * numbers - mid - 1)) // 2
        if (current_sum < target):
            left = mid + 1
        else:
            right = mid

    return left

def actualCode():
    testCaseNumber = int(sys.stdin.readline().strip())

    total_sum = (((testCaseNumber - 1) * testCaseNumber) / 2)
    target_sum = (total_sum + 1) // 2

    index = binary_search(testCaseNumber, target_sum)


    sys.stdout.write(str(index) + '\n')

if __name__ == '__main__':
    actualCode()

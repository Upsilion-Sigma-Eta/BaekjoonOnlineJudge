import sys

def actual_code():
    A, B = map(int, sys.stdin.readline().strip().split())
    N = int(sys.stdin.readline().strip())

    frequency_list = []
    for _ in range(N):
        frequency_list.append(int(sys.stdin.readline().strip()))

    counter = 0

    for i in range(N):
        frequency_list[i] = abs(B - frequency_list[i])

    A = abs(B - A)

    if (A == B):
        sys.stdout.write(str(counter))
        return

    frequency_list.sort()

    if (frequency_list[0] >= A):
        sys.stdout.write(str(A))
        return

    minimum_distance = frequency_list[0]
    counter += 1

    counter += abs(minimum_distance)

    sys.stdout.write(str(counter))

if __name__ == '__main__':
    actual_code()

import sys

def Solution():
    N, K =  map(int, sys.stdin.readline().strip().split())

    students = list(map(int, sys.stdin.readline().strip().split()))

    diffs = []

    for i in range(1, N):
        diffs.append(students[i] - students[i - 1])

    indices = sorted(range(len(diffs)), key=lambda x: diffs[x], reverse=True)
    split_points = sorted(indices[:K - 1])

    cost = 0
    previous_index = 0
    for i in split_points:
        group = students[previous_index:i + 1]
        cost += max(group) - min(group)
        previous_index = i + 1

    last_group = students[previous_index:]
    cost += max(last_group) - min(last_group)

    sys.stdout.write(str(cost) + '\n')

if __name__ == "__main__":
    Solution()
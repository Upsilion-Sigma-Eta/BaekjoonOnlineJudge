import sys

# Using a stack to propagate the compliments through the hierarchy
def give_compliment_points(hierarchy, compliment_points, current_employee):
    stack = [current_employee]

    while stack:
        employee = stack.pop()

        for subordinate in hierarchy[employee]:
            compliment_points[subordinate] += compliment_points[employee]
            stack.append(subordinate)

def actual_code():
    n, m = map(int, sys.stdin.readline().strip().split())
    employee = list(map(int, sys.stdin.readline().strip().split()))

    employee_hierarchy = [[] for _ in range(n)]
    for i in range(1, n):
        boss = employee[i] - 1
        employee_hierarchy[boss].append(i)

    compliment_points = [0] * n

    for _ in range(m):
        target, point = map(int, sys.stdin.readline().strip().split())
        target -= 1  # Convert to zero-based index
        compliment_points[target] += point

    # Propagate the compliments through the hierarchy
    give_compliment_points(employee_hierarchy, compliment_points, 0)

    sys.stdout.write(' '.join(map(str, compliment_points)) + '\n')


if __name__ == '__main__':
    actual_code()

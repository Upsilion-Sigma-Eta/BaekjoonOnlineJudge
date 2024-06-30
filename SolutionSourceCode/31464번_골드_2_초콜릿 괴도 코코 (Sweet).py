import sys
from collections import deque
import copy
import itertools

def clamp(value, min_val, max_val):
    return min(max(value, min_val), max_val)

def get_nearby_cell_list(chocolate, x, y):
    left = (clamp(x - 1, 0, len(chocolate) - 1), y)
    right = (clamp(x + 1, 0, len(chocolate) - 1), y)
    up = (x, clamp(y - 1, 0, len(chocolate[0]) - 1))
    down = (x, clamp(y + 1, 0, len(chocolate[0]) - 1))

    nearby_cell = [left, right, up, down]
    nearby_cell = list(filter(lambda v: chocolate[v[0]][v[1]] == 1 and v != (x, y), nearby_cell))

    return nearby_cell

def dfs(chocolate, start, visited):
    stack = deque()

    stack.append(start)
    visited.add(start)

    while stack:
        x, y = stack.pop()

        for neighbor in get_nearby_cell_list(chocolate, x, y):
            if neighbor in visited or chocolate[neighbor[0]][neighbor[1]] == 0:
                continue

            visited.add(neighbor)
            stack.append(neighbor)

    return visited

def has_cycle(chocolate):
    visited = set()
    parent = {}

    def dfs_cycle(x, y, px, py):
        if (x, y) in visited:
            return True

        visited.add((x, y))
        parent[(x, y)] = (px, py)

        for neighbor in get_nearby_cell_list(chocolate, x, y):
            if neighbor == parent.get((x, y)):
                continue
            if dfs_cycle(neighbor[0], neighbor[1], x, y):
                return True

        return False

    for i in range(len(chocolate)):
        for j in range(len(chocolate[0])):
            if chocolate[i][j] == 1 and (i, j) not in visited:
                if dfs_cycle(i, j, -1, -1):
                    return True

    return False

def count_piece_count(chocolate):
    visited = set()
    counter = 0

    for x in range(len(chocolate)):
        for y in range(len(chocolate[0])):
            if (x, y) in visited or chocolate[x][y] == 0:
                continue

            dfs(chocolate, (x, y), visited)
            counter += 1

    return counter

def check_is_candidate(chocolate, x, y):
    if chocolate[x][y] == 0:
        return False

    chocolate[x][y] = 0
    cycle_appeared = has_cycle(chocolate)

    if (count_piece_count(chocolate) > 1):
        cycle_appeared = True

    chocolate[x][y] = 1

    return not cycle_appeared

def actual_code():
    N = int(sys.stdin.readline().strip())

    chocolate_orig = []
    chocolate = []
    for _ in range(N):
        chocolate_orig.append(list(sys.stdin.readline().strip().split()))
        chocolate.append([0] * N)
    # We should make a dangling chocolate state.

    for i in range(N):
        for j in range(N):
            chocolate[i][j] = 0 if chocolate_orig[i][0][j] == '.' else 1

    candidate_pos = set()
    for i in range(N):
        for j in range(N):
            result = check_is_candidate(copy.deepcopy(chocolate), i, j)

            if (result):
                candidate_pos.add((i + 1, j + 1))

    counter = len(candidate_pos)

    candidate = list(candidate_pos)
    candidate = sorted(candidate, key=lambda x: (x[0], x[1]))


    sys.stdout.write(str(counter) + "\n")
    for index in range(0, len(candidate)):
        if (index != len(candidate) - 1):
            sys.stdout.write(str(candidate[index][0]) + " " + str(candidate[index][1]) + "\n")
        else:
            sys.stdout.write(str(candidate[index][0]) + " " + str(candidate[index][1]))

if __name__ == '__main__':
    actual_code()
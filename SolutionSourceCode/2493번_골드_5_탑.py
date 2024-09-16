import sys
from collections import deque

def Solution():
    N = int(sys.stdin.readline().strip())
    tower_list = list(map(int, sys.stdin.readline().strip().split()))
    tower_stack = deque([])

    receive_tower_list = []
    for index, tower in enumerate(tower_list):
        while tower_stack and tower_stack[-1][1] <= tower:
            tower_stack.pop()

        if tower_stack:
            receive_tower_list.append(tower_stack[-1][0] + 1)
        else:
            receive_tower_list.append(0)

        tower_stack.append((index, tower))

    for _ in range(N):
        sys.stdout.write(str(receive_tower_list[_]) + " ")


if __name__ == "__main__":
    Solution()
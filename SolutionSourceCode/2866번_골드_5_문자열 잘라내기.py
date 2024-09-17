import sys

def Check(grid, R, C, deleted_line_count):
    column_string_table = set()
    for c in range(C):
        column_string_table.add(''.join(grid[r][c] for r in range(deleted_line_count, R)))

    return len(column_string_table) == C

def Solution():
    R, C = map(int, sys.stdin.readline().strip().split())

    character_grid = []
    for _ in range(R):
        character_grid.append(list(sys.stdin.readline().strip()))

    left = 0
    right = R

    while left <= right:
        mid = (left + right) // 2

        if Check(character_grid, R, C, mid):
            left = mid + 1
        else:
            right = mid - 1

    print(right)

if __name__ == "__main__":
    Solution()
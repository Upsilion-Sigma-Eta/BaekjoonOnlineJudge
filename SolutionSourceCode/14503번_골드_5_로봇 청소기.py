import sys

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

UNCLEANED = 0
WALL = 1
CLEANED = 2

# x == row y == column
class CleanSweeper:
    is_shutdown = False
    cleaned_tiles = 0

    def __init__(self, current_pos_x, current_pos_y, direction):
        self.cur_pos_x = current_pos_x
        self.cur_pos_y = current_pos_y
        self.dir = direction

    def uncleaned_tile_nearby(self, grid):
        if grid[self.cur_pos_x-1][self.cur_pos_y] == UNCLEANED:
            return True
        elif grid[self.cur_pos_x][self.cur_pos_y+1] == UNCLEANED:
            return True
        elif grid[self.cur_pos_x+1][self.cur_pos_y] == UNCLEANED:
            return True
        elif grid[self.cur_pos_x][self.cur_pos_y-1] == UNCLEANED:
            return True
        else:
            return False

    def move_back(self, grid):
        if self.dir == NORTH:
            self.cur_pos_x += 1
        elif self.dir == EAST:
            self.cur_pos_y -= 1
        elif self.dir == SOUTH:
            self.cur_pos_x -= 1
        elif self.dir == WEST:
            self.cur_pos_y += 1
        return self.cur_pos_x, self.cur_pos_y

    def move_forward(self):
        if self.dir == NORTH:
            self.cur_pos_x -= 1
        elif self.dir == EAST:
            self.cur_pos_y += 1
        elif self.dir == SOUTH:
            self.cur_pos_x += 1
        elif self.dir == WEST:
            self.cur_pos_y -= 1
        return self.cur_pos_x, self.cur_pos_y

    def front_is_uncleaned(self, grid):
        if self.dir == NORTH:
            if (grid[self.cur_pos_x-1][self.cur_pos_y] == UNCLEANED):
                return True
        elif self.dir == EAST:
            if (grid[self.cur_pos_x][self.cur_pos_y + 1] == UNCLEANED):
                return True
        elif self.dir == SOUTH:
            if (grid[self.cur_pos_x + 1][self.cur_pos_y ] == UNCLEANED):
                return True
        elif self.dir == WEST:
            if (grid[self.cur_pos_x][self.cur_pos_y - 1] == UNCLEANED):
                return True
        else:
            return False

    def rotate_counter_clockwise(self):
        self.dir = (self.dir - 1) % 4

def Solution():
    N, M = map(int, sys.stdin.readline().strip().split())
    r, c, d = map(int, sys.stdin.readline().strip().split())

    grid = []
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().strip().split()))
        grid.append(row)

    mechanoid = CleanSweeper(r, c, d)

    while not mechanoid.is_shutdown:
        if (grid[mechanoid.cur_pos_x][mechanoid.cur_pos_y] == UNCLEANED):
            grid[mechanoid.cur_pos_x][mechanoid.cur_pos_y] = CLEANED
            mechanoid.cleaned_tiles += 1

        if mechanoid.uncleaned_tile_nearby(grid):
            mechanoid.rotate_counter_clockwise()
            if (mechanoid.front_is_uncleaned(grid)):
                mechanoid.move_forward()
            continue
        else:
            mechanoid.move_back(grid)
            if grid[mechanoid.cur_pos_x][mechanoid.cur_pos_y] == WALL:
                mechanoid.is_shutdown = True
                break

    sys.stdout.write(str(mechanoid.cleaned_tiles))



if __name__ == "__main__":
    Solution()
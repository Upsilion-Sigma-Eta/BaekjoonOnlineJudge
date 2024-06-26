import sys
import copy

CCTV_TYPE = [1, 2, 3, 4, 5]

def mark_seen_space(office, N, M, start_x, start_y, direction):
    # Direction is Right
    if (direction == 0):
        for col in range(start_y, M, 1):
            if (office[start_x][col] == 6):
                break
            elif (office[start_x][col] in CCTV_TYPE):
                continue
            else:
                office[start_x][col] = 7
    #Direction is Up
    if (direction == 1):
        for row in range(start_x, -1, -1):
            if (office[row][start_y] == 6):
                break
            elif (office[row][start_y] in CCTV_TYPE):
                continue
            else:
                office[row][start_y] = 7
    #Direction is Left
    if (direction == 2):
        for col in range(start_y, -1, -1):
            if (office[start_x][col] == 6):
                break
            elif (office[start_x][col] in CCTV_TYPE):
                continue
            else:
                office[start_x][col] = 7
    #Direction is Down
    if (direction == 3):
        for row in range(start_x, N, 1):
            if (office[row][start_y] == 6):
                break
            elif (office[row][start_y] in CCTV_TYPE):
                continue
            else:
                office[row][start_y] = 7

def calc_seen_space(office, N, M, cctv, rotation_int):
    if (cctv[0] == 1):
        mark_seen_space(office, N, M, cctv[1], cctv[2], rotation_int)
    elif (cctv[0] == 2):
        mark_seen_space(office, N, M, cctv[1], cctv[2], rotation_int)
        mark_seen_space(office, N, M, cctv[1], cctv[2], (rotation_int + 2) % 4)
    elif (cctv[0] == 3):
        mark_seen_space(office, N, M, cctv[1], cctv[2], rotation_int)
        mark_seen_space(office, N, M, cctv[1], cctv[2], (rotation_int + 1) % 4)
    elif (cctv[0] == 4):
        mark_seen_space(office, N, M, cctv[1], cctv[2], rotation_int)
        mark_seen_space(office, N, M, cctv[1], cctv[2], (rotation_int + 1) % 4)
        mark_seen_space(office, N, M, cctv[1], cctv[2], (rotation_int + 2) % 4)
    elif (cctv[0] == 5):
        mark_seen_space(office, N, M, cctv[1], cctv[2], 0)
        mark_seen_space(office, N, M, cctv[1], cctv[2], 1)
        mark_seen_space(office, N, M, cctv[1], cctv[2], 2)
        mark_seen_space(office, N, M, cctv[1], cctv[2], 3)

def count_blind_spots(office, N):
    count = 0
    for i in range(N):
        count += office[i].count(0)
    return count

def find_minimum_blind_spot(office, cctv_list, N, M, minimum_blind_spot, camera_index):
    if (len(cctv_list) == 0):
        return count_blind_spots(office, N)

    for i in range(4):

        office_copy = copy.deepcopy(office)

        cctv_list[camera_index][3][0] = i

        for cctv in cctv_list:
            calc_seen_space(office_copy, N, M, cctv, cctv[3][0])

        min_calc = count_blind_spots(office_copy, N)

        if min_calc < minimum_blind_spot:
            minimum_blind_spot = min(minimum_blind_spot, min_calc)
            if (camera_index + 1 < len(cctv_list)):
                minimum_blind_spot = find_minimum_blind_spot(office, cctv_list, N, M, minimum_blind_spot, camera_index + 1)

        if (camera_index + 1 < len(cctv_list)):
            minimum_blind_spot = find_minimum_blind_spot(office, cctv_list, N, M, minimum_blind_spot, camera_index + 1)


        minimum_blind_spot = min(minimum_blind_spot, min_calc)

    return minimum_blind_spot

def actual_code():
    N, M = map(int, sys.stdin.readline().strip().split())

    CCTV = []
    office = []
    for i in range(N):
        office.append(list(map(int, sys.stdin.readline().strip().split())))
        for j in range(M):
            if office[i][j] in CCTV_TYPE:
                CCTV.append((office[i][j], i, j, [0]))

    minimum_blind_spot = find_minimum_blind_spot(copy.deepcopy(office), copy.deepcopy(CCTV), N, M, N * M, 0)

    sys.stdout.write(str(minimum_blind_spot))

if __name__ == '__main__':
    actual_code()
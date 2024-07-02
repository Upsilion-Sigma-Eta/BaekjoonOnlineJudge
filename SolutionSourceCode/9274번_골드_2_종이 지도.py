import sys
import copy

def actual_code():
    # Ar => row pixel count
    # Ac => column pixel count
    # Tr => row pixel count
    # Tc => column pixel count
    while True:
        try:
            Ar, Ac, Tr, Tc = map(int, sys.stdin.readline().strip().split())

            map_shape_orig = [[0] * (Ac + Tc) for _ in range(Ar + Tr)]
            for i in range(Ar):
                row = (list(sys.stdin.readline().strip()))
                for j in range(Ac):
                    if (row[j] == 'X'):
                        map_shape_orig[Tr + i][Tc + j] = 1

            # Mark starting location
            for i in range(Ar + Tr):
                count = Tc
                for j in range(Ac + Tc - 1, -1, -1):
                    if (map_shape_orig[i][j] == 1):
                       count = 0
                    else:
                        count += 1
                    if (count >= Tc):
                        map_shape_orig[i][j] = 2

            for j in range(Ac + Tc):
                count = Tr
                for i in range(Ar + Tr - 1, -1, -1):
                    if map_shape_orig[i][j] != 2:
                        count = 0
                    else:
                        count += 1
                    if (count >= Tr):
                        map_shape_orig[i][j] = 3

            min_paper_count = Ar * Ac
            for row in range(Tr):
                for col in range(Tc):
                    current_paper_count = 0
                    for r in range(row, Ar + Tr, Tr):
                        for c in range(col, Ac + Tc, Tc):
                            if (map_shape_orig[r][c] != 3):
                                current_paper_count += 1
                    if (current_paper_count < min_paper_count):
                        min_paper_count = current_paper_count

            sys.stdout.write(str(min_paper_count) + "\n")
        except:
            return 0

if __name__ == '__main__':
    actual_code()